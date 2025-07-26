from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('cleanser', 'cleanser'),
        ('Toner-Essence', 'Toner-Essence'),
        ('Serum-Treatments', 'Serum-Treatments'),
        ('Moisturizer', 'Moisturizer'),
        ('Sunscreen', 'Sunscreen'),
        ('Exfoliator', 'Exfoliator'),
        ('Mask', 'Mask'),
        ('Eye-Care', 'Eye-Care'),
    ]
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

    INGREDIENTS = (
        # مواد مرطوب‌کننده و آبرسان:
        ('hyaluronic_acid', 'Hyaluronic Acid (اسید هیالورونیک)'),
        ('glycerin', 'Glycerin (گلیسیرین)'),
        ('squalane', 'Squalane (اسکوالان)'),
        ('panthenol', 'Panthenol (پانتنول)'),
        ('aloe_vera', 'Aloe Vera (آلوئه‌ورا)'),
        # ایه‌بردارهای شیمیایی:
        ('salicylic_acid', 'Salicylic Acid (اسید سالیسیلیک)'),
        ('glycolic_acid', 'Glycolic Acid (اسید گلیکولیک)'),
        ('lactic_acid', 'Lactic Acid (اسید لاکتیک)'),
        ('mandelic_acid', 'Mandelic Acid (اسید ماندلیک)'),
        ('azelaic_acid', 'Azelaic Acid (اسید آزلائیک)'),
        #  روشن‌کننده‌ها و ضدلک:
        ('vitamin_c', 'Vitamin C (ویتامین سی)'),
        ('arbutin', 'Arbutin (آربوتین)'),
        ('kojic_acid', 'Kojic Acid (اسید کوجیک)'),
        ('licorice_extract', 'Licorice Extract (عصاره شیرین‌بیان)'),
        ('niacinamide', 'Niacinamide (نیاسینامید)'),
        # مواد محافظت‌کننده:
        ('zinc_oxide', 'Zinc Oxide (اکسید روی)'),
        ('titanium_dioxide', 'Titanium Dioxide (دی‌اکسید تیتانیوم)'),
        ('green_tea_extract', 'Green Tea Extract (عصاره چای سبز)'),
        ('vitamin_e', 'Vitamin E (ویتامین E)'),
        ('centella_asiatica', 'Centella Asiatica (سنتلا آسیاتیکا/علف ببر)'),
        #  مواد طبیعی معروف:
        ('rosehip_oil', 'Rosehip Oil (روغن نسترن وحشی)'),
        ('argan_oil', 'Argan Oil (روغن آرگان)'),
        ('tea_tree_oil', 'Tea Tree Oil (روغن درخت چای)'),
        ('chamomile_extract', 'Chamomile Extract (عصاره بابونه)'),
        ('caffeine', 'Caffeine (کافئین - ضد پف و تیرگی)'),
        # مواد ضدپیری (Anti-aging):
        ('retinol', 'Retinol (رتینول)'),
        ('retinaldehyde', 'Retinaldehyde (رتین‌آلدئید)'),
        ('bakuchiol', 'Bakuchiol (باکوچیول، جایگزین گیاهی رتینول)'),
        ('peptides', 'Peptides (پپتیدها)'),
        ('collagen', 'Collagen (کلاژن)'),
        ('dimethicone', 'Dimethicone (دیمتیکون - پایه سیلیکونی)'),
        # مواد آرایشی رایج:
        ('mica', 'Mica (میکا - براق‌کننده)'),
        ('iron_oxides', 'Iron Oxides (رنگدانه‌های اکسید آهن)'),
        ('talc', 'Talc (تالک)'),
        ('silica', 'Silica (سیلیکا)'),

    )

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    brand = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    skin_type = MultiSelectField(choices=SKIN_TYPES,blank=True)
    concern_targeted = MultiSelectField(choices=CONCERNS_TARGETS,blank=True)
    preferences = MultiSelectField(choices=PREFERENCES,blank=True)
    ingredient = MultiSelectField(choices=INGREDIENTS,blank=True)
    rating = models.FloatField(
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(5.0)
            ]
            ,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    # tags = 

    def __str__(self):
        return self.name
