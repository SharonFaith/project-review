from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import welcome, index
from django.conf.urls.static import static

urlpatterns = [
    path('', welcome, name='welcome'),
    path('landing-page/', index, name='index'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)