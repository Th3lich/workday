#-*- encoding: utf-8 -*-

from django import forms


class EditUserForm(forms.Form):
    photo = forms.ImageField(required=False)
    nif = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'NIF', 'class': 'form-control'}), required=True)
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}), required=True)
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Apellidos', 'class': 'form-control'}), required=True)
    email = forms.EmailField(max_length=120, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}), required=True)
    address = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'placeholder': 'Dirección', 'class': 'form-control'}), required=False)
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Teléfono', 'class': 'form-control'}), required=False)






# class UsuarioForm(UserCreationForm):
#     error_css_class = 'alert alert-danger'
#     required_css_class = 'required'
#
#     nombre=forms.CharField(required=True)
#     apellidos=forms.CharField(required=False)
#     email = forms.EmailField(required=False)
#     username = forms.CharField()
#     admin = forms.BooleanField(required=False)
#
#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         password = self.cleaned_data['password1']
#         user.set_password(password)
#         user.first_name= self.cleaned_data['nombre']
#         user.last_name= self.cleaned_data['apellidos']
#         user.email= self.cleaned_data['email']
#         user.is_staff= self.cleaned_data['admin']
#         if commit:
#             user.save()
#         return user
#
#     class Meta:
#         model = User
#         exclude = {
#
#         }
#         fields ={
#             "username",
#             "email",
#             "password1",
#             "password2"
#         }
#
#         widgets = {
#         }
#
#
# class UsuarioEditForm(forms.Form):
#     username = forms.CharField()
#     nombre = forms.CharField(required=False)
#     apellidos = forms.CharField(required=False)
#     email = forms.EmailField(required=False)
#     admin = forms.BooleanField(required=False)
#
#     def save(self, *args, **kwargs):
#         self.usuario.username = self.cleaned_data['username']
#         self.usuario.first_name = self.cleaned_data['nombre']
#         self.usuario.last_name = self.cleaned_data['apellidos']
#         self.usuario.email = self.cleaned_data['email']
#         self.usuario.is_staff = self.cleaned_data['admin']
#         self.usuario.save()
#         return self.usuario
#
#     def __init__(self, *args, **kwargs):
#         self.usuario = kwargs.pop('usuario')
#         super(UsuarioEditForm, self).__init__(*args, **kwargs)
#         self.fields['username'].initial = self.usuario.username
#         self.fields['nombre'].initial = self.usuario.first_name
#         self.fields['apellidos'].initial = self.usuario.last_name
#         self.fields['email'].initial = self.usuario.email
#         self.fields['admin'].initial = self.usuario.is_staff
#
#
# class CambiarContrasenaForm(forms.Form):
#     antigua = forms.CharField(widget=forms.PasswordInput, label='Contraseña Antigua')
#     nueva = forms.CharField(widget=forms.PasswordInput, label='Contraseña Nueva')
#     renueva = forms.CharField(widget=forms.PasswordInput, label='Repetir Contraseña Nueva')
#
#
# class ContrasenaForm(forms.Form):
#     contrasena = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
#
#
# class Login(forms.Form):
#     username = forms.CharField(required=True)
#     password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
#
#
#
# class RecuperarContrasenaFormMail(forms.Form):
#         nueva = forms.CharField(widget=forms.PasswordInput, label='Contraseña Nueva')
#         renueva = forms.CharField(widget=forms.PasswordInput, label='Repetir Contraseña Nueva')
#
# class RecuperarContrasenaForm(forms.Form):
#         email = forms.EmailField()
#
#
# class BusquedaForm(forms.Form):
#     modelo = forms.CharField(label='modelo', required=False,
#                              widget=forms.TextInput(attrs={'placeholder': 'Ciudad'}))
#     marca = forms.CharField(label='marca', required=False,
#                             widget=forms.TextInput(attrs={'placeholder': 'Nombre o Email'}))
#     quiere_revision = forms.BooleanField(label='publicidad', required=False,
#                                          widget=forms.CheckboxInput(attrs={'placeholder': 'Publicidad'}))