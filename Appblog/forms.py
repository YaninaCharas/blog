#Tenemos que revisar la key de los modelos para poder relacionarlos

#from socket import fromshare
from turtle import textinput
from django import forms

# Acá van los formularios
class FormularioProvincias(forms.Form):
    codigo=forms.IntegerField()
    nombre=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder':'Nombre de la provincia'}))
    zona=forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':'Departamento,ciudad, municipio, etc.'}))
    descripcion=forms.CharField(max_length=150,widget=forms.TextInput(attrs={'placeholder':'Clima, tipo de bioma, fauna.'}))

class FormularioActividades(forms.Form):
    codigo=forms.IntegerField()
    nombre=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'¿Qué tipo de actividad recreativa es?'}))
    descripcion=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'En pocas palabras: ¿de qué trata esta actividad?'}))

class FormularioUsuarios(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()
    edad=forms.IntegerField()

# DATOS PARA LISTA DESPLEGABLE
# La usaremos en primera instancia, pero la idea
# para la entrega final es que la lista retorne
# las provincias, las actividades y los users
# directamente desde la base de datos. Ésto
# requiere de hacer CRUD, creo.
OPCIONES_PROVINCIAS=(
    ('Tierra del Fuego','Tierra del Fuego'),
    ('Buenos Aires','Buenos Aires')
)
OPCIONES_ACTIVIDADES=(
    ('Cabalgata','Cabalgata'),
    ('Trekking','Trekking')
)
OPCIONES_USERS=(
    ('belenpeluffo@gmail.com','Belén Peluffo'),
    ('yaninacharas@gmail.com','Yanina Charas')
)

# CLASE PARA MODIFFICAR ASPECTO DEL CAMPO FECHA_EXPERIENCIA:
# (porque si no aparece como cuadro de texto a rellenar)
class Calendario(forms.DateInput):
    input_type = 'date'

class FormularioExperiencias(forms.Form):
    #codigo_actividad= forms.IntegerField()
    #codigo_provincia= forms.IntegerField()
    provincia=forms.ChoiceField(choices=OPCIONES_PROVINCIAS)
    actividad=forms.ChoiceField(choices=OPCIONES_ACTIVIDADES)
    usuario = forms.ChoiceField(choices=OPCIONES_USERS)
    experiencia= forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Contanos en 140 caracteres o menos cómo fue tu experiencia.'}))
    fecha_experiencia = forms.DateField(widget=Calendario)