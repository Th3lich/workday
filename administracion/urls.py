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


    path('horarios', login_required(views.HorariosList.as_view()), name='horarios'),
    path('crear-horario', login_required(views.HorarioCreate.as_view()), name='horario_create'),
    path('editar-horario/<pk>', views.HorarioEdit.as_view(), name='horario_edit'),
    path('eliminar-horario/<pk>', views.HorarioDelete.as_view(), name='horario_delete'),


    path('horario-reparto', login_required(views.HorariosRepartoList.as_view()), name='horarios_reparto'),
    path('crear-horario-reparto', login_required(views.HorarioRepartoCreate.as_view()), name='horario_reparto_create'),
    path('editar-horario-reparto/<pk>', views.HorarioRepartoEdit.as_view(), name='horario_reparto_edit'),
    path('eliminar-horario-reparto/<pk>', views.HorarioRepartoDelete.as_view(), name='horario_reparto_delete'),


    path('cp', login_required(views.CpList.as_view()), name='cp'),
    path('crear-cp', login_required(views.CpCreate.as_view()), name='cp_create'),
    path('editar-cp/<pk>', views.CpEdit.as_view(), name='cp_edit'),
    path('eliminar-cp/<pk>', views.CpDelete.as_view(), name='cp_delete'),


    path('dia-festivo', login_required(views.FestivoList.as_view()), name='festivos'),
    path('crear-dia-festivo', login_required(views.FestivoCreate.as_view()), name='festivo_create'),
    path('editar-dia-festivo/<pk>', views.FestivoEdit.as_view(), name='festivo_edit'),
    path('eliminar-dia-festivo/<pk>', views.FestivoDelete.as_view(), name='festivo_delete'),


    # url(r'^editar-categoria/(?P<pk>\d+)$', login_required(views.CategoriaEdit.as_view()), name='categoria_edit'),
    # url(r'^eliminar-categoria/(?P<pk>\d+)$', login_required(views.CategoriaDelete.as_view()), name='categoria_delete'),
    # url(r'^nose-categoria/(?P<pk>\d+)$', login_required(views.CategoriaDelete.as_view()), name='delete'),

    #path('hola', views.Index.as_view),

]
