from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from comercios.models import Restaurante, TipoCocina
from django.db.models import Q
from django import http
import json
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from annoying.functions import get_object_or_None


class Index(CreateView):

    template_name = 'guia/index.html'

    def get(self, request, *args, **kwargs):

        restaurantes = Restaurante.objects.all()


        return render(request, self.template_name,{'restaurantes':restaurantes})



def filtrar(diccionario):

    restaurantes = Restaurante.objects.all()

    """filtrado por codigo postal"""
    try:
        print('filtro en cp')

        cp = diccionario['cp']
        restaurantes = restaurantes.filter(Q(codigo_postal__icontains=cp))

    except:
        pass

    """ Filtrado por tipo cocina """

    try:
        print('print en tipo de cocina')
        tipo_cocina = diccionario.getlist('tipo_cocina[]')
        if not tipo_cocina:
            restaurantes = restaurantes

        else:
            restaurantes = restaurantes.filter(tipo_cocina__in=tipo_cocina)

    except:
        pass

    """filtrado por tipo de dieta"""

    try:

        tipo_dieta = diccionario.getlist('tipo_dieta[]')

        if not tipo_dieta:
            restaurantes = restaurantes
        else:
            restaurantes = restaurantes.filter(tipo_dieta__in=tipo_dieta)


    except:
        pass


    """filtrado por recoger"""

    try:

        recoger = diccionario['recoger']
        if recoger == 'True':
            restaurantes = restaurantes.filter(recoger=True)

    except:
        pass


    """ordenador por mejor valorados"""
    try:

        mejor_valorados = diccionario['mejor_valorados']
        if mejor_valorados == 'True':
            restaurantes = restaurantes.order_by('-valoracion_total')

    except:
        pass

    try:

        gastos_de_envio = diccionario['gastos_de_envio']
        if gastos_de_envio == 'True':
            restaurantes = restaurantes.order_by('coste_resparto_cliente')


    except:
        pass


    try:

        envio_gratis = diccionario['envio_gratis']
        if envio_gratis == 'True':

            restaurantes_envio_gratis = []

            for r in restaurantes:
                if r.coste_resparto_cliente <= 0:
                    restaurantes_envio_gratis.append(r)

            restaurantes = restaurantes_envio_gratis

    except:
        pass


    try:

        destacado = diccionario['destacado']
        if destacado == 'True':
            restaurantes = restaurantes.order_by('-destacado')

    except:
        pass


    try:
        sin_gluten = diccionario['sin_gluten']

        if sin_gluten == 'True':
            restaurantes = restaurantes.filter(sin_gluten=True)

    except:
        pass



    return restaurantes


class Guia(ListView):
    model = Restaurante
    context_object_name = 'restaurantes'
    template_name = 'guia/map_listing.html'

    def get(self, request, *args, **kwargs):


        restaurantes = filtrar(request.GET)[:1]

        tipos_cocina = TipoCocina.objects.all().order_by('nombre_slug')

        categorias_cocina = []

        for tipo in tipos_cocina:

            restaurante_tipo = tipo.restaurante_set.all()
            categorias_cocina.append((tipo, restaurante_tipo.count()))



        paginator = Paginator(restaurantes, 1)
        page = request.GET.get('page', 1)


        #try:
         #   restaurantes=paginator.page(page)
        #except PageNotAnInteger:
         #   restaurantes=paginator.page(1)
        #except EmptyPage:
        #    restaurantes=paginator.page(paginator.num_pages)



        return render(request, self.template_name,{'restaurantes':restaurantes,
                                                   'categorias_cocina':categorias_cocina,
                                                   'page':page,
                                                   'paginator': paginator,
                                                   'tipos_cocina': tipos_cocina,
                                                   })


@csrf_exempt
def cargarMas(request):
    print('CARGAR MAS')
    try:
        paginaActual = request.POST['pg']

        restaurantes = filtrar(request.POST)

        paginator = Paginator(restaurantes, 1)
        page = paginator.page(paginaActual)


        print(restaurantes)



        html = render_to_string('guia/map_filtro_categorias.html', {'page': page,
                                                         'paginator': paginator,
                                                         'restaurantes':restaurantes
                                                         })

        response_data = {'result': 'ok', 'datos': html, 'end_index': page.end_index(),
                         'has_next': page.has_next()}
    except Exception as e:

        response_data = {'result': 'error', 'message': str(e)}

    return http.HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def filtro_categorias_comida_guia(request):

    #print('filtro_categorias_comida_guia')

    restaurantes = filtrar(request.GET)
    paginaActual = request.GET['pg']
    paginator = Paginator(restaurantes, 1)
    page = paginator.page(paginaActual)
    restaurantes = page.object_list

    print(restaurantes)


    try:

        html = render_to_string('guia/map_filtro_categorias.html', {'restaurantes': restaurantes,
                                                                    'page': page,
                                                                    'paginator': paginator,
                                                                   })
        response_data = {'result': 'ok', 'html': html}

    except Exception as e:
        print(e)

        response_data = {'result': 'error'}

    return http.HttpResponse(json.dumps(response_data), content_type="application/json")


class Detail(CreateView):

    template_name = 'guia/detail_page_2.html'

    def get(self, request, *args, **kwargs):

        restaurante = get_object_or_None(Restaurante, nombre_slug=self.kwargs['nombre_slug'])



        return render(request, self.template_name,{'restaurante':restaurante,
                                                   })


class prueba(CreateView):
    template_name = 'guia/index_8.html'

    def get(self, request, *args, **kwargs):
        restaurantes = Restaurante.objects.all()


        return render(request, self.template_name, {'restaurantes': restaurantes})