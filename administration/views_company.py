import threading

from django.template.loader import get_template
from annoying.functions import get_object_or_None
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from administration import forms
from administration.models import Company, Project, Center
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
            recipient = form.cleaned_data['email']
            subject = "Has sido invitado por %s a formar parte de Workday++" %company.name
            url = "http://127.0.0.1:8000/users/register-employee/" +str(company.pk)
            template = '<table class="main" width="100%" cellpadding="0" cellspacing="0" itemprop="action" itemscope itemtype="http://schema.org/ConfirmAction" style="font-family: Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; border-radius: 3px; margin: 0; border: none;" > <tr style="font-family: Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;"> <td class="content-wrap" style="font-family: Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0;padding: 30px;border: 3px solid #6610f2;border-radius: 7px; background-color: #fff;" valign="top"> <meta itemprop="name" content="Confirm Email" style="font-family: Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;"/> <table width="100%" cellpadding="0" cellspacing="0" style="font-family: Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;"> <tr style="font-family: Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;"> <td class="content-block" style="font-family: Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0; padding: 0 0 20px;" valign="top"> Te han invitado a unirte a la cuenta de Workday++ de tu equipo. </td> </tr> <tr style="font-family: Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;"> <td class="content-block" style="font-family: Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0; padding: 0 0 20px;" valign="top"> Workday++ es el espacio de trabajo que potenciará tu jornada laboral y te ayudará a administrar el tiempo de tus proyectos. </td> </tr> <tr style="font-family: Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;"> <td class="content-block" itemprop="handler" itemscope itemtype="http://schema.org/HttpActionHandler" style="font-family: Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0; padding: 0 0 20px;" valign="top"> <a href="' +url +'" class="btn-primary" itemprop="url" style="font-family: Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; color: #FFF; text-decoration: none; line-height: 2em; font-weight: bold; text-align: center; cursor: pointer; display: inline-block; border-radius: 5px; text-transform: capitalize; background-color: #6658dd; margin: 0; border-color: #6658dd; border-style: solid; border-width: 8px 16px;"> Aceptar invitación </a> </td> </tr> </table> </td> </tr> </table>'
            t = threading.Thread(target=send_mail, args=(
                subject, template, settings.DEFAULT_FROM_EMAIL, [recipient], False, None, None, None, template))
            t.start()
            result = "success"
            message = "Se ha enviado la invitación correctamente"


        return render(request, self.template_name, {
            'form': form,
            'company': company,
            'result': result,
            'message': message,
        })


class CreateProyect(CreateView):
    template_name = 'create_project.html'

    def get(self, request, *args, **kwargs):
        form = forms.CreateProjectForm()

        return render(request, self.template_name, {
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        result = "error"
        message = "Ha habido un fallo, vuelve a intentarlo"
        form = forms.CreateProjectForm(request.POST)
        if form.is_valid():
            project = Project.objects.create(name=form.cleaned_data['name'],
                                             estimated_time=form.cleaned_data['estimated_time'],
                                             )
            project.workers.add(request.user)
            project.save()
            result = "success"


        return render(request, self.template_name, {
            'form': form,
            'result': result,
            'message': message
        })



class CreateCenter(CreateView):
    template_name = 'create_center.html'

    def get(self, request, *args, **kwargs):
        form = forms.CreateCenterForm()

        return render(request, self.template_name, {
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        result = "error"
        message = "Ha habido un fallo, vuelve a intentarlo"
        form = forms.CreateCenterForm(request.POST)
        if form.is_valid():
            center = Center.objects.create(name=form.cleaned_data['name'],
                                           lat=form.cleaned_data['lat'],
                                           lng=form.cleaned_data['lng'],
                                           company=request.user.company
                                             )
            center.workers.add(request.user)
            center.save()
            result = "success"
            message = "Se ha creado un centro exitosamente"


        return render(request, self.template_name, {
            'form': form,
            'result': result,
            'message': message
        })