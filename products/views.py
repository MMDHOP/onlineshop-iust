from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , request , response 

from rest_framework import generics , permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

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
    


def products_list_view(request, products, title):
    return render(request, 'products_list.html', {'products': products, 'title': title})



def tag_filter_view(request, tag):
    products = Product.objects.filter(tags__contains=[tag])
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

