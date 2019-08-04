#-*- encoding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Categoria(models.Model):

    nombre = models.CharField(max_length=50, unique=True)
    nombre_slug = models.SlugField(unique=True, blank=True, editable=False)
    descripcion = models.CharField(max_length=150)

    def __unicode__(self):
        return u"%s" % self.nombre_slug

    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super(Categoria, self).save(*args, **kwargs)


class Entrada(models.Model):

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150, unique=True)
    titulo_slug = models.SlugField(max_length=150, unique=True, blank=True, editable=False)
    descripcion_corta = models.CharField(max_length=200, default="")
    descripcion_html = models.CharField(max_length=200, default="")
    keywords = models.CharField(max_length=200, default="")
    texto = RichTextUploadingField()
    fecha = models.DateTimeField(auto_now_add=True)
    publicacion = models.BooleanField(default=False)
    favorito = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='blog/', blank=True,null=True)
    imagen_web = models.CharField(max_length=512, null=True, blank=True)

    def __unicode__(self):
        return u"%s" % self.titulo_slug

    def save(self, *args, **kwargs):
        self.titulo_slug = slugify(self.titulo)
        super(Entrada, self).save(*args, **kwargs)