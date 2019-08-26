from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from annoying.functions import get_object_or_None
from django.http import HttpResponseRedirect

from administracion import forms
from administracion.forms import CategoriaForm, ContrasenaForm, ProductoForm, IngredienteForm, HorarioForm, \
    HorarioRepartoForm, CpForm, FestivoForm
from comercios.models import Restaurante, CategoriaProducto, Producto, Ingrediente, Horario, HorarioReparto, Cp, \
    DiaFestivo
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



class HorariosList(CreateView):

    template_name = 'horarios.html'

    def get(self, request, *args, **kwargs):

        trabajador = get_object_or_None(AdminRestaurante, user=request.user)
        restaurante = get_object_or_None(Restaurante,pk= trabajador.restaurante.pk)
        horario = Horario.objects.filter(restaurante=restaurante)

        return render(request, self.template_name,{'horario':horario})


class HorarioCreate(CreateView):
    template_name = 'horario_create.html'
    form_class = HorarioForm

    def get(self, request, *args, **kwargs):
        form = HorarioForm()
        trabajador = get_object_or_None(AdminRestaurante, user=request.user)
        restaurante = get_object_or_None(Restaurante, pk=trabajador.restaurante.pk)
        return render(request, self.template_name, {'form': form, 'restaurante':restaurante})

    def post(self, request, *args, **kwargs):
        form = HorarioForm(request.POST)
        trabajador = get_object_or_None(AdminRestaurante, user=request.user)
        restaurante = get_object_or_None(Restaurante, pk=trabajador.restaurante.pk)
        if form.is_valid():
            horario = form.save(commit=False)
            horario.restaurante = restaurante
            horario.save()
            return HttpResponseRedirect(reverse('horarios'))
        else:
            return render(request, self.template_name, {'form': form, 'restaurante':restaurante})



class HorarioEdit(CreateView):
    template_name = 'horario_edit.html'
    form_class = HorarioForm

    def get(self, request, *args, **kwargs):
        horario = get_object_or_None(Horario, pk=self.kwargs['pk'])
        form = HorarioForm(instance=horario)

        return render(request, self.template_name, {'form': form, 'horario':horario})

    def post(self, request, *args, **kwargs):
        horario = get_object_or_None(Horario, pk=self.kwargs['pk'])
        form = self.form_class(request.POST, request.FILES, instance=horario)

        if form.is_valid():
            horario = form.save(commit=False)
            horario.restaurante = horario.restaurante
            horario.save()
            return HttpResponseRedirect(reverse('horarios'))
        else:

            return render(request, self.template_name, {'form': form, 'horario':horario})


class HorarioDelete(CreateView):
    template_name = 'horario_delete.html'
    form_class = ContrasenaForm

    def get(self, request, *args, **kwargs):
        horario = get_object_or_None(Horario, pk=self.kwargs['pk'])
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'horario': horario})

    def post(self, request, *args, **kwargs):
        horario = get_object_or_None(Horario, pk=self.kwargs['pk'])
        form = self.form_class(request.POST)
        password = form['contrasena'].value()
        correcto = request.user.check_password(password)
        if correcto:
            horario.delete()
            return HttpResponseRedirect(reverse('horarios'))
        else:
            return render(request, self.template_name, {'form': form, 'horario': horario})



class HorariosRepartoList(CreateView):

    template_name = 'horarios_reparto.html'

    def get(self, request, *args, **kwargs):

        trabajador = get_object_or_None(AdminRestaurante, user=request.user)
        restaurante = get_object_or_None(Restaurante,pk= trabajador.restaurante.pk)
        horario_reparto = HorarioReparto.objects.filter(restaurante=restaurante)

        return render(request, self.template_name,{'horario_reparto':horario_reparto})


