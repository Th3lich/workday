from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView


class Contacto(CreateView):

    template_name = 'web/contacts.html'

    def get(self, request, *args, **kwargs):


        return render(request, self.template_name,{})


class Nosotros(CreateView):

    template_name = 'web/about.html'

    def get(self, request, *args, **kwargs):


        return render(request, self.template_name,{})