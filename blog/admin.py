#-*- encoding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from blog.models import Categoria, Entrada

admin.site.register(Categoria)
admin.site.register(Entrada)