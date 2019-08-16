# -*- encoding: utf-8 -*-

# import floppyforms as forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from datetimewidget.widgets import TimeWidget, DateWidget, DateTimeWidget

from comercios.models import CategoriaProducto, Producto, Ingrediente


class ContrasenaForm(forms.Form):
    contrasena = forms.CharField(widget=forms.PasswordInput, label='Contraseña')


class CategoriaForm(forms.ModelForm):
    error_css_class = 'alert alert-danger'

    class Meta:
        model = CategoriaProducto
        exclude = {'restaurante'}


class ProductoForm(forms.ModelForm):
    error_css_class = 'alert alert-danger'

    class Meta:
        model = Producto
        exclude = {'categoria'}


class IngredienteForm(forms.ModelForm):
    error_css_class = 'alert alert-danger'

    class Meta:
        model = Ingrediente
        exclude = {'producto'}


# class NifForm(forms.Form):
#     nif = forms.CharField(label='Nif')
#
#
# class CrearEmpresaForm(forms.ModelForm):
#     error_css_class = 'alert alert-danger'
#
#     class Meta:
#         model = Empresa
#         exclude = {'creador'}
#
# class CrearTurnoForm(forms.ModelForm):
#     error_css_class = 'alert alert-danger'
#
#     class Meta:
#         model = Turno
#         exclude = {'trabajador'}
#
#
# class CrearCentroForm(forms.ModelForm):
#     error_css_class = 'alert alert-danger'
#
#     class Meta:
#         model = Centro
#         exclude = {
#             'trabajadores',
#             'empresa'
#         }
#
# class SubirDocumentoForm(forms.ModelForm):
#     error_css_class = 'alert alert-danger'
#
#     class Meta:
#         model = Documento
#         exclude ={
#             'trabajador'
#         }
#
# class ContratoForm(forms.ModelForm):
#     class Meta:
#         model = Contrato
#         exclude = {
#             'trabajador'
#         }
#
#         widgets = {
#             'fecha_inicio': DateTimeWidget(usel10n=True, bootstrap_version=3),
#             'fecha_fin': DateTimeWidget(usel10n=True, bootstrap_version=3)
#         }
#
