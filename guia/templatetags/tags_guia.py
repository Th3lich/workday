# -*- coding: utf-8 -*-

from django import template
from django.db.models import Q
from comercios.models import CategoriaProducto, Producto, Ingrediente, Restaurante, TipoCocina, TipoDieta

register = template.Library()


@register.simple_tag(name='get_categoria_producto')
def get_categoria_producto(restaurante):
    categoria_producto = CategoriaProducto.objects.filter(restaurante__nombre_slug=restaurante.nombre_slug)

    return categoria_producto


@register.simple_tag(name='get_producto')
def get_producto(categoria_producto):
    producto = Producto.objects.filter(categoria__nombre_slug=categoria_producto.nombre_slug)

    return producto


@register.simple_tag(name='get_ingrediente')
def get_ingrediente(producto):
    ingrediente = Ingrediente.objects.filter(producto__nombre_slug=producto.nombre_slug)

    return ingrediente


@register.simple_tag(name='get_tipo_cocina')
def get_tipo_cocina(restaurantes, tipos_cocina):

    categorias_cocina = []

    for tipo in tipos_cocina:
        restaurantes = restaurantes.filter(Q(tipo_cocina=tipo))

        categorias_cocina.append((tipo,restaurantes.count()))


    return categorias_cocina



@register.simple_tag(name='get_tipo_dieta')
def get_tipo_dieta(restaurantes_cp):

    tipos_dieta = TipoDieta.objects.all().order_by('pk')

    categorias_dieta = []

    for dieta in tipos_dieta:
        restaurantes = restaurantes_cp.filter(Q(tipo_dieta=dieta))

        categorias_dieta.append((dieta,restaurantes.count()))


    return categorias_dieta


