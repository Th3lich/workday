# -*- encoding: utf-8 -*-

__author__ = 'brian'

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from usuarios import views_api

urlpatterns = [url(r'^login/$', views_api.login),
               url(r'^logout/$', views_api.logout),
               url(r'^get_perfil/$', views_api.get_perfil),
               url(r'^comprobar_token/$', views_api.comprobar_token),
               url(r'^cambiar_pass/$', views_api.cambiar_pass),
               ]
