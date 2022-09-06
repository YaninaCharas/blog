from django.urls import path
from Appblog.views import formulario_actividades, formulario_usuarios
from Appblog.views import inicio, formulario_provincias, formulario_experiencias
from django.urls import path
from userblog.views import *

urlpatterns = [
        path('login/', login_request, name='userbloglogin'),
]