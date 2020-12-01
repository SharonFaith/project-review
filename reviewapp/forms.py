from django import forms
from .models import Projects, Profile
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']