# -*- coding: utf-8 -*-

from django import template
from django.db.models import Q
from comercios.models import CategoriaProducto, Producto, Ingrediente, Restaurante, TipoCocina

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
def get_tipo_cocina(restaurantes_cp):

    tipos_cocina = TipoCocina.objects.all()

    categorias = []

    for tipo in tipos_cocina:
        restaurantes = restaurantes_cp.filter(Q(tipo_cocina=tipo))

        categorias.append((tipo.nombre,restaurantes.count()))


    return categorias

