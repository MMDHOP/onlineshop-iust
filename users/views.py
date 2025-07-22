from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import LoginSerializer, SignUpSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=request.data.get('password')
            )
            if user:
                login(request, user)  # Django session login
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SignUpAPIView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# HTML page for signup
def sign_up_page(request):
    return render(request, 'sign_up.html')  # make sure you have templates/sign_up.html


# HTML page for login
def login_page(request):
    return render(request, 'login.html')  # make sure you have templates/sign_in.html


# Profile page (only for logged in users)
# @login_required
# def profile_page(request):
#     return render(request, 'profile.html', {"user": request.user})
