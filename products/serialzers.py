from rest_framework import serializers
from .models import Comments , Product
from users.models import CustomUser 


class CommentsSerialzer(serializers.ModelSerializer) :

    user = serializers.StringRelatedField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta :
        model = Comments
        fields = ['user','product','text']
        only_read_fields = ['craeted_at','user']