from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.conf import settings

from users.models import CustomUser 

from multiselectfield import MultiSelectField
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

    INGREDIENTS = [
        # Hydrating
        ('hyaluronic_acid', 'hyaluronic_acid'),
        ('glycerin', 'glycerin'),
        ('squalane', 'squalane'),
        ('panthenol', 'panthenol'),
        ('aloe_vera', 'aloe_vera'),
        # Exfoliants
        ('salicylic_acid', 'salicylic_acid'),
        ('glycolic_acid', 'glycolic_acid'),
        ('lactic_acid', 'lactic_acid'),
        ('mandelic_acid', 'mandelic_acid'),
        ('azelaic_acid', 'azelaic_acid'),
        # Brightening
        ('vitamin_c', 'vitamin_c'),
        ('arbutin', 'arbutin'),
        ('kojic_acid', 'kojic_acid'),
        ('licorice_extract', 'licorice_extract'),
        ('niacinamide', 'niacinamide'),
        # Protection
        ('zinc_oxide', 'zinc_oxide'),
        ('titanium_dioxide', 'titanium_dioxide'),
        ('green_tea_extract', 'green_tea_extract'),
        ('vitamin_e', 'vitamin_e'),
        ('centella_asiatica', 'centella_asiatica'),
        # Natural
        ('rosehip_oil', 'rosehip_oil'),
        ('argan_oil', 'argan_oil'),
        ('tea_tree_oil', 'tea_tree_oil'),
        ('chamomile_extract', 'chamomile_extract'),
        ('caffeine', 'caffeine'),
        # Anti-aging
        ('retinol', 'retinol'),
        ('retinaldehyde', 'retinaldehyde'),
        ('bakuchiol', 'bakuchiol'),
        ('peptides', 'peptides'),
        ('collagen', 'collagen'),
        ('dimethicone', 'dimethicone'),
        # Cosmetic
        ('mica', 'mica'),
        ('iron_oxides', 'iron_oxides'),
        ('talc', 'talc'),
        ('silica', 'silica'),
    ]

    TAGS_CHOICES = CATEGORY_CHOICES + SKIN_TYPES + CONCERNS_TARGETS + PREFERENCES + INGREDIENTS

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
    tags = MultiSelectField(choices=TAGS_CHOICES,blank=True)
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            num = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class Comments(models.Model) :

    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"
