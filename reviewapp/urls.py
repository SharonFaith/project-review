from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
#from .views import welcome, index, profile, upload_image, update_profile, search_results, single_image, comments, single_image_comments
from django.conf.urls.static import static

urlpatterns = [
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)