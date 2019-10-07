from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from annoying.functions import get_object_or_None

from comercios.models import Restaurante, Ciudad, CategoriaProducto, TipoCocina
from domicilio.forms import BusquedaForm
from django.http import HttpResponseRedirect
from django.urls import reverse


class Domicilio(CreateView):

    template_name = 'domicilio/domicilio.html'

    def get(self, request, *args, **kwargs):

        form = BusquedaForm()

        restaurantes = Restaurante.objects.filter(domicilio=True, destacado=True)

        return render(request, self.template_name, {'restaurantes':restaurantes,
                                                    'form':form
                                                    })


class DomicilioList(CreateView):

    template_name = 'domicilio/grid_list.html'

    def get(self, request, *args, **kwargs):

        restaurantes_cp = Restaurante.objects.all()
        categoria_comida = TipoCocina.objects.all()
        tipo_cocina = []
        form = BusquedaForm()

        try:
            q = request.GET['cp']
            restaurantes_cp = restaurantes_cp.filter(Q(codigo_postal__icontains=q))

            tipos_cocina = TipoCocina.objects.all()

            for tipo in tipos_cocina:
                restaurantes = restaurantes_cp.filter(Q(tipo_cocina=tipo)).count()


        except:
            pass

        #reques.GET.getlist()



        return render(request, self.template_name,{'restaurantes_cp': restaurantes_cp,
                                                    'form': form,
                                                   'categoria_comida':categoria_comida,
                                                   'tipo_cocina':tipo_cocina
                                                   })


class Menu(CreateView):

    template_name = 'domicilio/detail_page.html'

    def get(self, request, *args, **kwargs):

        restaurante = get_object_or_None(Restaurante, nombre_slug=self.kwargs['nombre_slug'])

        categoria_productos = CategoriaProducto.objects.filter(restaurante__nombre_slug=restaurante.nombre_slug)


        print(restaurante)

        for c in categoria_productos:
            print(c.nombre)


        return render(request, self.template_name,{'restaurante':restaurante,
                                                   })


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