from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , request , response 
from django.contrib.auth.decorators import login_required

from rest_framework import generics , permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Cart , CartItem
from .serialzers import CartItemSerializer , CartSerialazer
from browsing_history.models import BrowsingHistory




class CartApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)

        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            item = serializer.save(cart=cart)

            BrowsingHistory.objects.create(
                user=user,
                product=item.product,
                interaction_type='cart'
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
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



@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart-detail')
