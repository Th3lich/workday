
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from administration import views_timer, views_dashboard, views_projects, views_company, views_documents



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
    url(r'^change_project/$', login_required(views_timer.change_project), name='change_project'),

    url(r'^projects/$', login_required(views_projects.Projects.as_view()), name='projects'),

    url(r'^company_settings/(?P<pk>\d+)$', login_required(views_company.CompanySettings.as_view()), name='company_settings'),
    url(r'^employee_create/(?P<pk>\d+)$', login_required(views_company.CreateEmployee.as_view()), name='employee_create'),
    url(r'^company_projects/(?P<pk>\d+)$', login_required(views_projects.CompanyProjects.as_view()), name='company_projects'),
    url(r'^project_create/$', login_required(views_company.CreateProyect.as_view()), name='project_create'),
    url(r'^delete_project/(?P<pk>\d+)$', login_required(views_projects.DeleteProject.as_view()), name='delete_project'),
    url(r'^add_employee_project/<int:user_pk>/<int:project_pk>$', login_required(views_projects.AddEmployeeProject.as_view()), name='add_employee_project'),
    url(r'^center_create/$', login_required(views_company.CreateCenter.as_view()), name='center_create'),

    url(r'^documents/$', login_required(views_documents.Documents.as_view()), name='documents')

]