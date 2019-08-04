from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView


class Admin(CreateView):

    template_name = 'base.html'

    def get(self, request, *args, **kwargs):


        return render(request, self.template_name,{})