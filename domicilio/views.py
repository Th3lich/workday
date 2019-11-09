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

from comercios.models import Restaurante, Ciudad, CategoriaProducto, TipoCocina, Valoracion
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
        #categoria_comida = TipoCocina.objects.all()
        form = BusquedaForm()

        try:

            cp = request.GET['cp']
            restaurantes_cp = restaurantes_cp.filter(Q(codigo_postal__icontains=cp))

        except:

            cp = []

        return render(request, self.template_name,{'restaurantes_cp': restaurantes_cp,
                                                    'form': form,
                                                   #'categoria_comida':categoria_comida,
                                                   'cp':cp,
                                                   })


@csrf_exempt
def filtro_categorias_comida(request):
    print('filtro_categorias_comida')


    restaurantes = Restaurante.objects.filter(domicilio=True)

    try:

        cp = request.GET['cp']
        restaurantes = restaurantes.filter(Q(codigo_postal__icontains=cp))

    except:
        restaurantes = Restaurante.objects.filter(domicilio=True)


    try:

        tipo_cocina = request.GET.getlist('tipo_cocina[]')
        if not tipo_cocina:
            restaurantes = restaurantes
        else:
            restaurantes = restaurantes.filter(tipo_cocina__in=tipo_cocina)


    except:
        pass

    try:

        tipo_dieta = request.GET.getlist('tipo_dieta[]')
        if not tipo_dieta:
            restaurantes = restaurantes
        else:
            restaurantes = restaurantes.filter(tipo_dieta__in=tipo_dieta)


    except:
        pass


    try:

        recoger = request.GET['recoger']
        if recoger == 'True':
            restaurantes = restaurantes.filter(recoger=True)

    except:
        pass

    try:

        mejor_valorados = request.GET['mejor_valorados']
        if mejor_valorados == 'True':
            restaurantes = restaurantes.order_by('-valoracion_total')


    except:
        pass

    try:

        gastos_de_envio = request.GET['gastos_de_envio']
        if gastos_de_envio == 'True':
            restaurantes = restaurantes.order_by('coste_resparto_cliente')


    except:
        pass

    try:

        envio_gratis = request.GET['envio_gratis']
        if envio_gratis == 'True':

            restaurantes_envio_gratis = []

            for r in restaurantes:
                if r.coste_resparto_cliente <= 0:
                    restaurantes_envio_gratis.append(r)


            restaurantes = restaurantes_envio_gratis


    except:
        pass

    try:

        destacado = request.GET['destacado']
        if destacado == 'True':
            restaurantes = restaurantes.order_by('-destacado')


    except:
        pass

    try:

        sin_gluten = request.GET['sin_gluten']

        if sin_gluten == 'True':
            restaurantes = restaurantes.filter(sin_gluten=True)

    except:
        pass


    try:

        html = render_to_string('domicilio/grid_list_filtro_categorias.html', {'restaurantes': restaurantes,
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



