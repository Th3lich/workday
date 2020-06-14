
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from annoying.functions import get_object_or_None
from django.shortcuts import render
from django.views.generic import CreateView

from administration.models import *


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


class Timer(CreateView):
    template_name = 'timer.html'

    def get(self, request, *args, **kwargs):
        centers = request.user.center_set.all()
        projects = request.user.project_set.all()

        workdays = Workday.objects.filter(user=request.user).order_by('-pk')[:10]
        current_workday = get_object_or_None(Workday, user=request.user, date_start__isnull=False, date_end__isnull=True)

        return render(request, self.template_name, {
            'centers': centers,
            'projects': projects,
            'workdays': workdays,
            'current_workday': current_workday,
        })


@csrf_exempt
def get_center_location(request):

    try:
        center = Center.objects.get(pk=request.POST['pk'])

        response_data = {'result': 'ok', 'lat': center.lat, 'lng': center.lng}

    except Exception as e:
        print(e)
        response_data = {'result': 'error', 'mensaje': str(e)}

    return JsonResponse(response_data)


@csrf_exempt
def start_workday(request):

    try:
        center_pk = request.POST['center_pk']
        project_pk = request.POST['project_pk']
        lat = request.POST['lat']
        lng = request.POST['lng']
        comment = request.POST['comment']

        workdays = Workday.objects.filter(user=request.user, date_start__isnull=False, date_end__isnull=True)

        if len(workdays) == 0:
            workday = Workday.objects.create(center=Center.objects.get(pk=center_pk),
                                             lat_start=lat,
                                             lat_end=lng,
                                             comment_start=comment,
                                             user=request.user)

            if int(project_pk) != -1:
                project_time = ProjectTime.objects.create(user=request.user,
                                                          project=project_pk)

                response_data = {'result': 'ok', 'center': workday.center.name, 'date_start': workday.date_start, 'project': project_time.project.name}

            else:
                response_data = {'result': 'ok', 'center': workday.center.name, 'date_start': workday.date_start, 'project': ''}

        else:
            response_data = {'result': 'error', 'mensaje': 'Ya tienes una jornada activa'}

    except Exception as e:
        print(e)
        response_data = {'result': 'error', 'mensaje': str(e)}

    return JsonResponse(response_data)


@csrf_exempt
def exit_workday(request):

    try:

        response_data = {'result': 'ok'}

    except Exception as e:
        # print(e)
        response_data = {'result': 'error', 'mensaje': str(e)}

    return JsonResponse(response_data)


@csrf_exempt
def pause_workday(request):

    try:

        response_data = {'result': 'ok'}

    except Exception as e:
        # print(e)
        response_data = {'result': 'error', 'mensaje': str(e)}

    return JsonResponse(response_data)


@csrf_exempt
def continue_workday(request):

    try:

        response_data = {'result': 'ok'}

    except Exception as e:
        # print(e)
        response_data = {'result': 'error', 'mensaje': str(e)}

    return JsonResponse(response_data)