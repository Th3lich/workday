from django.contrib import admin

# Register your models here.
from comercios.models import Provincia, Ciudad, TipoDieta, Restaurante, Tienda, Galeria, Valoracion, ValoracionAbierta, \
    Favoritos, Alergenos, CategoriaProducto, Producto, Ingrediente, Horario, Cp, HorarioReparto, DiaFestivo, TipoCocina


admin.site.register(Provincia)
admin.site.register(Ciudad)
admin.site.register(TipoDieta)
admin.site.register(Restaurante)
admin.site.register(Tienda)
admin.site.register(Galeria)
admin.site.register(Valoracion)
admin.site.register(ValoracionAbierta)
admin.site.register(Favoritos)
admin.site.register(Alergenos)
admin.site.register(CategoriaProducto)
admin.site.register(Producto)
admin.site.register(Ingrediente)
admin.site.register(Horario)
admin.site.register(Cp)
admin.site.register(HorarioReparto)
admin.site.register(DiaFestivo)
admin.site.register(TipoCocina)
