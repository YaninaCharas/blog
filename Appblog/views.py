from django.shortcuts import render, redirect
from Appblog.models import Actividades, Provincias, Usuarios, Experiencias
# Importamos los formularios:
from Appblog.forms import FormularioProvincias, FormularioActividades, FormularioUsuarios, FormularioExperiencias


# Create your views here.
def inicio(request):
    return render(request, "index.html")

# La vista para ingresar a formulario_provincias.html y HACER ALGO con el
# formulario:
def formulario_provincias(request):
    if request.method=="POST":
        form_provincia1=FormularioProvincias(request.POST)
        print(form_provincia1)
        if form_provincia1.is_valid:
            datos_a_basededatos=form_provincia1.cleaned_data
            provincia=Provincias(
                codigo=datos_a_basededatos['codigo'],
                nombre=datos_a_basededatos['nombre'],
                zona=datos_a_basededatos['zona'],
                descripcion=datos_a_basededatos['descripcion'])
            provincia.save()
            return redirect('AppblogFormularioProvincias')
    else:
        form_provincia1=FormularioProvincias()
    
    contexto={
        'formulario_provincia':form_provincia1,
    }
    return render(request,'formulario_provincias.html',contexto)

def formulario_actividades(request):
    if request.method=="POST":
        form_actividad1=FormularioActividades(request.POST)
        print(form_actividad1)
        if form_actividad1.is_valid:
            datos_a_basededatos=form_actividad1.cleaned_data
            actividad=Actividades(
                codigo=datos_a_basededatos['codigo'],
                nombre=datos_a_basededatos['nombre'],
                descripcion=datos_a_basededatos['descripcion'])
            actividad.save()
            return redirect('AppblogFormularioActividades')
    else:
        form_actividad1=FormularioActividades()
    
    contexto={
        'formulario_actividad':form_actividad1,
    }
    return render(request,'formulario_actividades.html',contexto)

def formulario_usuarios(request):
    if request.method=="POST":
        form_usuario1=FormularioUsuarios(request.POST)
        print(form_usuario1)
        if form_usuario1.is_valid:
            datos_a_basededatos=form_usuario1.cleaned_data
            usuario=Usuarios(
                nombre=datos_a_basededatos['nombre'],
                apellido=datos_a_basededatos['apellido'],
                email=datos_a_basededatos['email'],
                edad=datos_a_basededatos['edad'])
            usuario.save()
            return redirect('AppblogFormularioUsuarios')
    else:
        form_usuario1=FormularioUsuarios()
    
    contexto={
        'formulario_usuario':form_usuario1,
    }
    return render(request,'formulario_usuarios.html',contexto)

def formulario_experiencias(request):
    if request.method=='POST':
        form_experiencia1=FormularioExperiencias(request.POST)
        print(form_experiencia1)
        if form_experiencia1.is_valid:
            datos_a_basededatos=form_experiencia1.cleaned_data
            experiencia=Experiencias(
                codigo_actividad=datos_a_basededatos['codigo_actividad'],
                codigo_provincia=datos_a_basededatos['codigo_provincia'],
                email_usuario=datos_a_basededatos['email_usuario'],
                experiencia=datos_a_basededatos['experiencia'],
                fecha_experiencia=datos_a_basededatos['fecha_experiencia'])
            experiencia.save()
            return redirect('AppblogFormularioExperiencias')
    else:
        form_experiencia1=FormularioExperiencias()
    
    contexto={
        'formulario_experiencia':form_experiencia1,
    }
    return render(request,'formulario_experiencias.html',contexto)