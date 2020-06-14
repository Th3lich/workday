
from django.shortcuts import render
from django.views.generic import CreateView


class RedirectToDashboard(CreateView):

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {})


class DashboardIndividual(CreateView):
    template_name = 'dashboard_individual.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {})


class DashboardCompany(CreateView):
    template_name = 'dashboard_company.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {})