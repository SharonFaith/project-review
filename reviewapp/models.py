from django.db import models
import datetime as dt
from django.contrib.auth.models import User
import cloudinary 
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = None, related_name='profile')
    profile_pic = CloudinaryField(blank=True, null=True)
    bio = models.TextField(blank =True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    
    def __str__(self):
        return self.user.username


class Projects(models.Model):
    profile= models.ForeignKey(Profile, on_delete=models.CASCADE, default = None, related_name='projects')
    title = models.CharField(max_length = 30)
    landing_page = CloudinaryField()
    description = models.TextField()
    live_site = models.URLField()

class New(models.Model):
    name = models.CharField(max_length=30)


class DisplayProfile:
    def __init__(self, id, user, profile_pic, bio, phone_number, projects):
        self.id = id
        self.user = user
        self.profile_pic = profile_pic
        self.bio = bio
        self.phone_number = phone_number
        self.projects = projects

class DisplayProjects:
    def __init__(self, id, profile, title, landing_page, description, live_site):
        self.id = id
        self.profile = profile
        self.title = title
        self.landing_page = landing_page
        self.description = description
        self.live_site = live_site

