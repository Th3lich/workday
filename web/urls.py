"""proyectolimpio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.urls import path, re_path

from web import views

urlpatterns = [

    url(r'^contacto/$', views.Contacto.as_view(), name='contacto'),
    url(r'^sobre-nosotros/$', views.Nosotros.as_view(), name='nosotros'),
    #url(r'^$', views.Index.as_view(), name='index'),
    #path('hola', views.Index.as_view),

]