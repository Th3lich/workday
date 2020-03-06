from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from comercios.models import Restaurante, Cp, Producto


class Codigo(models.Model):
    nombre = models.CharField(max_length=300)
    nombre_slug = models.SlugField(blank=True, editable=False)
    descripcion = models.CharField(max_length=300)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    valor = models.IntegerField(default=0)
    porcentaje = models.BooleanField(default=False)
    inicio = models.DateField()
    fin = models.DateField()
    aplicar_carrito = models.BooleanField(default=False)
    aplicar_envio = models.BooleanField(default=False)
    max_canjeo_total = models.IntegerField(blank=True, null=True)
    max_canjeo_user = models.IntegerField(blank=True, null=True)



    def __unicode__(self):
        return u"%s_%s" %(self.restaurante.nombre, self.nombre)

    def toJSONFavoritos(self):
        json = {'pk': self.pk,
                }
        return json


class Carrito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=300)
    precio_total = models.IntegerField()
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    codigo_descuento = models.ForeignKey(Codigo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=300)
    nombre_slug = models.SlugField(blank=True, editable=False)
    direccion = models.CharField(max_length=300)
    cp = models.ForeignKey(Cp, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s_%s" %(self.restaurante.nombre, self.user.last_name)

    def toJSONFavoritos(self):
        json = {'pk': self.pk,
                }
        return json


class ProductoCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.IntegerField()

    def __unicode__(self):
        return u"%s_%s" %(self.carrito.nombre, self.producto.nombre)

    def toJSONFavoritos(self):
        json = {'pk': self.pk,
                }
        return json


class IngredienteCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto_carrito = models.ForeignKey(ProductoCarrito, on_delete=models.CASCADE)
    precio = models.IntegerField()

    def __unicode__(self):
        return u"%s_%s" %(self.carrito.nombre, self.producto_carrito.nombre)

    def toJSONFavoritos(self):
        json = {'pk': self.pk,
                }
        return json