class HorarioRepartoCreate(CreateView):
    template_name = 'horario_reparto_create.html'
    form_class = HorarioRepartoForm

    def get(self, request, *args, **kwargs):
        form = HorarioRepartoForm()
        trabajador = get_object_or_None(AdminRestaurante, user=request.user)
        restaurante = get_object_or_None(Restaurante, pk=trabajador.restaurante.pk)
        return render(request, self.template_name, {'form': form, 'restaurante':restaurante})

    def post(self, request, *args, **kwargs):
        form = HorarioRepartoForm(request.POST)
        trabajador = get_object_or_None(AdminRestaurante, user=request.user)
        restaurante = get_object_or_None(Restaurante, pk=trabajador.restaurante.pk)
        if form.is_valid():
            horario_reparto = form.save(commit=False)
            horario_reparto.restaurante = restaurante
            horario_reparto.save()
            return HttpResponseRedirect(reverse('horarios_reparto'))
        else:
            return render(request, self.template_name, {'form': form, 'restaurante':restaurante})



class HorarioRepartoEdit(CreateView):
    template_name = 'horario_reparto_edit.html'
    form_class = HorarioRepartoForm

    def get(self, request, *args, **kwargs):
        horario_reparto = get_object_or_None(HorarioReparto, pk=self.kwargs['pk'])
        form = HorarioRepartoForm(instance=horario_reparto)

        return render(request, self.template_name, {'form': form, 'horario_reparto':horario_reparto})

    def post(self, request, *args, **kwargs):
        horario_reparto = get_object_or_None(HorarioReparto, pk=self.kwargs['pk'])
        form = self.form_class(request.POST, request.FILES, instance=horario_reparto)

        if form.is_valid():
            horario_reparto = form.save(commit=False)
            horario_reparto.restaurante = horario_reparto.restaurante
            horario_reparto.save()
            return HttpResponseRedirect(reverse('horarios'))
        else:

            return render(request, self.template_name, {'form': form, 'horario_reparto':horario_reparto})


class HorarioRepartoDelete(CreateView):
    template_name = 'horario_reparto_delete.html'
    form_class = ContrasenaForm

    def get(self, request, *args, **kwargs):
        horario_reparto = get_object_or_None(HorarioReparto, pk=self.kwargs['pk'])
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'horario_reparto': horario_reparto})

    def post(self, request, *args, **kwargs):
        horario_reparto = get_object_or_None(HorarioReparto, pk=self.kwargs['pk'])
        form = self.form_class(request.POST)
        password = form['contrasena'].value()
        correcto = request.user.check_password(password)
        if correcto:
            horario_reparto.delete()
            return HttpResponseRedirect(reverse('horarios_reparto'))
        else:
            return render(request, self.template_name, {'form': form, 'horario_reparto': horario_reparto})


class CpList(CreateView):

    template_name = 'cp.html'

    def get(self, request, *args, **kwargs):

        trabajador = get_object_or_None(AdminRestaurante, user=request.user)
        restaurante = get_object_or_None(Restaurante,pk= trabajador.restaurante.pk)
        cp = Cp.objects.filter(restaurante=restaurante)

        return render(request, self.template_name,{'cp':cp})


class CpCreate(CreateView):
    template_name = 'cp_create.html'
    form_class = CpForm

    def get(self, request, *args, **kwargs):
        form = CpForm()
        trabajador = get_object_or_None(AdminRestaurante, user=request.user)
        restaurante = get_object_or_None(Restaurante, pk=trabajador.restaurante.pk)
        return render(request, self.template_name, {'form': form, 'restaurante':restaurante})

    def post(self, request, *args, **kwargs):
        form = CpForm(request.POST)
        trabajador = get_object_or_None(AdminRestaurante, user=request.user)
        restaurante = get_object_or_None(Restaurante, pk=trabajador.restaurante.pk)
        if form.is_valid():
            cp = form.save(commit=False)
            cp.restaurante = restaurante
            cp.save()
            return HttpResponseRedirect(reverse('cp'))
        else:
            return render(request, self.template_name, {'form': form, 'restaurante':restaurante})


