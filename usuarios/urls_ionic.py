# -*- encoding: utf-8 -*-

__author__ = 'ruben'

from django.conf.urls import url
from usuarios import views_ionic as usuarios_ionic_views
from django.contrib.auth.decorators import login_required

urlpatterns = [url(r'^login/$', usuarios_ionic_views.login),
               url(r'^logout/$', usuarios_ionic_views.logout),
               #url(r'^get_usuarios/$', usuarios_ionic_views.get_usuarios),
               url(r'^get_perfil/$', usuarios_ionic_views.get_perfil),
               url(r'^cambiar_datos/$', usuarios_ionic_views.cambiar_datos),
               url(r'^comprobar_token/$', usuarios_ionic_views.comprobar_token),
               url(r'^cambiar_pass/$', usuarios_ionic_views.cambiar_pass),
               url(r'^registrar_usuario/$', usuarios_ionic_views.registrar_usuario),
               url(r'^registrar_usuario_facebook_google/$', usuarios_ionic_views.registrar_usuario_facebook_google)
               ]
