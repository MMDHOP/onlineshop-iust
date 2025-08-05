from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from django.utils.timezone import now


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
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    USER_TYPE_CHOICES2 = (
        ('dry','dry'),
        ('oily','oily'),
        ('combintion','combintaion'),
        ('sensitive','sensitive'),
    )

    skin_type = MultiSelectField(choices=USER_TYPE_CHOICES2,blank=True)

    SKIN_CONCERNS = [
        ('acne', 'acne'),
        ('dullness', 'dullness'),
        ('wrinkles', 'wrinkles'),
        ('dark_spots', 'dark_spots'),
        ('redness', 'redness'),
        ('pores', 'pores'),
        ('uneven_tone', 'uneven_tone'),
        ('blackheads', 'blackheads'),
        ('puffiness', 'puffiness'),
        ('dark_circles', 'dark_circles'),
    ]

    concern = MultiSelectField(choices=SKIN_CONCERNS,blank=True)

    SKIN_PREFERENCES = (
        ('fragrance_free', 'fragrance_free'),
        ('alcohol_free', 'alcohol_free'),
        ('cruelty_free', 'cruelty_free'),
        ('vegan', 'vegan'),
        ('paraben_free', 'paraben_free'),
        ('non_comedogenic', 'non_comedogenic'),
        ('dermatologist_tested', 'dermatologist_tested'),
        ('eco_friendly', 'eco_friendly'),
        ('sulfate_free', 'sulfate_free'),
        ('natural_ingredients', 'natural_ingredients'),
    )
    preferences = MultiSelectField(choices=SKIN_PREFERENCES,blank=True)

    device_type = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.username
