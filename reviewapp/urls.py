from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import welcome, index, search_results, update_profile, profile, single_project, rate_project
from . import views

urlpatterns = [
    path('', welcome, name='welcome'),
    path('landing-page/', index, name='index'),
    path('projects/<project_id>/', single_project, name='single-project'),
    path('profile/<id>/', profile, name='profile'),
    path('rateproject/<proj_id>/', rate_project, name='rate-project'),
    path('api/projects/', views.ProjectList.as_view()),
    path('api/profiles/', views.ProfileList.as_view()),
    path('update_the_profile/<profile_id>', update_profile, name='update-profile'),
    re_path(r'api/projects/project-id/(?P<pk>[0-9]+)/', views.ProjectDescription.as_view()),
    re_path(r'api/profiles/profile-id/(?P<pk>[0-9]+)/', views.ProfileDescription.as_view()),
    path('search/', search_results, name='search-results'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)