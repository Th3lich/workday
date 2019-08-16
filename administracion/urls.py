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
from django.contrib.auth.decorators import login_required
from django.urls import include
from django.urls import path, re_path


from administracion import views

urlpatterns = [

    path('', login_required(views.Admin.as_view()), name='index_admin'),
    path('carta', login_required(views.CategoriasList.as_view()), name='categoria_productos'),
    path('crear-categoria', login_required(views.CategoriaCreate.as_view()), name='categoria_create'),
    path('editar-categoria/<pk>', views.CategoriaEdit.as_view(), name='categoria_edit'),
    path('eliminar-categoria-productos/<pk>', views.CategoriaDelete.as_view(), name='categoria_delete'),

    path('platos/<pk>', login_required(views.ProductosList.as_view()), name='productos'),
    path('crear-plato/<pk>', login_required(views.ProductoCreate.as_view()), name='producto_create'),
    path('editar-plato/<pk>', views.ProductoEdit.as_view(), name='producto_edit'),
    path('eliminar-plato/<pk>', views.ProductoDelete.as_view(), name='producto_delete'),


    path('ingrediente/<pk>', login_required(views.IngredientesList.as_view()), name='ingredientes'),
    path('crear-ingrediente/<pk>', login_required(views.IngredienteCreate.as_view()), name='ingrediente_create'),
    path('editar-ingrediente/<pk>', views.IngredienteEdit.as_view(), name='ingrediente_edit'),
    path('eliminar-ingrediente/<pk>', views.IngredienteDelete.as_view(), name='ingrediente_delete'),

    # url(r'^editar-categoria/(?P<pk>\d+)$', login_required(views.CategoriaEdit.as_view()), name='categoria_edit'),
    # url(r'^eliminar-categoria/(?P<pk>\d+)$', login_required(views.CategoriaDelete.as_view()), name='categoria_delete'),
    # url(r'^nose-categoria/(?P<pk>\d+)$', login_required(views.CategoriaDelete.as_view()), name='delete'),

    #path('hola', views.Index.as_view),

]
