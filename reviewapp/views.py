from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
#from .models import Article, NewsLetterRecipients, MoringaMerch, Projects, Profile, CloudinaryTest
from django.core.exceptions import ObjectDoesNotExist
#from .forms import NewsLetterForm, NewArticleForm, MerchForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
#from .serializer import MerchSerializer, ProjectSerializer, ProfileSerializer, CloudinaryTestSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
#from .request import get_movies, get_merch, post_merch, get_a_merch, update_a_merch
from decouple import config

# Create your views here.


def logout_view(request):
    logout(request)

    return redirect(index)


def welcome(request):

   return redirect(index)


def index(request):

   return render(request, 'index.html')
   


# Create your views here.
