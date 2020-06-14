
from django.conf.urls import include,url
from django.contrib.auth.decorators import login_required
from users import views


urlpatterns = [

    url(r'^account_settings/$', login_required(views.AccountSettings.as_view()), name='account_settings'),
    url(r'^change_theme/$', views.change_theme, name='change_theme'),
# url(r'^change_theme/(?P<check>\d+)/$', views.change_theme.as_view(), name='change_theme')

]