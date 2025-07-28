from django.urls import path
from .views import *

urlpatterns = [
    path('category/',category_page),
    path('category/cleanser/',cleanser_page),
    path('category/Toner-Essence/',Toner_Essence_page),
    path('category/Serum-Treatments/',Serum_Treatments_page),
    path('category/Moisturizer/',Moisturizer_page),
    path('category/Sunscreen/',Sunscreen_page),
    path('category/Exfoliator/',Exfoliator_page),
    path('category/Mask/',Mask_page),
    path('category/Eye-Care/',Eye_Care_page),
    path('category/<slug:slug>/', every_product_page, name='product_detail'),
    path('comments/add/', AddingComments.as_view(), name='add-comment'),

]


