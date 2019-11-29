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


    """ filtrado por busqueda """
    try:
        q = diccionario['q']

        restaurantes = restaurantes.filter(Q(nombre__icontains=q)
                                     | Q(descripcion__icontains=q)
                                     | Q(referencia__icontains=q)
                                     | Q(referencia_raiz__icontains=q)
                                     | Q(material__icontains=q)
                                     )
    except:
        q = ""

    return restaurantes, q


class Guia(ListView):
    model = Restaurante
    paginate_by = 1
    context_object_name = 'restaurantes'
    template_name = 'guia/map_listing.html'

    def get(self, request, *args, **kwargs):

        restaurantes = Restaurante.objects.all()

        paginator =  Paginator(restaurantes, 1)
        page = request.GET.get('page',1)

        tipos_cocina = TipoCocina.objects.all().order_by('nombre_slug')

        categorias_cocina = []


        for tipo in tipos_cocina:

            restaurante_tipo = tipo.restaurante_set.all()
            categorias_cocina.append((tipo, restaurante_tipo.count()))


        try:
            restaurantes=paginator.page(page)
        except PageNotAnInteger:
            restaurantes=paginator.page(1)
        except EmptyPage:
            restaurantes=paginator.page(paginator.num_pages)

        print(restaurantes)

        return render(request, self.template_name,{'restaurantes':restaurantes,
                                                   'categorias_cocina':categorias_cocina
                                                   })


@csrf_exempt
def cargarMas(request):
    print('CARGAR MAS')
    try:
        paginaActual = request.POST['pg']
        print(paginaActual)


        restaurantes = Restaurante.objects.all()

        paginator = Paginator(restaurantes, 1)
        page = paginator.page(paginaActual)

        print(page)
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

    print('filtro_categorias_comida_guia')

    restaurantes = Restaurante.objects.filter()
    print(restaurantes)

    try:
        print('filtro en cp')

        cp = request.GET['cp']
        restaurantes = restaurantes.filter(Q(codigo_postal__icontains=cp))

    except:
        pass

    try:
        print('print en tipo de cocina')
        tipo_cocina = request.GET.getlist('tipo_cocina[]')
        if not tipo_cocina:
            restaurantes = restaurantes
        else:
            restaurantes = restaurantes.filter(tipo_cocina__in=tipo_cocina)

    except:
        pass


    try:
        print('tipo de dieta')
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

        html = render_to_string('guia/map_filtro_categorias.html', {'restaurantes': restaurantes,
                                                                               })
        response_data = {'result': 'ok', 'html': html}

    except Exception as e:
        print(e)

        response_data = {'result': 'error'}

    return http.HttpResponse(json.dumps(response_data), content_type="application/json")


class Detail(CreateView):

    template_name = 'guia/detail_page_2.html'

    def get(self, request, *args, **kwargs):


        return render(request, self.template_name,{})


class prueba(CreateView):
    template_name = 'guia/index_8.html'

    def get(self, request, *args, **kwargs):
        restaurantes = Restaurante.objects.all()


        return render(request, self.template_name, {'restaurantes': restaurantes})