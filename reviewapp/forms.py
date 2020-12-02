from django import forms
from .models import Projects, Profile, Rating
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class UpdateProfileForm(forms.Form):
    profile_pic = forms.ImageField(required=True)
    bio = forms.CharField(max_length=255, required=True)
    phone_number = forms.CharField(max_length=10, required=True)

class UploadProject(forms.ModelForm):

    class Meta:
        model = Projects
        exclude = ['profile']

design,usability
content


class RatingsForm(forms.ModelForm):

    class Meta:
        model = Rating
        exclude = ['user_rating', 'project_rated', 'overall']


