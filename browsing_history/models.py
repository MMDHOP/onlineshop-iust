from django.db import models
from django.conf import settings
from products.models import Product

class BrowsingHistory(models.Model):

    INTERACTION_CHOICES = [
        ("view", "View"),
        ("cart", "Cart"),
        ("wishlist", "Wishlist"),
        ("like", "Like"),
        ("rating", "Rating"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=20, choices=INTERACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Browsing Histories"
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user} - {self.product} - {self.interaction_type}"
