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
    concern = MultiSelectField(choices=SKIN_CONCERNS,blank=True)

    SKIN_PREFERENCES = (
        ('fragrance_free', 'Fragrance-Free (بدون عطر)'),
        ('alcohol_free', 'Alcohol-Free (بدون الکل)'),
        ('cruelty_free', 'Cruelty-Free (تست نشده روی حیوانات)'),
        ('vegan', 'Vegan (کاملاً گیاهی)'),
        ('paraben_free', 'Paraben-Free (بدون پارابن)'),
        ('non_comedogenic', 'Non-Comedogenic (نمسدودکننده منافذ نیست)'),
        ('dermatologist_tested', 'Dermatologist Tested (تایید شده توسط متخصص پوست)'),
        ('eco_friendly', 'Eco-Friendly (سازگار با محیط زیست)'),
        ('sulfate_free', 'Sulfate-Free (بدون سولفات)'),
        ('natural_ingredients', 'Natural Ingredients (ترکیبات طبیعی)'),
    )
    preferences = MultiSelectField(choices=SKIN_PREFERENCES,blank=True)

    device_type = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.username
