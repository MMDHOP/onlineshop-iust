from django.urls import path
from .views import browsing_history_view, clear_browsing_history, product_interaction

urlpatterns = [
    path('browsing-history/', browsing_history_view, name='browsing_history'),
    path('browsing-history/clear/', clear_browsing_history, name='clear_browsing_history'),
    path('product/<int:product_id>/interact/', product_interaction, name='product_interaction'),
]
