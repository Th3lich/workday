from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView


class Index(CreateView):

    template_name = 'guia/index_8.html'

    def get(self, request, *args, **kwargs):


        return render(request, self.template_name,{})


class Guia(CreateView):

    template_name = 'guia/map_listing.html'

    def get(self, request, *args, **kwargs):


        return render(request, self.template_name,{})



class Detail(CreateView):

    template_name = 'guia/detail_page_2.html'

    def get(self, request, *args, **kwargs):


        return render(request, self.template_name,{})