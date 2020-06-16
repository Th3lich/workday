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


class CreateProjectForm(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}),
                           required=True)
    estimated_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'placeholder': '00:00', 'class': 'form-control'}), required=False)


class CreateCenterForm(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}),
                           required=True)
    lat = forms.DecimalField(max_digits=10, widget=forms.TextInput(attrs={'placeholder': 'Latitud', 'class': 'form-control'}), required=True)
    lng = forms.DecimalField(max_digits=11,
                             widget=forms.TextInput(attrs={'placeholder': 'Longitud', 'class': 'form-control'}),
                             required=True)