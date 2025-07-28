from django.urls import path
from .views import CartApiView , profile_view , cart_detail_view

urlpatterns = [
    # ...
    path('api/cart/', CartApiView.as_view(), name='add-to-cart'),
    path('profile/', profile_view, name='profile'),
    path('cart/', cart_detail_view, name='cart-detail'),
]

