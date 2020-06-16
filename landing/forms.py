from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}), required=True)
    subject = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Asunto', 'class': 'form-control'}))
    email = forms.EmailField(max_length=256, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Mensaje', 'class': 'form-control'}), required=True)