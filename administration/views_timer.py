
from django.http import JsonResponse
from django.template.defaultfilters import date
from django.views.decorators.csrf import csrf_exempt
from annoying.functions import get_object_or_None
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView
from django.urls import reverse
from django.http import HttpResponseRedirect

from administration.models import *



class Timer(CreateView):
    template_name = 'timer.html'

    def get(self, request, *args, **kwargs):
        centers = request.user.center_set.all()
        projects = request.user.project_set.all()

        workdays = Workday.objects.filter(user=request.user).order_by('-pk')[:10]
        current_workday = get_object_or_None(Workday, user=request.user, date_start__isnull=False, date_end__isnull=True)
        current_project_time = get_object_or_None(ProjectTime, user=request.user, date_start__isnull=False, date_end__isnull=True)


        return render(request, self.template_name, {
            'centers': centers,
            'current_project_time': current_project_time,
            'projects': projects,
            'workdays': workdays,
            'current_workday': current_workday,
        })


class DeleteWorkday(DeleteView):

    def get(self, request, *args, **kwargs):
        workday = get_object_or_None(Workday, pk=self.kwargs['pk'])
        workday.delete()

        return HttpResponseRedirect(reverse('timer'))


@csrf_exempt
def get_center_location(request):

    try:
        center = Center.objects.get(pk=request.POST['pk'])

        response_data = {'result': 'ok', 'lat': center.lat, 'lng': center.lng}

    except Exception as e:
        print(e)
        response_data = {'result': 'error', 'message': str(e)}

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
                                                          project=Project.objects.get(pk=project_pk))

                response_data = {'result': 'ok',
                                 'center': workday.center.name,
                                 'date_start': date(workday.date_start,'Y-m-d H:i'),
                                 'url':reverse('delete_workday',args=[workday.pk]),
                                 'project': project_time.project.name}

            else:
                response_data = {'result': 'ok',
                                 'pk': workday.pk,
                                 'center': workday.center.name,
                                 'date_start': date(workday.date_start,'Y-m-d H:i'),
                                 'url': reverse('delete_workday', args=[workday.pk]),
                                 'project': ''}

        else:
            response_data = {'result': 'error', 'message': 'Ya tienes una jornada activa'}

    except Exception as e:
        print(e)
        response_data = {'result': 'error', 'message': str(e)}

    return JsonResponse(response_data)


@csrf_exempt
def end_workday(request):

    try:
        center_pk = request.POST['center_pk']
        lat = request.POST['lat']
        lng = request.POST['lng']
        comment = request.POST['comment']

        current_time = timezone.now()
        current_workday = get_object_or_None(Workday, center__pk=int(center_pk),
                                             user=request.user, date_start__isnull=False, date_end__isnull=True)
        project_time = get_object_or_None(ProjectTime, user=request.user,
                                                  date_start__isnull=False, date_end__isnull=True)

        if current_workday is not None:

            if project_time is not None:
                project_time.paused = False
                project_time.date_end = current_time
                project_time.save()

            if current_workday.paused is True:
                pause = get_object_or_None(Pause, workday=current_workday, date_start__isnull=False,
                                           date_end__isnull=True)

                if pause is not None:
                    pause.lat_end = lat
                    pause.lng_end = lng
                    pause.comment_end = comment
                    pause.date_end = current_time
                    pause.save()

            current_workday.lat_end = lat
            current_workday.lng_end = lng
            current_workday.comment_end = comment
            current_workday.date_end = current_time
            current_workday.save()

            response_data = {'result': 'ok', 'date_end': date(current_workday.date_end,'Y-m-d H:i') }

        else:
            response_data = {'result': 'error', 'message': 'No hay jornada activa'}

    except Exception as e:
        print(e)
        response_data = {'result': 'error', 'message': str(e)}

    return JsonResponse(response_data)


@csrf_exempt
def pause_workday(request):

    try:
        center_pk = request.POST['center_pk']
        lat = request.POST['lat']
        lng = request.POST['lng']
        comment = request.POST['comment']

        current_workday = get_object_or_None(Workday, center__pk=int(center_pk),
                                             user=request.user, date_start__isnull=False, date_end__isnull=True)

        project_time = get_object_or_None(ProjectTime, user=request.user,
                                             date_start__isnull=False, date_end__isnull=True)

        if current_workday is not None:
            pause = get_object_or_None(Pause, workday=current_workday, date_start__isnull=False, date_end__isnull=True)

            if pause is None:

                if project_time is not None:
                    project_time.date_end = timezone.now()
                    project_time.save()

                pause = Pause.objects.create(workday=current_workday,
                                             comment_start=comment,
                                             lat_start=lat, lat_end=lng)

                current_workday.paused = True
                current_workday.save()

                response_data = {'result': 'ok'}
            else:
                response_data = {'result': 'error', 'message': 'Ya hay una pausa activa'}

        else:
            response_data = {'result': 'error', 'message': 'No hay jornada activa'}

    except Exception as e:
        # print(e)
        response_data = {'result': 'error', 'message': str(e)}

    return JsonResponse(response_data)


@csrf_exempt
def resume_workday(request):

    try:
        project_pk = request.POST['project_pk']
        center_pk = request.POST['center_pk']
        lat = request.POST['lat']
        lng = request.POST['lng']
        comment = request.POST['comment']

        current_workday = get_object_or_None(Workday, center__pk=int(center_pk),
                                             user=request.user, date_start__isnull=False, date_end__isnull=True)

        if current_workday is not None:
            pause = get_object_or_None(Pause, workday=current_workday, date_start__isnull=False, date_end__isnull=True)

            if pause is not None:

                pause.lat_end = lat
                pause.lng_end = lng
                pause.comment_end = comment
                pause.date_end = timezone.now()
                pause.save()

                current_workday.paused = False
                current_workday.save()

                if int(project_pk) != -1:
                    project_time = ProjectTime.objects.create(user=request.user,
                                                              project=Project.objects.get(pk=project_pk))

                response_data = {'result': 'ok'}

            else:
                response_data = {'result': 'error', 'message': 'No hay ninguna pausa activa'}
        else:
            response_data = {'result': 'error', 'message': 'No hay jornada activa'}

    except Exception as e:
        # print(e)
        response_data = {'result': 'error', 'message': str(e)}

    return JsonResponse(response_data)


@csrf_exempt
def change_project(request):

    try:
        project_pk = request.POST['project_pk']

        project_time = get_object_or_None(ProjectTime, user=request.user,
                                          date_start__isnull=False, date_end__isnull=True)

        if project_time is not None:
            project_time.date_end = timezone.now()
            project_time.save()

        if int(project_pk) != -1:
            project_time = ProjectTime.objects.create(user=request.user,
                                                      project=Project.objects.get(pk=project_pk))

        response_data = {'result': 'ok'}



    except Exception as e:
        # print(e)
        response_data = {'result': 'error', 'message': str(e)}

    return JsonResponse(response_data)