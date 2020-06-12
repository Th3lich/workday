
from django.conf.urls import include,url
from django.contrib.auth.decorators import login_required
from users import views


urlpatterns = [

    url(r'^account_settings/', login_required(views.AccountSettings.as_view()), name='account_settings'),

]