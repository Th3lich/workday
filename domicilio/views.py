from django.db.models import Q
from django.shortcuts import render
import json
from django import http
from django.template.loader import render_to_string

# Create your views here.
from django.utils import html
from django.views.decorators.csrf import csrf_exempt
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

        restaurantes_cp = Restaurante.objects.filter(domicilio=True)
        categoria_comida = TipoCocina.objects.all()
        form = BusquedaForm()


        try:

            q = request.GET['cp']
            restaurantes_cp = restaurantes_cp.filter(Q(codigo_postal__icontains=q))

        except:
            q = []

        try:

            categoria = request.GET['categorias']
            restaurantes_cp = restaurantes_cp.filter(Q(tipo__categoriaproducto=categoria))


        except:
            pass


        return render(request, self.template_name,{'restaurantes_cp': restaurantes_cp,
                                                    'form': form,
                                                   'categoria_comida':categoria_comida,
                                                   'q':q,
                                                   })


@csrf_exempt
def filtro_categorias_comida(request):

    categorias = request.GET.getlist('categorias[]')
    restaurantes_cp = Restaurante.objects.filter(domicilio=True)

    try:

        q = request.GET['cp']
        restaurantes_cp = restaurantes_cp.filter(Q(codigo_postal__icontains=q))

    except:
        pass


    if not categorias:

        restaurantes_cp = restaurantes_cp
        try:
            recoger = request.GET['recoger']
            if recoger == 'True':
                restaurantes_cp = restaurantes_cp.filter(recoger=True)
            else:
                pass
        except:
            pass

    else:

        try:
            recoger = request.GET['recoger']
            if recoger == 'True':
                restaurantes_cp = restaurantes_cp.filter(tipo_cocina__in=categorias).filter(recoger=True)
                print('if')
                print(restaurantes_cp)
            else:
                restaurantes_cp = restaurantes_cp.filter(tipo_cocina__in=categorias)
                print('else')
                print(restaurantes_cp)

        except:
            restaurantes_cp = restaurantes_cp.filter(tipo_cocina__in=categorias)

    try:

        html = render_to_string('domicilio/grid_list_filtro_categorias.html', {'restaurantes_cp': restaurantes_cp,
                                                                               })
        response_data = {'result': 'ok', 'html': html}

    except Exception as e:
        print(e)

        response_data = {'result': 'error'}

    return http.HttpResponse(json.dumps(response_data), content_type="application/json")


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



