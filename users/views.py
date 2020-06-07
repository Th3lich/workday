# -*- encoding: utf-8 -*-
from django.core.mail import send_mail

from users import forms, models
from users import forms
from django.views.generic import ListView, FormView, DeleteView,CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
import django.http as http
from django.urls import reverse
from django.utils.encoding import smart_str
from django.contrib.auth.models import User
from annoying.functions import get_object_or_None
#from utilities import enviarmail,contrasena
import datetime
from django.utils.timezone import utc
from django.db.models import Q


from django.http import HttpResponse
from django.contrib import auth
import json
from django.views.decorators.csrf import csrf_exempt

class AdministradoresList(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/administradores_list.html'

    def get_queryset(self):
        by_id = User.objects.filter(is_staff=True).order_by('id')

        return by_id

class TrabajadoresList(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/trabajadores_list.html'

    def get(self, request, *args, **kwargs):
        by_id = User.objects.filter(is_staff=False).order_by('id')
        usuarios = models.ExtraUserData.objects.all().order_by('usuario')
        form = forms.BusquedaForm(request.GET)
        publicidad = False
        if form.is_valid():
            try:
                q = form.cleaned_data['marca']
                if q != '':
                    usuarios = usuarios.filter(
                        Q(usuario__username=q) | Q(usuario__email=q)).distinct()
            except:
                pass
            try:
                q = form.cleaned_data['modelo']
                if q != '':
                    usuarios = usuarios.filter(
                        Q(ciudad=q)).distinct()
            except:
                pass
            try:
                q = form.cleaned_data['quiere_revision']
                if q == True:
                    publicidad = True
                    usuarios = usuarios.filter(
                        Q(publicidad=q)).distinct()
            except:
                pass

        return render(request, self.template_name, {'users': usuarios,
                                                    'form': form})

class UsuarioCreate(FormView):
    template_name = 'users/usuario_create.html'
    form_class = forms.UsuarioForm
    second_form_class = UserCreationForm

    def get(self, request, *args, **kwargs):
        usuarioform = self.form_class(initial=self.initial)

        return render(request, self.template_name, { 'usuarioform': usuarioform})

    def post(self, request, *args, **kwargs):
        data = request

        usuarioform = forms.UsuarioForm(data.POST, data.FILES)

        if  usuarioform.is_valid():
            #password = contrasena.contrasena_generator()
            password = "123456789"

            email = usuarioform['email'].value()
            email = email.lower()
            if User.objects.exclude(pk=request.user.pk).filter(username=email).exists():
                error =u"Usuario ya existente"
                return render(request, self.template_name, {'mensaje':error,'usuarioform': usuarioform})
            administrador = usuarioform['administrador'].value()
            nombre=usuarioform['nombre'].value()
            apellidos= usuarioform['apellidos'].value()
            djangouser = User(username=email)
            djangouser.set_password(password)
            djangouser.email = email
            djangouser.is_staff = administrador
            djangouser.is_superuser = administrador
            djangouser.first_name=nombre
            djangouser.last_name=apellidos
            djangouser.save()
            asunto = u'Usuario y Contraseña Factudreams'
            texto = u'Bienvenido, estos son los datos para acceder: \n\n'
            texto+=u"Su nombre de usuario es: "+email+"\n"
            texto+=u"Su pasword es: "+password+"\n"
            texto+=u"\nPuede cambiarla dentro de la web : http://conta.tecnisolarasistencia.com/"

            send_mail(asunto,texto,'tecnisolarf@hotmail.com',[djangouser.email,])
            if administrador:
                return http.HttpResponseRedirect(reverse('administradores_list'))
            else:
                return http.HttpResponseRedirect(reverse('trabajadores_list'))

        return render(request, self.template_name, {'usuarioform': usuarioform})

class UsuarioEdit(FormView):
    template_name = 'users/usuario_edit.html'
    form_class = forms.UsuarioForm
    second_form_class = UserCreationForm

    def get(self, request, *args, **kwargs):
        usuario = get_object_or_404(models.User, pk=self.kwargs['pk'])
        usuarioform = self.form_class(initial={'email':usuario.email,'nombre':usuario.first_name,
                                               'apellidos':usuario.last_name,'administrador':usuario.is_staff})
        return render(request, self.template_name, { 'usuarioform': usuarioform,'usuario':usuario})

    def post(self, request, *args, **kwargs):
        data = request
        usuario = get_object_or_404(models.User, pk=self.kwargs['pk'])
        usuarioform = forms.UsuarioForm(data.POST, data.FILES)

        if  usuarioform.is_valid():

            djangouser = usuario
            email = usuarioform['email'].value()
            email = email.lower()
            administrador = usuarioform['administrador'].value()
            nombre=usuarioform['nombre'].value()
            apellidos= usuarioform['apellidos'].value()
            djangouser.username = email
            djangouser.email = email
            djangouser.is_staff = administrador
            djangouser.is_superuser = administrador
            djangouser.first_name=nombre
            djangouser.last_name=apellidos
            djangouser.save()
            if administrador:
                return http.HttpResponseRedirect(reverse('administradores_list'))
            else:
                return http.HttpResponseRedirect(reverse('clientes_list'))

        return render(request, self.template_name, { 'usuarioform': usuarioform,'usuario':usuario})

class UsuarioDelete(DeleteView):
    template_name = 'users/usuario_delete.html'
    form_class = forms.ContrasenaForm

    def get(self, request, *args, **kwargs):

        form = self.form_class()

        usuario = get_object_or_404(models.User, pk=self.kwargs['pk'])
        return render(request, self.template_name, {'usuario': usuario, 'form':form})

    def post(self, request, *args, **kwargs):
        djangouser = get_object_or_404(models.User, pk=self.kwargs['pk'])
        form = self.form_class(request.POST)
        password = form['contrasena'].value()
        correcto = request.user.check_password(password)
        if correcto:
            if djangouser.pk != 1:
                if djangouser.is_superuser:
                    djangouser.delete()
                    return http.HttpResponseRedirect(reverse('administradores_list'))
                else:
                    djangouser.delete()
                    return http.HttpResponseRedirect(reverse('trabajadores_list'))
            else:
                return http.HttpResponseRedirect(reverse('administradores_list'))

        else:
            return render(request, self.template_name, {'usuario': djangouser ,'form':form})

class UsuarioPerfil(CreateView):
    model = User
    context_object_name = 'usuario'
    template_name = 'users/usuario_perfil.html'

    def get(self, request, *args, **kwargs):

        usuario = get_object_or_404(models.User, pk=self.kwargs['pk'])
        return render(request, self.template_name, {'usuario': usuario,})

class UsuarioRecuperarContrasena(CreateView):

    template_name = 'users/recuperar_contrasena.html'
    template_respuesta = 'users/recuperar_contrasena_respuesta.html'
    form_class = forms.RecuperarContrasenaForm
    def get(self, request, *args, **kwargs):


        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        email = form['email'].value()
        try:
            men="El correo no esta registrado"
            usuario = get_object_or_None(models.User, email=email)
            if usuario is None:
                men="El correo no esta registrado"
            else:


                token_pass= contrasena.contrasena_generator()
                enl =models.TokenRecuperarPass(user=usuario,token=token_pass)
                enl.save()

                enlace = u'http://aplicacion.construccionesrodriguez.es/users/confirmarrecuperarpass/'+token_pass
                #enlace = u'http://192.168.1.12:8000/usuarios/confirmarrecuperarpass/'+token_pass
                asunto = smart_str(u'Recuperar password')

                texto = smart_str(u'Bienvenido, haga click en el siguiente enlace para recuperar su password: \n\n')
                texto+= enlace

                enviarmail.enviarmail(texto,asunto,email)
                men="Se ha enviado un correo con el que podra recuperar la contraseña"

        except Exception as e:
            men = e.args

        return render(request, self.template_respuesta, {'men':men})

class ConfirmarMailRecuperarContrasena(CreateView):

    template_name = 'users/confirmar_cambiar_pass.html'
    template_name_denegar = 'users/denegar_cambiar_pass.html'
    template_respuesta = 'users/recuperar_contrasena_respuesta.html'
    form_class = forms.RecuperarContrasenaFormMail

    def get(self, request, *args, **kwargs):
        token = self.kwargs['token']

        objeto_token = get_object_or_None(models.TokenRecuperarPass, token=token)
        if objeto_token is not None:
            fecha = objeto_token.date
            ahora= datetime.datetime.utcnow().replace(tzinfo=utc)
            form = self.form_class(initial=self.initial)
            diff=ahora -fecha

            if diff.total_seconds() <= 10000:
                return render(request, self.template_name, {'form':form,'token':objeto_token.token, 'usuario':objeto_token.user})
            else:
                mensaje = "El tiempo de recuperación se ha agotado. Vuelva a recuperar la contraseña"
                return render(request, self.template_name_denegar, {'form':form, 'mensaje':mensaje})
        else:

            mensaje = "no se ha podido recuperar el usuario"
            return render(request, self.template_name_denegar, {'mensaje':mensaje})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        contrasena_nueva = form['nueva'].value()
        contrasena_nueva_confirmada = form['renueva'].value()
        if contrasena_nueva == contrasena_nueva_confirmada:
            token = get_object_or_None(models.TokenRecuperarPass, token=self.kwargs['token'])
            usuario = token.user


            if usuario is None:
                men="El usuario no existe "
                return render(request, self.template_respuesta, {'men':men})
            else:
                usuario.set_password(contrasena_nueva)
                token.delete()
                men="contraseña cambiada "
        return render(request, self.template_respuesta, {'men':men})

class CambiarPass(FormView):
    template_name = 'users/cambiar_pass.html'
    form_class = forms.CambiarContrasenaForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        usuario = get_object_or_404(models.User, pk=self.kwargs['pk'])
        return render(request, self.template_name, {'usuario': usuario,'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        usuario = get_object_or_404(models.User, pk=self.kwargs['pk'])
        djangouser = usuario
        if form.is_valid():
            antigua = form['antigua'].value()
            nueva = form['nueva'].value()
            renueva = form['renueva'].value()
            correcto = request.user.check_password(antigua)
            if correcto:
                if nueva == renueva:
                    djangouser.set_password(nueva)
                    djangouser.save()
                    return http.HttpResponseRedirect(reverse('usuario_perfil', args=(djangouser.pk,)))
                else:
                    men = "Las contraseñas no coinciden."
                    return render(request, self.template_name, {'usuario': usuario,'form':form, 'mensaje':men})
            else:
                men = "La contraseña antigua no es correcta. "
                return render(request, self.template_name, {'usuario': usuario,'form':form, 'mensaje':men})

        return render(request, self.template_name, {'usuario': usuario,'form':form})