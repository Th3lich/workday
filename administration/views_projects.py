from annoying.functions import get_object_or_None
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView
from django.urls import reverse
from django.http import HttpResponseRedirect

from administration.models import Company, Project


class Projects(CreateView):
    template_name = 'projects.html'

    def get(self, request, *args, **kwargs):
        projects = request.user.project_set.all()

        return render(request, self.template_name, {
            'projects': projects
        })


class CompanyProjects(CreateView):
    template_name = 'company_projects.html'

    def get(self, request, *args, **kwargs):
        company = get_object_or_None(Company, pk=self.kwargs['pk'], owner=request.user.pk)
        projects = Project.objects.filter(company=company)

        return render(request, self.template_name, {
            'company': company,
            'projects': projects,
            'default_param':-1
        })


class DeleteProject(DeleteView):

    def get(self, request, *args, **kwargs):
        project = get_object_or_None(Project, pk=self.kwargs['pk'])
        project.delete()

        return HttpResponseRedirect(reverse('company_projects', args=[project.company.pk]))


class AddEmployeeProject(CreateView):
    def get(self, request, *args, **kwargs):
        user = self.kwargs['user_pk']
        project = self.kwargs['project_pk']

        print (user)
        print (project)

        return HttpResponseRedirect(reverse('projects'))