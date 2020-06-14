
from django.shortcuts import render
from django.views.generic import CreateView



class Projects(CreateView):
    template_name = 'projects.html'

    def get(self, request, *args, **kwargs):
        projects = request.user.project_set.all()

        return render(request, self.template_name, {
            'projects': projects
        })