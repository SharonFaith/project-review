from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import welcome, index, search_results
from . import views

urlpatterns = [
    path('', welcome, name='welcome'),
    path('landing-page/', index, name='index'),
    path('api/projects/', views.ProjectList.as_view()),
    path('api/profiles/', views.ProfileList.as_view()),
    re_path(r'api/projects/project-id/(?P<pk>[0-9]+)/', views.ProjectDescription.as_view()),
    re_path(r'api/profiles/profile-id/(?P<pk>[0-9]+)/', views.ProfileDescription.as_view()),
    path('search/', search_results, name='search-results'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)