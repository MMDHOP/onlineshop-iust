from django.db import models
from multiselectfield import MultiSelectField

from django.conf import settings

# Create your models here.

class Quiz(models.Model) :
            
    CONCERNS_TARGETS = [
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

    SKIN_TYPES = [
        ('dry','dry'),
        ('oily','oily'),
        ('combination','combination'),
        ('sensitive','sensitive'),
    ]

    PREFERENCES = [
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
    ]

    TAGS_CHOICES =  SKIN_TYPES + CONCERNS_TARGETS + PREFERENCES 


    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    skin_type = MultiSelectField(choices=SKIN_TYPES,blank=True)
    concern_targeted = MultiSelectField(choices=CONCERNS_TARGETS,blank=True)
    preferences = MultiSelectField(choices=PREFERENCES,blank=True)
    tags = MultiSelectField(choices=TAGS_CHOICES,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
