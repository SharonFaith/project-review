from django.contrib import admin
from .models import Projects, Profile, Rating


# Register your models here.
admin.site.register(Projects)
admin.site.register(Profile)
admin.site.register(Rating)