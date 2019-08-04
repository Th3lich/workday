#-*- encoding: utf-8 -*-

from django.conf.urls import url

from blog import views

urlpatterns = [

     url(r'^$', views.Blog3.as_view(), name='blog'),
     url(r'^prueba/', views.Blog2.as_view(), name='blog2'),
     url(r'^(?P<categoria>[-\w]+)$', views.Blog.as_view(), name='blog_123'),
     url(r'^(?P<entrada>[-\w]+)$', views.EntradaView.as_view(), name='blog-entrada'),
]