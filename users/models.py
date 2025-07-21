from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('buyer', 'buyer'),
        ('seller', 'seller'),
    )
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='buyer',
    )

    def __str__(self):
        return self.username