class CpEdit(CreateView):
    template_name = 'cp_edit.html'
    form_class = CpForm

    def get(self, request, *args, **kwargs):
        cp = get_object_or_None(Cp, pk=self.kwargs['pk'])
        form = CpForm(instance=cp)

        return render(request, self.template_name, {'form': form, 'cp':cp})

    def post(self, request, *args, **kwargs):
        cp = get_object_or_None(Cp, pk=self.kwargs['pk'])
        form = self.form_class(request.POST, request.FILES, instance=cp)

        if form.is_valid():
            cp = form.save(commit=False)
            cp.restaurante = cp.restaurante
            cp.save()
            return HttpResponseRedirect(reverse('cp'))
        else:

            return render(request, self.template_name, {'form': form, 'cp':cp})


class CpDelete(CreateView):
    template_name = 'cp_delete.html'
    form_class = ContrasenaForm

    def get(self, request, *args, **kwargs):
        cp = get_object_or_None(Cp, pk=self.kwargs['pk'])
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'cp': cp})

    def post(self, request, *args, **kwargs):
        cp = get_object_or_None(Cp, pk=self.kwargs['pk'])
        form = self.form_class(request.POST)
        password = form['contrasena'].value()
        correcto = request.user.check_password(password)
        if correcto:
            cp.delete()
            return HttpResponseRedirect(reverse('cp'))
        else:
            return render(request, self.template_name, {'form': form, 'cp': cp})


class FestivoList(CreateView):

    template_name = 'festivo.html'

    def get(self, request, *args, **kwargs):

        trabajador = get_object_or_None(AdminRestaurante, user=request.user)
        restaurante = get_object_or_None(Restaurante,pk= trabajador.restaurante.pk)
        festivo = DiaFestivo.objects.filter(restaurante=restaurante)

        return render(request, self.template_name,{'festivo':festivo})


class FestivoCreate(CreateView):
    template_name = 'festivo_create.html'
    form_class = FestivoForm

    def get(self, request, *args, **kwargs):
        form = FestivoForm()
        trabajador = get_object_or_None(AdminRestaurante, user=request.user)
        restaurante = get_object_or_None(Restaurante, pk=trabajador.restaurante.pk)
        return render(request, self.template_name, {'form': form, 'restaurante':restaurante})

    def post(self, request, *args, **kwargs):
        form = FestivoForm(request.POST)
        trabajador = get_object_or_None(AdminRestaurante, user=request.user)
        restaurante = get_object_or_None(Restaurante, pk=trabajador.restaurante.pk)
        if form.is_valid():
            festivo = form.save(commit=False)
            festivo.restaurante = restaurante
            festivo.save()
            return HttpResponseRedirect(reverse('festivos'))
        else:
            return render(request, self.template_name, {'form': form, 'restaurante':restaurante})


class FestivoEdit(CreateView):
    template_name = 'festivo_edit.html'
    form_class = FestivoForm

    def get(self, request, *args, **kwargs):
        festivo = get_object_or_None(DiaFestivo, pk=self.kwargs['pk'])
        form = FestivoForm(instance=festivo)

        return render(request, self.template_name, {'form': form, 'festivo':festivo})

    def post(self, request, *args, **kwargs):
        festivo = get_object_or_None(DiaFestivo, pk=self.kwargs['pk'])
        form = self.form_class(request.POST, request.FILES, instance=festivo)

        if form.is_valid():
            festivo = form.save(commit=False)
            festivo.restaurante = festivo.restaurante
            festivo.save()
            return HttpResponseRedirect(reverse('festivos'))
        else:

            return render(request, self.template_name, {'form': form, 'festivo':festivo})


class FestivoDelete(CreateView):
    template_name = 'festivo_delete.html'
    form_class = ContrasenaForm

    def get(self, request, *args, **kwargs):
        festivo = get_object_or_None(DiaFestivo, pk=self.kwargs['pk'])
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'festivo': festivo})

    def post(self, request, *args, **kwargs):
        festivo = get_object_or_None(DiaFestivo, pk=self.kwargs['pk'])
        form = self.form_class(request.POST)
        password = form['contrasena'].value()
        correcto = request.user.check_password(password)
        if correcto:
            festivo.delete()
            return HttpResponseRedirect(reverse('festivos'))
        else:
            return render(request, self.template_name, {'form': form, 'festivo': festivo})