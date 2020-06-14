# -*- encoding: utf-8 -*-

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from users import forms
from django.views.generic import UpdateView
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


class AccountSettings(UpdateView):
    template_name = 'account_settings.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        form = forms.EditUserForm(initial={'nif':user.extrauserdata.nif,
                                                    'first_name':user.first_name,
                                                    'last_name':user.last_name,
                                                    'email':user.email,
                                                    'address':user.extrauserdata.address,
                                                    'phone':user.extrauserdata.phone,
                                                    'photo':user.extrauserdata.photo})

        return render(request, self.template_name, {
            'form': form,
            'user': user
        })

    def post(self, request, *args, **kwargs):

        user = request.user
        form = forms.EditUserForm(request.POST, request.FILES)

        if form.is_valid():

            photo = form.cleaned_data['photo']
            nif = form.cleaned_data['nif']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']

            if photo is not None and photo != "":
                user.extrauserdata.photo = photo

            user.username = nif
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.extrauserdata.address = address
            user.extrauserdata.phone = phone

            user.save()

            user.extrauserdata.save()

            return HttpResponseRedirect(reverse('account_settings'))

        else:

            return render(request, self.template_name, {
                'form': form,
                'user': user
            })


@csrf_exempt
def change_theme(request):

    try:

        checked = request.POST["checked"]

        if checked == 1:
            request.session['darkmode'] = True
        else:
            request.session['darkmode'] = False


        response_data = {'result': 'ok', 'checked': checked}

    except Exception as e:
        # print(e)
        response_data = {'result': 'error', 'mensaje': str(e)}

    return JsonResponse(response_data)



# class UsuarioCreate(FormView):
#     template_name = 'users/usuario_create.html'
#     form_class = forms.UsuarioForm
#     second_form_class = UserCreationForm
#
#     def get(self, request, *args, **kwargs):
#         usuarioform = self.form_class(initial=self.initial)
#
#         return render(request, self.template_name, { 'usuarioform': usuarioform})
#
#     def post(self, request, *args, **kwargs):
#         data = request
#
#         usuarioform = forms.UsuarioForm(data.POST, data.FILES)
#
#         if  usuarioform.is_valid():
#             #password = contrasena.contrasena_generator()
#             password = "123456789"
#
#             email = usuarioform['email'].value()
#             email = email.lower()
#             if User.objects.exclude(pk=request.user.pk).filter(username=email).exists():
#                 error =u"Usuario ya existente"
#                 return render(request, self.template_name, {'mensaje':error,'usuarioform': usuarioform})
#             administrador = usuarioform['administrador'].value()
#             nombre=usuarioform['nombre'].value()
#             apellidos= usuarioform['apellidos'].value()
#             djangouser = User(username=email)
#             djangouser.set_password(password)
#             djangouser.email = email
#             djangouser.is_staff = administrador
#             djangouser.is_superuser = administrador
#             djangouser.first_name=nombre
#             djangouser.last_name=apellidos
#             djangouser.save()
#             asunto = u'Usuario y Contraseña Factudreams'
#             texto = u'Bienvenido, estos son los datos para acceder: \n\n'
#             texto+=u"Su nombre de usuario es: "+email+"\n"
#             texto+=u"Su pasword es: "+password+"\n"
#             texto+=u"\nPuede cambiarla dentro de la web : http://conta.tecnisolarasistencia.com/"
#
#             send_mail(asunto,texto,'tecnisolarf@hotmail.com',[djangouser.email,])
#             if administrador:
#                 return http.HttpResponseRedirect(reverse('administradores_list'))
#             else:
#                 return http.HttpResponseRedirect(reverse('trabajadores_list'))
#
#         return render(request, self.template_name, {'usuarioform': usuarioform})
#
# class UsuarioEdit(FormView):
#     template_name = 'users/usuario_edit.html'
#     form_class = forms.UsuarioForm
#     second_form_class = UserCreationForm
#
#     def get(self, request, *args, **kwargs):
#         usuario = get_object_or_404(models.User, pk=self.kwargs['pk'])
#         usuarioform = self.form_class(initial={'email':usuario.email,'nombre':usuario.first_name,
#                                                'apellidos':usuario.last_name,'administrador':usuario.is_staff})
#         return render(request, self.template_name, { 'usuarioform': usuarioform,'usuario':usuario})
#
#     def post(self, request, *args, **kwargs):
#         data = request
#         usuario = get_object_or_404(models.User, pk=self.kwargs['pk'])
#         usuarioform = forms.UsuarioForm(data.POST, data.FILES)
#
#         if  usuarioform.is_valid():
#
#             djangouser = usuario
#             email = usuarioform['email'].value()
#             email = email.lower()
#             administrador = usuarioform['administrador'].value()
#             nombre=usuarioform['nombre'].value()
#             apellidos= usuarioform['apellidos'].value()
#             djangouser.username = email
#             djangouser.email = email
#             djangouser.is_staff = administrador
#             djangouser.is_superuser = administrador
#             djangouser.first_name=nombre
#             djangouser.last_name=apellidos
#             djangouser.save()
#             if administrador:
#                 return http.HttpResponseRedirect(reverse('administradores_list'))
#             else:
#                 return http.HttpResponseRedirect(reverse('clientes_list'))
#
#         return render(request, self.template_name, { 'usuarioform': usuarioform,'usuario':usuario})