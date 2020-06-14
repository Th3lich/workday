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






class RegisterUserForm(forms.Form):

    nif = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'NIF', 'class': 'form-control'}), required=True)
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}), required=True)
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Apellidos', 'class': 'form-control'}), required=True)
    email = forms.EmailField(max_length=120, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}), required=True)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'}))
    re_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Repetir Contraseña', 'class': 'form-control'}))