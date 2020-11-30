from django.db import models
from django.db import models
import datetime as dt
from django.contrib.auth.models import User
import cloudinary 
from cloudinary.models import CloudinaryField

# Create your models here.

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
    