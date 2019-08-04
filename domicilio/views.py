from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView


class IndexDomicilio(CreateView):

    template_name = 'domicilio/index.html'

    def get(self, request, *args, **kwargs):


        return render(request, self.template_name,{})


class Domicilio(CreateView):

    template_name = 'domicilio/grid_list.html'

    def get(self, request, *args, **kwargs):


        return render(request, self.template_name,{})


class Menu(CreateView):

    template_name = 'domicilio/detail_page.html'

    def get(self, request, *args, **kwargs):


        return render(request, self.template_name,{})


class Cart(CreateView):

    template_name = 'domicilio/cart.html'

    def get(self, request, *args, **kwargs):


        return render(request, self.template_name,{})


class Pago(CreateView):

    template_name = 'domicilio/cart_2.html'

    def get(self, request, *args, **kwargs):


        return render(request, self.template_name,{})



class Confirmacion(CreateView):

    template_name = 'domicilio/cart_3.html'

    def get(self, request, *args, **kwargs):


        return render(request, self.template_name,{})