#from socket import fromshare
from django import forms

# Acá van los formularios
class FormularioProvincias(forms.Form):
    nombre=forms.CharField()
    zona=forms.CharField()
    codigo=forms.IntegerField()
    descripcion=forms.CharField()

class FormularioActividades(forms.Form):
    nombre=forms.CharField()
    descrpcion=forms.CharField()
    provincia=forms.IntegerField()

class FormularioUsuarios(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()
    edad=forms.IntegerField()