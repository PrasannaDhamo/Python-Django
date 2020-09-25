"""login_registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('lg', views.lg),
    path('reg', views.reg),
    path('registration/', views.registration),
    path('homepage/', views.home),
    path('update/', views.update),
    path('up', views.up),
    path('delete/', views.delete),
    path('dele', views.dele),
    path('admin/', admin.site.urls),
]
