from rest_framework import serializers
from .models import Comments , Product , Ratings
from users.models import CustomUser 


class CommentsSerialzer(serializers.ModelSerializer) :

    user = serializers.StringRelatedField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta :
        model = Comments
        fields = ['user','product','text']
        read_only_fields = ['craeted_at','user']

class RatingsSerialzer(serializers.ModelSerializer) :

    user = serializers.StringRelatedField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta :
        model = Ratings
        unique_together = ('user', 'product')
        fields = ['user','product','score']
        read_only_fields = ['craeted_at','user']
