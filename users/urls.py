
from django.conf.urls import include,url
from django.contrib.auth.decorators import login_required
from users import views


urlpatterns = [

    url(r'^account_settings/$', login_required(views.AccountSettings.as_view()), name='account_settings'),
    url(r'^change_theme/$', views.change_theme, name='change_theme'),
    url('register/', views.Register.as_view(), name='register'),
    url('register-employee/(?P<pk>\d+)$', views.RegisterEmployee.as_view(), name='register_employee'),

]