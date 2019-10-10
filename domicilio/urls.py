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


from domicilio import views

urlpatterns = [

    #url(r'^$', views.Index.as_view(), name='index'),
    #url(r'^$', views.Domicilio.as_view(), name='index_domicilio'),
    #url(r'^domicilio/', views.DomicilioList.as_view(), name='domicilio'),
    #url(r'^menu/', views.Menu.as_view(), name='menu'),
    #url(r'^carro/', views.Cart.as_view(), name='carro'),
    #url(r'^pago/', views.Pago.as_view(), name='pago'),
    #url(r'^confirmacion/', views.Confirmacion.as_view(), name='confirmacion'),


    path('', views.Domicilio.as_view(), name='index_domicilio'),
    path('restaurantes/', views.DomicilioList.as_view(), name='domicilio'),
    path('menu/<nombre_slug>', views.Menu.as_view(), name='menu'),
    path('carro/', views.Cart.as_view(), name='carro'),
    path('pago/', views.Pago.as_view(), name='pago'),
    path('confirmacion/', views.Confirmacion.as_view(), name='confirmacion'),

    url(r'^filtro_categorias_comida/$', views.filtro_categorias_comida, name='filtro_categorias_comida'),

    #path('hola', views.Index.as_view),



]
