
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from administration import views



urlpatterns = [

    url(r'^dashboard_individual/$', login_required(views.DashboardIndividual.as_view()), name='dashboard_individual'),
    url(r'^dashboard_company/$', login_required(views.DashboardCompany.as_view()), name='dashboard_company'),
    url(r'^dashboard/$', login_required(views.DashboardIndividual.as_view()), name='dashboard'),
    url(r'^timer/$', login_required(views.Timer.as_view()), name='timer'),
    url(r'^get_center_location/$', views.get_center_location, name='get_center_location'),
    url(r'^start_workday/$', views.start_workday, name='start_workday'),

]