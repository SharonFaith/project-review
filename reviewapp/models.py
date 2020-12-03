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

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile(cls, id, updates):
        to_update = cls.objects.filter(id = id)
        to_update.update(bio = updates)


class Projects(models.Model):
    profile= models.ForeignKey(Profile, on_delete=models.CASCADE, default = None, related_name='projects')
    title = models.CharField(max_length = 30)
    landing_page = CloudinaryField()
    description = models.TextField()
    live_site = models.URLField()

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def update_project(cls, id, updates):
        to_update = cls.objects.filter(id = id)
        to_update.update(description = updates)


class New(models.Model):
    name = models.CharField(max_length=30)

class Rating(models.Model):
    user_rating = models.ForeignKey(User, on_delete=models.CASCADE, default = None, related_name='ratings_done')
    project_rated = models.ForeignKey(Projects, on_delete=models.CASCADE,default = None, related_name='ratings')
    #design = models.IntegerField()
    #usability = models.IntegerField()
    #content= models.IntegerField()
    #overall= models.IntegerField()
    design = models.DecimalField(max_digits=4, decimal_places=2)
    usability = models.DecimalField(max_digits=4, decimal_places=2)
    content= models.DecimalField(max_digits=4, decimal_places=2)
    overall= models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        unique_together = ('user_rating', 'project_rated')


    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()

    @classmethod
    def update_rating(cls, id, updates):
        to_update = cls.objects.filter(id = id)
        to_update.update(usability = updates)




class DisplayProfile:

    api_profile_list = []

    def __init__(self, id, user, profile_pic, bio, phone_number, projects):
        self.id = id
        self.user = user
        self.profile_pic = profile_pic
        self.bio = bio
        self.phone_number = phone_number
        self.projects = projects

    def save_profile(self):
        '''
        method that appends profile to list
        '''
        DisplayProfile.api_profile_list.append(self)

class DisplayProjects:
    api_projects_list = []
    def __init__(self, id, profile, title, landing_page, description, live_site):
        self.id = id
        self.profile = profile
        self.title = title
        self.landing_page = landing_page
        self.description = description
        self.live_site = live_site

    def save_project(self):
        '''
        method that appends project to list
        '''
        DisplayProjects.api_projects_list.append(self)
