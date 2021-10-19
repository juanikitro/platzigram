"""platzigram URL Configuration module"""
# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('', include(('posts.urls', 'posts'), namespace = 'posts')),

    path('', include(('users.urls', 'users'), namespace = 'users')),

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
