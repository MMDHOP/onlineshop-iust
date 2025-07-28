from rest_framework import serializers

from .models import Cart , CartItem
from users.models import CustomUser 
from products.models import Product


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=8, decimal_places=2, read_only=True)
    cart = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name', 'product_price', 'quantity', 'cart']

    def validate_product(self, value):
        if not Product.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Invalid product")
        return value



class CartSerialazer(serializers.ModelSerializer) :
    items = CartItemSerializer(many=True, read_only=True)
    class Meta :
        model = Cart
        fields = ['user','created_at','updated_at','items']



