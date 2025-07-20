from django.http import HttpResponse , request
from django.shortcuts import render

# from templates import home
# from static import home_style


def homepage(request) :
    return render(request, 'home.html')
    