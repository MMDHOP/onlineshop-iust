from django.db import models
from django.contrib.auth.models import AbstractUser\

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

    skin_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES2,
        default='oily',

    )

    SKIN_CONCERNS = (
    ('acne', 'Acne (جوش)'),
    ('dullness', 'Dullness (کدر بودن پوست)'),
    ('wrinkles', 'Wrinkles & Fine Lines (چین و چروک)'),
    ('dark_spots', 'Dark Spots (لک‌های تیره)'),
    ('redness', 'Redness (قرمزی پوست)'),
    ('pores', 'Large Pores (منافذ باز)'),
    ('uneven_tone', 'Uneven Skin Tone (ناهمواری رنگ پوست)'),
    ('blackheads', 'Blackheads (جوش سرسیاه)'),
    ('puffiness', 'Puffiness (پف پوست)'),
    ('dark_circles', 'Dark Circles (تیرگی دور چشم)'),
)

    concern = models.ManyToManyField(choices=SKIN_CONCERNS,blank=True)

    def __str__(self):
        return self.username
