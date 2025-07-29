from django.urls import path
from .views import quiz_view , tag_filter_view

urlpatterns = [
    path('quiz/', quiz_view, name='quiz'),
    path('tag/<str:tag>/', tag_filter_view, name='tag_filter'),

]