from django.shortcuts import render
from django.views.generic import CreateView

from administration.models import *


class Dashboard(CreateView):
    template_name = 'dashboard_individual.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {})
