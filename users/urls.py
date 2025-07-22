from django.urls import path
from .views import (
    LoginAPIView,
    SignUpAPIView,
    sign_up_page,
    login_page,
    # profile_page
)

urlpatterns = [
    # API endpoints
    path('api/login/', LoginAPIView.as_view(), name='login_api'),
    path('api/signup/', SignUpAPIView.as_view(), name='signup_api'),

    # HTML pages
    path('login/', login_page, name='login'),
    path('sign-up/', sign_up_page, name='sign_up'),
    # path('profile/', profile_page, name='profile'),
]
