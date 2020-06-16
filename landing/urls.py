
from django.conf.urls import url
from landing import views



urlpatterns = [

    url(r'^$', views.Home.as_view(), name='index'),
    url(r'^privacy_policy/$', views.PrivacyPolicy.as_view(), name='privacy_policy'),

]