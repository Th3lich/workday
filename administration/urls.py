
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from administration import views_timer, views_dashboard, views_projects



urlpatterns = [

    url(r'^dashboard_individual/$', login_required(views_dashboard.DashboardIndividual.as_view()), name='dashboard_individual'),
    url(r'^dashboard_company/$', login_required(views_dashboard.DashboardCompany.as_view()), name='dashboard_company'),
    url(r'^dashboard/$', login_required(views_dashboard.DashboardIndividual.as_view()), name='dashboard'),

    url(r'^timer/$', login_required(views_timer.Timer.as_view()), name='timer'),
    url(r'^delete_workday/(?P<pk>\d+)$', login_required(views_timer.DeleteWorkday.as_view()), name='delete_workday'),
    url(r'^get_center_location/$', login_required(views_timer.get_center_location), name='get_center_location'),
    url(r'^start_workday/$', login_required(views_timer.start_workday), name='start_workday'),
    url(r'^end_workday/$', login_required(views_timer.end_workday), name='end_workday'),
    url(r'^pause_workday/$', login_required(views_timer.pause_workday), name='pause_workday'),
    url(r'^resume_workday/$', login_required(views_timer.resume_workday), name='resume_workday'),
    url(r'^change_workday/$', login_required(views_timer.change_workday), name='change_workday'),

    url(r'^projects/$', login_required(views_projects.Projects.as_view()), name='projects')

]