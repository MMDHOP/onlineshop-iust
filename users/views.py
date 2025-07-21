from django.shortcuts import render

from django.http import HttpResponse , request
# Create your views here.

def loginpage(request) :
    return HttpResponse('login here')


def signinpage(request) :
    return render(request,'sign_in.html')
    

def profilepage(request) :
    return HttpResponse('your prof')