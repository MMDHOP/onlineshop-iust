from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , request , response 
from django.contrib.auth.decorators import login_required

from rest_framework import generics , permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Cart , CartItem
from .serialzers import CartItemSerializer , CartSerialazer



class CartApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        print("Request data:", request.data)
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)

        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cart=cart)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('CartItemSerializer errors:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@login_required
def profile_view(request):
    cart = Cart.objects.filter(user=request.user).first()
    cart_items = cart.items.select_related('product') if cart else []

    return render(request, 'profile.html', {
        'user': request.user,
        'cart_items': cart_items,
    })


@login_required
def cart_detail_view(request):
    cart = Cart.objects.filter(user=request.user).first()
    cart_items = cart.items.select_related('product') if cart else []

    return render(request, 'cart_detail.html', {'cart_items': cart_items})
