from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class Quiz(models.Model) :
            
    SKIN_TYPES = (
        ('dry','dry'),
        ('oily','oily'),
        ('combintion','combintaion'),
        ('sensitive','sensitive'),
    )
    PREFERENCES = (
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

    CONCERNS_TARGETS = (
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


    user_id = models.ForeignKey('users.CustomUser',on_delete=models.CASCADE)
    skin_type = MultiSelectField(choices=SKIN_TYPES,blank=True)
    concern_targeted = MultiSelectField(choices=CONCERNS_TARGETS,blank=True)
    preferences = MultiSelectField(choices=PREFERENCES,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
