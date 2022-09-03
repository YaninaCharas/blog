#Tenemos que revisar la key de los modelos para poder relacionarlos

#from socket import fromshare
from django import forms

# Acá van los formularios
class FormularioProvincias(forms.Form):
    zona=forms.CharField()
    nombre=forms.CharField()
    descripcion=forms.CharField()

class FormularioActividades(forms.Form):
    nombre=forms.CharField()
    descrpcion=forms.CharField()

class FormularioUsuarios(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()
    edad=forms.IntegerField()