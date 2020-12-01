from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Projects, Profile
from django.core.exceptions import ObjectDoesNotExist
#from .forms import NewsLetterForm, NewArticleForm, MerchForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer, ProfileSerializer
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
   

class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format = None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many = True)

        return Response(serializers.data)

    def post(self, request, format = None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_profile(self, pk):
        

        try:
            return Profile.objects.get(pk=pk)
            #print(MoringaMerch.objects.get(pk=pk))
        except Profile.DoesNotExist:
            raise Http404()
            

    def get(self, request, pk, format=None):
        #try:
        #    merch = self.get_merch(pk)
        #except ObjectDoesNotExist:
        #    return Http404
        
            profile = self.get_profile(pk)

            serializers = ProfileSerializer(profile)
            return Response(serializers.data)
       
    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ProjectList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format = None):
        all_projects = Projects.objects.all()
        serializers = ProjectSerializer(all_projects, many = True)

        return Response(serializers.data)

    def post(self, request, format = None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_project(self, pk):
        

        try:
            return Projects.objects.get(pk=pk)
            #print(MoringaMerch.objects.get(pk=pk))
        except Projects.DoesNotExist:
            raise Http404()
            

    def get(self, request, pk, format=None):
        #try:
        #    merch = self.get_merch(pk)
        #except ObjectDoesNotExist:
        #    return Http404
        
            project = self.get_project(pk)

            serializers = ProjectSerializer(project)
            return Response(serializers.data)
       
    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project, request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

