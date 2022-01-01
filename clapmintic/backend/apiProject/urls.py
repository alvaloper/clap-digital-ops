"""apiProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from apiApp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    #path('ips/', views.IpsCreateView.as_view()),
    #path('ips/<int:pk>/', views.IpsDetailView.as_view()),
    #path('ips/<int:pk>/', views.IpsUpdateView.as_view()),
    #path('pruebatutor/', views.pruebaluisjose),
    
    
    path('ips/', views.IpsList.as_view()),
    path('ips/<int:pk>/', views.IpsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)