from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from annoying.functions import get_object_or_None
from django.http import HttpResponseRedirect

from administracion import forms
from administracion.forms import CategoriaForm, ContrasenaForm, ProductoForm, IngredienteForm
from comercios.models import Restaurante, CategoriaProducto, Producto, Ingrediente
from usuarios.models import AdminRestaurante
from django.urls import reverse

class Admin(CreateView):

    template_name = 'base.html'

    def get(self, request, *args, **kwargs):



        return render(request, self.template_name,{})


class CategoriasList(CreateView):

    template_name = 'categoria.html'

    def get(self, request, *args, **kwargs):

        trabajador = get_object_or_None(AdminRestaurante, user=request.user)
        restaurante = get_object_or_None(Restaurante,pk= trabajador.restaurante.pk)
        categoria = CategoriaProducto.objects.filter(restaurante=restaurante)

        return render(request, self.template_name,{'trabajador':trabajador,
                                                   'restaurante':restaurante,
                                                   'categoria':categoria,
                                                   })


class CategoriaCreate(CreateView):
    template_name = 'categoria_create.html'
    form_class = CategoriaForm

    def get(self, request, *args, **kwargs):
        form = CategoriaForm()
        trabajador = get_object_or_None(AdminRestaurante, user=request.user)
        restaurante = get_object_or_None(Restaurante, pk=trabajador.restaurante.pk)
        return render(request, self.template_name, {'form': form, 'restaurante':restaurante})

    def post(self, request, *args, **kwargs):
        form = CategoriaForm(request.POST)
        trabajador = get_object_or_None(AdminRestaurante, user=request.user)
        restaurante = get_object_or_None(Restaurante, pk=trabajador.restaurante.pk)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.restaurante = restaurante
            categoria.save()
            return HttpResponseRedirect(reverse('categoria_productos'))
        else:
            return render(request, self.template_name, {'form': form, 'restaurante':restaurante})



class CategoriaEdit(CreateView):
    template_name = 'categoria_edit.html'
    form_class = CategoriaForm

    def get(self, request, *args, **kwargs):
        categoria = get_object_or_None(CategoriaProducto, pk=self.kwargs['pk'])
        form = CategoriaForm(instance=categoria)

        return render(request, self.template_name, {'form': form, 'categoria':categoria})

    def post(self, request, *args, **kwargs):
        categoria = get_object_or_None(CategoriaProducto, pk=self.kwargs['pk'])
        form = self.form_class(request.POST, request.FILES, instance=categoria)

        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.restaurante = categoria.restaurante
            categoria.save()
            return HttpResponseRedirect(reverse('categoria_productos'))
        else:

            return render(request, self.template_name, {'form': form, 'categoria':categoria})


class CategoriaDelete(CreateView):
    template_name = 'categoria_delete.html'
    form_class = ContrasenaForm

    def get(self, request, *args, **kwargs):
        categoria = get_object_or_None(CategoriaProducto, pk=self.kwargs['pk'])
        print(categoria)
        form = self.form_class(initial=self.initial)
        print('hola hola')
        return render(request, self.template_name, {'form': form, 'categoria': categoria})

    def post(self, request, *args, **kwargs):
        print('holahola')
        categoria = get_object_or_None(CategoriaProducto, pk=self.kwargs['pk'])
        print(categoria)
        form = self.form_class(request.POST)
        password = form['contrasena'].value()
        correcto = request.user.check_password(password)
        if correcto:
            categoria.delete()
            return HttpResponseRedirect(reverse('categoria_productos'))
        else:
            return render(request, self.template_name, {'form': form, 'categoria': categoria})



class ProductosList(CreateView):
    template_name = 'productos.html'

    def get(self, request, *args, **kwargs):
        categoria = get_object_or_None(CategoriaProducto, pk=self.kwargs['pk'])
        productos = Producto.objects.filter(categoria=categoria)

        return render(request, self.template_name, {'categoria':categoria,
                                                    'productos':productos})



class ProductoCreate(CreateView):
    template_name = 'producto_create.html'
    form_class = ProductoForm

    def get(self, request, *args, **kwargs):
        form = ProductoForm()
        categoria = get_object_or_None(CategoriaProducto, pk=self.kwargs['pk'])
        return render(request, self.template_name, {'form': form, 'categoria':categoria})

    def post(self, request, *args, **kwargs):
        form = ProductoForm(request.POST)
        categoria = get_object_or_None(CategoriaProducto, pk=self.kwargs['pk'])
        if form.is_valid():
            producto = form.save(commit=False)
            producto.categoria = categoria
            producto.save()
            return HttpResponseRedirect(reverse('productos', args=[categoria.pk]))
        else:
            return render(request, self.template_name, {'form': form, 'categoria':categoria})



