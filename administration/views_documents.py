from django.shortcuts import render
from django.views.generic import CreateView



class Documents(CreateView):
    template_name = 'documents.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {

        })