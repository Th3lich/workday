from django.shortcuts import render

from django.views.generic import CreateView
from django.shortcuts import render


class Home(CreateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {})


class PrivacyPolicy(CreateView):
    template_name = 'privacy-policy.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {})
