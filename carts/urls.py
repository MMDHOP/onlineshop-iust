from django.urls import path
from .views import CartApiView, profile_view, cart_detail_view, remove_from_cart

urlpatterns = [
    path('api/cart/', CartApiView.as_view(), name='add-to-cart'),
    path('profile/', profile_view, name='profile'),
    path('cart/', cart_detail_view, name='cart-detail'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]
