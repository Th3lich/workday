#-*- encoding: utf-8 -*-

from django import forms


class EditCompanyForm(forms.Form):

    photo = forms.ImageField(required=False)
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}),
                           required=True)
    cif = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'CIF', 'class': 'form-control'}), required=True)


class AddEmployeeForm(forms.Form):
    email = forms.EmailField(max_length=120,
                             widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
                             required=True)


class CreateCenterForm(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}),
                           required=True)
    addresss = forms.CharField(max_length=80,
                           widget=forms.TextInput(attrs={'placeholder': 'Dirección', 'class': 'form-control'}),
                           required=True)