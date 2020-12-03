from django import forms
from .models import Projects, Profile, Rating
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField

class UpdateProfile(forms.ModelForm):
    profile_pic = forms.ImageField(required=True)
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


CHOICES = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]
class RatingsForm(forms.ModelForm):
    design = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    usability = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    content= forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = Rating
        exclude = ['user_rating', 'project_rated', 'overall']


