from django.shortcuts import render

from django.http import HttpResponse , request
# Create your views here.

def category_page(request):
    return HttpResponse('sklcnkjndclk')

def cleanser_page(request) :
    return HttpResponse('all cleansers')

def Toner_Essence_page(request) :
    return HttpResponse('all Toner & Essence')

def Serum_Treatments_page(request) :
    return HttpResponse('all Serum & Treatments')

def Moisturizer_page(request) :
    return HttpResponse('all Moisturizer')

def Sunscreen_page(request) :
    return HttpResponse('all Sunscreen')

def Exfoliator_page(request) :
    return HttpResponse('all Exfoliator	')

def Mask_page(request) :
    return HttpResponse('all Masks')

def Eye_Care_page(request) :
    return HttpResponse('all Eye_Care')