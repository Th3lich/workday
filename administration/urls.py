
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from administration import views



urlpatterns = [

    url(r'^dashboard/$', login_required(views.Dashboard.as_view()), name='dashboard'),

]