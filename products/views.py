from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , request , response 
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Value , Q , Count ,FloatField
from django.db.models.functions import Coalesce

from rest_framework import generics , permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from functools import reduce
from operator import or_

from .models import Product , Comments , Ratings
from .serialzers import CommentsSerialzer , RatingsSerialzer
from browsing_history.views import BrowsingHistory


# Create your views here.

def category_page(request):
    return render(request, 'category.html')

def every_category_page(request, name, category):
    products = Product.objects.filter(category=category)
    return render(request, 'products_list.html', {'products': products, 'title': name})

def cleanser_page(request) :
    return every_category_page(request, 'cleanser', 'cleanser')

def Toner_Essence_page(request) :
    return every_category_page(request, 'Toner Essence', 'Toner-Essence')

def Serum_Treatments_page(request) :
    return every_category_page(request, 'Serum Treatmentse', 'Serum-Treatments')

def Moisturizer_page(request) :
    return every_category_page(request, 'Moisturizer', 'Moisturizer')

def Sunscreen_page(request) :
    return every_category_page(request, 'Sunscreen', 'Sunscreen')


def Exfoliator_page(request) :
    return every_category_page(request, 'Exfoliator', 'Exfoliator')


def Mask_page(request) :
    return every_category_page(request, 'Mask', 'Mask')


def Eye_Care_page(request):
    return every_category_page(request, 'Eye Care', 'Eye-Care')



def every_product_page(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.user.is_authenticated:
        BrowsingHistory.objects.create(
            user=request.user,
            product=product,
            interaction_type='view'
        )
    user_rating = None
    if request.user.is_authenticated:
        user_rating = product.ratings.filter(user=request.user).first()
    
    avg_rating = product.ratings.aggregate(avg=Avg('score'))['avg'] or 0

    return render(request, 'every_product.html', {
        'product': product,
        'user_rating': user_rating,
        'avg_rating': round(avg_rating, 1),
    })



class AddingComments(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CommentsSerialzer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save(user=request.user)
            slug = comment.product.slug 
            return redirect('product_detail', slug=slug)
        return redirect(request.META.get('HTTP_REFERER', '/'))
    


class RatingProducts(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        product_id = request.data.get("product")
        score = request.data.get("score")
        product = Product.objects.filter(id=product_id).first()
        if not product:
            return Response({"error": "Product not found"}, status=404)

        if Ratings.objects.filter(user=request.user, product=product).exists():
            return Response({"error": "Already rated"}, status=400)

        Ratings.objects.create(user=request.user, product=product, score=score)

        BrowsingHistory.objects.create(
            user=request.user,
            product=product,
            interaction_type='rating'
        )

        if int(score) > 3:
            BrowsingHistory.objects.get_or_create(user=request.user, product=product, interaction_type='like')
            BrowsingHistory.objects.get_or_create(user=request.user, product=product, interaction_type='wishlist')

        return Response({"success": True})


def products_list_view(request, products, title=None, html=None):
    context = {'products': products, 'title': title}
    if html:
        if html == 'home.html':
            context = {'latest_products': products}
        return render(request, html, context)
    return render(request, 'products_list.html', context)


def tag_filter_view(request, tag):
    products = Product.objects.filter(tags__contains=tag)
    li = ['cleanser','Toner-Essence','Serum-Treatments','Moisturizer','Sunscreen','Exfoliator','Mask','Eye-Care'] 
    if tag == li[0] :
        return cleanser_page(request)
    elif tag == li[1] :
        return Toner_Essence_page(request)
    elif tag == li[2] :
        return Serum_Treatments_page(request)
    elif tag == li[3] :
        return Moisturizer_page(request)
    elif tag == li[4] :
        return Sunscreen_page(request)
    elif tag == li[5] :
        return Exfoliator_page(request)
    elif tag == li[6] :
        return Mask_page(request)
    elif tag == li[7] :
        return Eye_Care_page(request)


    return products_list_view(request, products, title=f"Tag: {tag}")




def homepage(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    skin_matched_products = []
    concerns_matched_products = []
    preferences_matched_products = []

    if request.user.is_authenticated:
        user_skin_types = request.user.skin_type or []
        user_concerns = request.user.concern or []
        user_preferences = request.user.preferences or []

        if user_skin_types:
            skin_query = reduce(or_, (Q(skin_type__icontains=skin) for skin in user_skin_types))
            skin_matched_products = Product.objects.filter(skin_query).distinct()[:5]

        if user_concerns:
            print("User concerns:", user_concerns)
            concern_query = reduce(or_, (Q(concern_targeted__icontains=c) for c in user_concerns))
            concerns_matched_products = Product.objects.filter(concern_query).distinct()[:5]
            print("Matched concerns:", concerns_matched_products)


        if user_preferences:
            preference_query = reduce(or_, (Q(preferences__icontains=p) for p in user_preferences))
            preferences_matched_products = Product.objects.filter(preference_query).distinct()[:5]

    context = {
        'latest_products': latest_products,
        'skin_matched_products': skin_matched_products,
        'concerns_matched_products': concerns_matched_products,
        'preferences_matched_products': preferences_matched_products,
    }
    return render(request, 'home.html', context)




def search_products(request):
    query = request.GET.get('q', '').lower().strip()
    keywords = query.split()

    user = request.user if request.user.is_authenticated else None

    products = Product.objects.all()

    if user:
        user_filters = Q()

        if user.skin_type:
            for st in user.skin_type:
                user_filters |= Q(skin_type__icontains=st)

        if user.concern:
            for c in user.concern:
                user_filters |= Q(concern_targeted__icontains=c)

        if user.preferences:
            for p in user.preferences:
                user_filters |= Q(preferences__icontains=p)

        if user_filters:
            products = products.filter(user_filters)


    if keywords:
        q_objects = Q()
        for word in keywords:
            q_objects |= (
                Q(name__icontains=word) |
                Q(description__icontains=word) |
                Q(skin_type__icontains=word) |
                Q(concern_targeted__icontains=word) |
                Q(preferences__icontains=word)
            )
        products = products.filter(q_objects)


    POSITIVE_KEYWORDS = [
    'عالی', 'خوب', 'محشر', 'فوق‌العاده', 'بی‌نظیر', 'عالیه', 'زیبا', 'خوشمزه', 'مناسب', 'با کیفیت', 'عالی‌ترین',
    'good', 'excellent', 'love', 'amazing', 'high quality', 'best', 'awesome', 'perfect', 'fantastic', 'great'              
    ]

    products = products.annotate(num_comments=Count('comments'))

    comment_q = Q()
    for word in POSITIVE_KEYWORDS:
        comment_q |= Q(comments__text__icontains=word)

    products = products.filter(comment_q | Q(num_comments=0)).distinct()


    products = products.annotate(
        avg_rating=Coalesce(
            Avg('ratings__score'),
            Value(1, output_field=FloatField()) 
        )
    ).order_by('-avg_rating', 'created_at')


    return render(request, "search_results.html", {"results": products, "query": query})
