from rest_framework import serializers
from .models import Routine
from products.models import Product

class StepSerializer(serializers.Serializer):
    step_name = serializers.CharField()
    product_id = serializers.IntegerField()
    product_name = serializers.SerializerMethodField()

    def get_product_name(self, obj):
        product = Product.objects.filter(id=obj['product_id']).first()
        return product.name if product else None

class RoutineSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)

    class Meta:
        model = Routine
        fields = ['routine_id', 'plan_name', 'steps', 'created_at']
