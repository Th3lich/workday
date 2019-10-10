#-*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe




# class RegistrationForm(forms.Form):
#     email = forms.EmailField()
#     username = forms.CharField(max_length=25, label="Nombre de usuario")
#     password1 = forms.CharField(min_length=6, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña...'}), label='Contraseña')
#     password2 = forms.CharField(min_length=6, widget=forms.PasswordInput(attrs={'placeholder': 'Repite Contraseña...'}),
#                                 label='Repite Contraseña')
#     protecion_de_datos = forms.BooleanField(required=True, label=mark_safe(
#         '<p>Más información sobre la<a style="color:red;" href="{% url "lpd" %}"> politica de privacidad.</a></p>'))
#
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if User.objects.filter(username=username).exists():
#             raise forms.ValidationError(u'El usuario "%s" ya existe.' % username)
#         return username
#
#
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError(u'El email "%s" ya existe.' % email)
#         return email
#
#
#     def clean_password2(self):
#         password1 = self.cleaned_data['password1']
#         password2 = self.cleaned_data['password2']
#         if password1 != password2:
#             raise forms.ValidationError(u'Las contraseñas no coinciden')
#         return password2
#
#
#     def clean_protecion_de_datos(self):
#         protecion_de_datos = self.cleaned_data['protecion_de_datos']
#         if protecion_de_datos != True:
#             raise forms.ValidationError(u'Debes leer y aceptar la política de privacidad.')
#         return protecion_de_datos
#
#
# class DatosExtraUserEditForm(forms.ModelForm):
#     error_css_class = 'alert alert-danger'
#
#     class Meta:
#         model = DatosExtraUser
#         exclude = {
#             'user',
#
#         }
#         labels = {'imagen': "Imagen de perfil",
#                   'imagenFondo': "Imagen de fondo",
#                   'titulo': "Titulo",
#                   'color_titulo': "Color titulo",
#                   'sobremi': "Sobre mi",
#                   'juego1': "Juego uno",
#                   'juego2': "Juego dos",
#                   'juego3': "Juego tres",
#                   'juego4': "Juego cuatro",
#                   'juego5': "Juego cinco",
#                   'juego6': "Juego seix",
#
#
#                  }
#
#         widgets = {
#
#         }
#
# class UserEditForm(forms.ModelForm):
#     error_css_class = 'alert alert-danger'
#
#     class Meta:
#         model = User
#         exclude = {
#
#         }
#
#         widgets = {
#
#         }
#
#
# class VotacionForm(forms.ModelForm):
#     error_css_class = 'alert alert-danger'
#
#     class Meta:
#         model = Votacion
#         exclude = {
#
#         }
#
#         widgets = {
#
#         }


class BusquedaForm(forms.Form):

       cp = forms.CharField(label='subject', max_length=5,
                                 widget=forms.TextInput(attrs={'class': "search-query",'placeholder': 'Introduzca su codigo postal'}))




