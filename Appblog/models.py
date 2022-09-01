from django.db import models

# Create your models here.
class Provincias(models.Model):
    nombre = models.CharField(max_length=40)
    zona = models.CharField(max_length=15)
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=150)


class Actividades(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    provincia = models.IntegerField()


class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.IntegerField()