class ProductoEdit(CreateView):
    template_name = 'producto_edit.html'
    form_class = ProductoForm

    def get(self, request, *args, **kwargs):
        producto = get_object_or_None(Producto, pk=self.kwargs['pk'])
        form = ProductoForm(instance=producto)

        return render(request, self.template_name, {'form': form, 'producto':producto})

    def post(self, request, *args, **kwargs):
        producto = get_object_or_None(Producto, pk=self.kwargs['pk'])
        form = self.form_class(request.POST, request.FILES, instance=producto)

        if form.is_valid():
            producto = form.save(commit=False)
            producto.categoria = producto.categoria
            producto.save()
            return HttpResponseRedirect(reverse('productos', args=[producto.categoria.pk]))
        else:

            return render(request, self.template_name, {'form': form, 'producto':producto})


class ProductoDelete(CreateView):
    template_name = 'producto_delete.html'
    form_class = ContrasenaForm

    def get(self, request, *args, **kwargs):
        producto = get_object_or_None(Producto, pk=self.kwargs['pk'])
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'producto': producto})

    def post(self, request, *args, **kwargs):
        producto = get_object_or_None(Producto, pk=self.kwargs['pk'])
        form = self.form_class(request.POST)
        password = form['contrasena'].value()
        correcto = request.user.check_password(password)
        if correcto:
            producto.delete()
            return HttpResponseRedirect(reverse('productos', args=[producto.categoria.pk]))
        else:
            return render(request, self.template_name, {'form': form, 'producto': producto})



class IngredientesList(CreateView):
    template_name = 'ingredientes.html'

    def get(self, request, *args, **kwargs):
        producto = get_object_or_None(Producto, pk=self.kwargs['pk'])
        ingredientes = Ingrediente.objects.filter(producto=producto)

        return render(request, self.template_name, {'ingredientes':ingredientes,
                                                    'producto':producto})



class IngredienteCreate(CreateView):
    template_name = 'ingrediente_create.html'
    form_class = IngredienteForm

    def get(self, request, *args, **kwargs):
        form = IngredienteForm()
        producto = get_object_or_None(Producto, pk=self.kwargs['pk'])
        return render(request, self.template_name, {'form': form, 'producto':producto})

    def post(self, request, *args, **kwargs):
        form = IngredienteForm(request.POST)
        producto = get_object_or_None(Producto, pk=self.kwargs['pk'])
        if form.is_valid():
            ingrediente = form.save(commit=False)
            ingrediente.producto = producto
            ingrediente.save()
            return HttpResponseRedirect(reverse('ingredientes', args=[producto.pk]))
        else:
            return render(request, self.template_name, {'form': form, 'producto':producto})



class IngredienteEdit(CreateView):
    template_name = 'ingrediente_edit.html'
    form_class = IngredienteForm

    def get(self, request, *args, **kwargs):
        ingrediente = get_object_or_None(Ingrediente, pk=self.kwargs['pk'])
        form = IngredienteForm(instance=ingrediente)

        return render(request, self.template_name, {'form': form, 'ingrediente':ingrediente})

    def post(self, request, *args, **kwargs):
        ingrediente = get_object_or_None(Ingrediente, pk=self.kwargs['pk'])
        form = self.form_class(request.POST, request.FILES, instance=ingrediente)

        if form.is_valid():
            ingrediente = form.save(commit=False)
            ingrediente.producto = ingrediente.producto
            ingrediente.save()
            return HttpResponseRedirect(reverse('ingredientes', args=[ingrediente.producto.pk]))
        else:

            return render(request, self.template_name, {'form': form, 'producto':producto})


class IngredienteDelete(CreateView):
    template_name = 'ingrediente_delete.html'
    form_class = ContrasenaForm

    def get(self, request, *args, **kwargs):
        ingrediente = get_object_or_None(Ingrediente, pk=self.kwargs['pk'])
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'ingrediente': ingrediente})

    def post(self, request, *args, **kwargs):
        ingrediente = get_object_or_None(Ingrediente, pk=self.kwargs['pk'])
        form = self.form_class(request.POST)
        password = form['contrasena'].value()
        correcto = request.user.check_password(password)
        if correcto:
            ingrediente.delete()
            return HttpResponseRedirect(reverse('ingredientes', args=[ingrediente.producto.pk]))
        else:
            return render(request, self.template_name, {'form': form, 'ingrediente': ingrediente})



