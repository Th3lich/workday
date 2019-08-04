# -*- encoding: utf-8 -*-

__author__ = 'brian'

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from usuarios import views_java

urlpatterns = [url(r'^login/$', views_java.login),
               url(r'^logout/$', views_java.logout),
               url(r'^get_perfil/$', views_java.get_perfil),
               url(r'^comprobar_token/$', views_java.comprobar_token),
               url(r'^cambiar_pass/$', views_java.cambiar_pass),
               ]
