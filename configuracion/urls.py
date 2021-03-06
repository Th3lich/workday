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
from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView

from ckeditor_uploader import views as vistas_ckeditor

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),
    url(r'^', include('landing.urls')),
    url(r'^administration/', include('administration.urls')),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),

    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    #url(r'^upload/', include(vistas_ckeditor.upload), name='ckeditor_upload'),
    #url(r'^browse/', include(vistas_ckeditor.browse), name='ckeditor_browse'),

]
