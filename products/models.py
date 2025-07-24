from django.db import models

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

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    brand = models.CharField(max_length=100, blank=True)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
