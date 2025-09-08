from django.db import models
from django.conf import settings
from products.models import Product

# Create your models here.



class BrowsingHisrory(models.Model) :

    INTERACTION_CHOICES = [
        ("view", "View"),
        ("like", "Like"),
        ("wishlist", "Wishlist"),
        ("cart", "Cart"),
    ]



    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    interaction_type = models.CharField(max_length=20,choices=INTERACTION_CHOICES)
    
