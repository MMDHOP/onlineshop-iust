from django.urls import path
from .views import GenerateRoutineFromQuiz, UserRoutineView , user_routine_page

urlpatterns = [
    path('api/routine/generate/', GenerateRoutineFromQuiz.as_view(), name='generate-routine'),
    path('api/routine/', UserRoutineView.as_view(), name='get-routine'),
     path('routine/', user_routine_page, name='routine'),
]
