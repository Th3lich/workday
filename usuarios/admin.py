from django.contrib import admin
from usuarios.models import Tokenregister, DatosExtraUser, Direccion, AdminRestaurante

admin.site.register(Tokenregister)
admin.site.register(DatosExtraUser)
admin.site.register(Direccion)
admin.site.register(AdminRestaurante)