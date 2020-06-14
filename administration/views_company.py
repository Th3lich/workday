import threading

from annoying.functions import get_object_or_None
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from administration import forms
from administration.models import Company
from configuracion import settings


class CompanySettings(CreateView):
    template_name = 'company_settings.html'

    def get(self, request, *args, **kwargs):
        company = get_object_or_None(Company, pk=self.kwargs['pk'], owner=request.user.pk)
        form = forms.EditCompanyForm(initial={'cif': company.cif,
                                           'name': company.name,
                                           'photo': company.photo})

        return render(request, self.template_name, {
            'form': form,
            'company': company
        })

    def post(self, request, *args, **kwargs):

        company = get_object_or_None(Company, pk=self.kwargs['pk'], owner=request.user.pk)
        form = forms.EditCompanyForm(request.POST, request.FILES)

        if form.is_valid():

            photo = form.cleaned_data['photo']
            name = form.cleaned_data['name']
            cif = form.cleaned_data['cif']

            if photo is not None and photo != "":
                company.photo = photo

            company.name = name
            company.cif = cif

            company.save()

            return HttpResponseRedirect(reverse('company_settings', args=[company.pk]))

        else:

            return render(request, self.template_name, {
                'form': form,
                'company': company
            })


class CreateEmployee(CreateView):
    template_name = 'create_employee.html'

    def get(self, request, *args, **kwargs):
        company = get_object_or_None(Company, pk=self.kwargs['pk'], owner=request.user.pk)
        form = forms.AddEmployeeForm()

        return render(request, self.template_name, {
            'form': form,
            'company': company
        })

    def post(self, request, *args, **kwargs):
        company = get_object_or_None(Company, pk=self.kwargs['pk'], owner=request.user.pk)
        form = forms.AddEmployeeForm(request.POST)
        result = "error"
        message = "Ha habido un fallo, vuelve a intentarlo"
        recipient = 'javilpx2.jl@gmail.com'

        if form.is_valid():
            asunto = "Has sido invitado a la %s en Workday++" %company.name
            mensaje = "El usuario: " + form['email'].value() + "\n"
            t = threading.Thread(target=send_mail, args=(
                asunto, mensaje, settings.DEFAULT_FROM_EMAIL, [recipient], False, None, None, None, mensaje))
            t.start()
            result = "success"
            message = "Mensaje enviado correctamente"


        return render(request, self.template_name, {
            'form': form,
            'company': company,
            'result': result,
            'message': message,
        })


class CreateProyect(CreateView):
    template_name = 'company_settings.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {

        })


class CreateCenter(CreateView):
    template_name = 'company_settings.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {

        })