from django.db import models

# Create your models here.
class Provincias(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=40)
    zona = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=150)

class Actividades(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)


class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()

# DATOS PARA LISTA DESPLEGABLE:
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
class Experiencias(models.Model):
    #codigo_actividad= models.IntegerField()
    #codigo_provincia= models.IntegerField()
    provincia=models.CharField(max_length=20,choices=OPCIONES_PROVINCIAS,default=OPCIONES_PROVINCIAS[0])
    actividad=models.CharField(max_length=15,choices=OPCIONES_ACTIVIDADES,default=OPCIONES_ACTIVIDADES[0])
    usuario = models.CharField(max_length=35,choices=OPCIONES_USERS,default=OPCIONES_USERS[0])
    experiencia= models.TextField(max_length=140)
    fecha_experiencia = models.DateField()
    