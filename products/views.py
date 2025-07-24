from django.shortcuts import render

from django.http import HttpResponse , request

from .models import Product
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




