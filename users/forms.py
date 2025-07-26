from django import forms
from django import forms
from django.contrib.auth import get_user_model

from multiselectfield.forms.fields import MultiSelectFormField
from django.forms import CheckboxSelectMultiple

from .models import CustomUser

User = get_user_model()

class UserImageForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_image']



User = get_user_model()

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'user_type', 'skin_type', 'concern', 'preferences', 'profile_image'
        ]
        widgets = {
            'concern': CheckboxSelectMultiple,
            'preferences': CheckboxSelectMultiple,
        }
