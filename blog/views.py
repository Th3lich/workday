#-*- encoding: utf-8 -*-

from annoying.functions import get_object_or_None
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from blog.models import Entrada, Categoria

""" Vistas blog """

class Blog(CreateView):
    template_name = 'blog/blog.html'
    context_object_name = 'categoria'

    def get(self, request, *args, **kwargs):

        categorias = Categoria.objects.order_by('pk')
        # Filtro por get
        try:
            categoria = request.GET['categoria']
        except:
            categoria = None

        entradas = Entrada.objects.filter(categoria__nombre_slug=categoria).order_by('-pk') if categoria is not None else Entrada.objects.all().order_by('-pk')

        # Paginacion
        page = request.GET.get('page', 1)
        paginator = Paginator(entradas, 4)
        try:
            entradas = paginator.page(page)
        except PageNotAnInteger:
            entradas = paginator.page(1)
        except EmptyPage:
            entradas = paginator.page(paginator.num_pages)

        return render(request, self.template_name, {'entradas': entradas,
                                                    'categorias':categorias,
                                                    })

class EntradaView(CreateView):
    template_name = 'blog/blog-entrada.html'

    def get(self, request, *args, **kwargs):
        entrada = get_object_or_None(Entrada, titulo_slug=self.kwargs['entrada'])
        return render(request, self.template_name, {'entrada': entrada
                                                    })

""" Fin Vistas Blog """




class Blog2(CreateView):

    template_name = 'blog/blog_2.html'

    def get(self, request, *args, **kwargs):
        print('entro en prueba')


        return render(request, self.template_name,{})


class Blog3(CreateView):

    template_name = 'blog/blog.html'

    def get(self, request, *args, **kwargs):


        return render(request, self.template_name,{})