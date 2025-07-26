from django.urls import path
from .views import (
    LoginAPIView,
    SignUpAPIView,
    sign_up_page,
    login_page,
    profile_page,
    logout_view,
    delete_profile_image,
    edit_profile
)

urlpatterns = [
    # API
    path('api/login/', LoginAPIView.as_view(), name='login_api'),
    path('api/signup/', SignUpAPIView.as_view(), name='signup_api'),

    # HTML 
    path('login/', login_page, name='login'),
    path('sign-up/', sign_up_page, name='sign_up'),
    path('profile/',profile_page,name='profile'),
    path('logout/', logout_view, name='logout'), 
    path('profile/edit/delete-image/', delete_profile_image, name='delete_profile_image'),
    path('profile/edit/', edit_profile, name='edit_profile'),
 

]
