"""
URL configuration for Tutoring_center project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('api/', include('apps.comments.urls', namespace='api-comments')),
    path('api/', include('apps.disciplines.urls', namespace='api-disciplines')),
    path('api/', include('apps.users.urls', namespace='api-users')),
    path('api/', include('apps.contacts.urls', namespace='api-contacts')),
    path('api/', include('apps.documents.urls', namespace='api-documents')),
    path('api/', include('apps.notifications.urls', namespace='api-notifications')),
]
