from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .forms import UserImageForm
from .serializer import LoginSerializer, SignUpSerializer
from user_agents import parse

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignUpAPIView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})

    return render(request, 'login.html')


def sign_up_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')


        errors = {}
        if password != password2:
            errors['password'] = "Passwords do not match."
        if not user_type:
            errors['user_type'] = "User type is required."

        if errors:
            return render(request, 'sign_up.html', {'errors': errors})


        from django.contrib.auth import get_user_model
        User = get_user_model()

        if User.objects.filter(username=username).exists():
            errors['username'] = "Username already exists."
            return render(request, 'sign_up.html', {'errors': errors})

        user = User.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            user_type=user_type,
        )
        user.set_password(password)
        user.save()

        return redirect('login')

    return render(request, 'sign_up.html')




def profile_page(request):
    if request.method == 'POST' and request.FILES.get('profile_image'):
        request.user.profile_image = request.FILES['profile_image']
        request.user.save()
        return redirect('profile')
    
    if not request.user.device_type:
        device = get_device_type(request)
        request.user.device_type = device
        request.user.save()

    return render(request, 'profile.html')



@login_required
@require_POST
def delete_profile_image(request):
    if request.user.profile_image:
        request.user.profile_image.delete()
        request.user.save()
    return redirect('profile')


def logout_view(request):
    logout(request)
    return redirect('home') 



def get_device_type(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    user_agent_parsed = parse(user_agent)

    if user_agent_parsed.is_mobile:
        return 'mobile'
    elif user_agent_parsed.is_tablet:
        return 'tablet'
    elif user_agent_parsed.is_pc:
        return 'desktop'
    else:
        return 'unknown'
