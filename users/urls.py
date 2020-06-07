
from django.conf.urls import include,url
from django.contrib.auth.decorators import login_required
from users import views


urlpatterns = [


    url(r'^administradores/$', login_required(views.AdministradoresList.as_view()), name='administradores_list'),
    url(r'^trabajadores/$', login_required(views.TrabajadoresList.as_view()), name='trabajadores_list'),
    url(r'^crear/$', login_required(views.UsuarioCreate.as_view()), name='usuario_create'),
    url(r'^perfil/(?P<pk>\d+)$', login_required(views.UsuarioPerfil.as_view()), name='usuario_perfil'),
    url(r'^editar/(?P<pk>\d+)$', login_required(views.UsuarioEdit.as_view()), name='usuario_edit'),
    url(r'^borrar/(?P<pk>\d+)$', login_required(views.UsuarioDelete.as_view()), name='usuario_delete'),
    url(r'^cambiarpass/(?P<pk>\d+)$', login_required(views.CambiarPass.as_view()), name='usuario_cambiar_pass'),
    url(r'^recuperarpass/$', views.UsuarioRecuperarContrasena.as_view(), name='recuperar_contrasena'),
    url(r'^confirmarrecuperarpass/(?P<token>\w+)$', views.ConfirmarMailRecuperarContrasena.as_view(),
        name='confirmar_cambiar_pass'),
]