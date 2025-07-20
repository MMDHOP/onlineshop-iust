from django.urls import path
from .views import loginpage, signinpage, profilepage

urlpatterns = [
    path('login/',loginpage),
    path('sign-in/',signinpage),
    path('profile/',profilepage)

]