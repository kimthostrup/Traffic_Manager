"""shaping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from django.views.generic.base import TemplateView
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^getDevIp', views.ControlingInfo.as_view()),
    re_path(r'^$', TemplateView.as_view(template_name='index.html')),
    re_path(r'^shaping/', views.Shaping.as_view()),
    re_path(r'^CheckDevStatus', views.CheckDevStatus.as_view()),
    re_path(r'profile', views.Profile.as_view()),
    #re_path(r'action/(?P<slug>((1?[1-9]?\d|[1-2][0-4]\d|25[0-5])\.){3}(1?[1-9]?\d|[1-2][0-4]\d|25[0-5]))/', views.Action.as_view()),
]
