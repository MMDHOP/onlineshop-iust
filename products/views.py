from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , request , response 


from rest_framework import generics , permissions, status
from rest_framework.views import APIView

from .models import Product , Comments
from .serialzers import CommentsSerialzer


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


def every_product_page(request,slug) :
    product = get_object_or_404(Product , slug=slug)
    return render(request, 'every_product.html' , {'product' : product})


class AddingComments(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CommentsSerialzer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save(user=request.user)
            slug = comment.product.slug 
            return redirect('product_detail', slug=slug)
        return redirect(request.META.get('HTTP_REFERER', '/'))