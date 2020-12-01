from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Projects, Profile
from django.core.exceptions import ObjectDoesNotExist
from .forms import UpdateProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer, ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from .request import get_profiles, get_projects, get_a_profile, get_a_project, update_a_profile
from decouple import config

# Create your views here.


def logout_view(request):
    logout(request)

    return redirect(index)


def welcome(request):

   return redirect(index)


def index(request):

   projects = get_projects()

   return render(request, 'index.html', {'projects':projects})

def search_results(request):
   if 'title' in request.GET and request.GET['title']:
      search_term = request.GET.get('title')
      searched_projects = Projects.objects.filter(title__icontains= search_term)
     
      message = f'{search_term}'

      return render(request, 'search.html', {'message':message, 'searched_projects':searched_projects})

   else:
      message = 'You have not searched for any term'

      return render(request, 'search.html', {'message':message})

def single_project(request, project_id):
    
    project = get_a_project(project_id)

    return render(request, 'singleproject.html', {'project':project})

@login_required(login_url='/accounts/login')
def rate_project(request, proj_id):

    return render(request, 'rateform.html')


@login_required(login_url='/accounts/login')
def profile(request, id):
  
   users = User.objects.all()
   #followed_users = UserFollowing.objects.all()
   #user_key = person being followed
   #following_user_id = user logged in who followed
   
      #if followed_user.following_user_id == current_user :
         

   
   logged_user = request.user
   current_user = User.objects.filter(id = id).first()
   
   #followers = current_user.followers.all()

   #current_follower = None
  

   #print(current_user.following_user_id)

   profiles = get_profiles()

   #projects = current_user.projects.all()
   
  
   #profiles = Profile.objects.all()
 #  print(profiles)
   current_profile = None

 #  print(current_user.id)

   for user_profile in profiles:
 #     print(profile.insta_user)
      if user_profile.user == current_user:
         current_profile = user_profile

   print(current_profile)
   if current_profile == None:
      current_profile = Profile.objects.create(user= current_user)

 
   #print(UserFollowing.objects.all())

   projects = current_profile.projects.all()
   
   return render(request, 'profile/profile.html', {'user_profile': current_profile, 'projects': projects, 'current_user':current_user,  })

@login_required(login_url='/accounts/login')
def update_profile(request):
    current_user = request.user

    id = current_user.profile.first().id
    print(id)

    if request.method == 'POST':
        form = UpdateProfile(request.POST, request.FILES)
        if form.is_valid():
            updated_profile = form.save(commit=False)
            profile_pic = updated_profile.profile_pic
            bio = updated_profile.bio
            phone_number = updated_profile.phone_number 

            update_a_profile(id, profile_pic, bio, phone_number)

            return redirect(profile, id = id)
   # else:
    
    form = UpdateProfile()

    return render(request, 'profile/update_profile.html', {'form': form})

   

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

