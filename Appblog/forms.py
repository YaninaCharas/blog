#Tenemos que revisar la key de los modelos para poder relacionarlos

#from socket import fromshare
from django import forms

# Acá van los formularios
class FormularioProvincias(forms.Form):
    codigo=forms.IntegerField()
    nombre=forms.CharField(max_length=40)
    zona=forms.CharField(max_length=15)
    descripcion=forms.CharField(max_length=150)

class FormularioActividades(forms.Form):
    codigo=forms.IntegerField()
    nombre=forms.CharField(max_length=30)
    descrpcion=forms.CharField(max_length=30)

class FormularioUsuarios(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()
    edad=forms.IntegerField()