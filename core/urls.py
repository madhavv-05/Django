"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from home.views import *
from vege.views import *
from accounts.views import*
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',receipe,name="vege"),
    path('receipe/',receipe,name="receipe"),
    path('delete-rec/<id>/',delete_rec,name="delete_rec"),
    path('update-rec/<id>/',update_rec,name="update_rec"),
    path('login/',login_page,name='login'),
    path('register/', register ,name='register'),
    
    path('logout/',logout_page,name='logout'),
    path('student/',get_students,name='get_students')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
