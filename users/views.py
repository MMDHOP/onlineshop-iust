from django.shortcuts import render

from django.http import HttpResponse , request
# Create your views here.

def loginpage(request) :
    return HttpResponse('login here')


def signinpage(request) :
    return HttpResponse('sign in here pedarsag')
    

def profilepage(request) :
    return HttpResponse('your prof')