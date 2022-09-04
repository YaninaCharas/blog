from django.urls import path
from Appblog.views import formulario_actividades, formulario_usuarios, inicio, formulario_provincias, formulario_experiencias



urlpatterns = [
    path('', inicio, name='AppblogInicio'),
    path('provincias/', formulario_provincias, name='AppblogFormularioProvincias'),
    path('actividades/', formulario_actividades, name='AppblogFormularioActividades'),
    path('usuarios/', formulario_usuarios, name='AppblogFormularioUsuarios'),
    path('experiencias/', formulario_experiencias, name='AppblogFormularioExperiencias'),
]