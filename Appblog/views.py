from django.shortcuts import render


# Create your views here.
def inicio(request):
    return render(request, "index.html")

from Appblog.models import Provincias


def provincias(request):
    provincia1 = provincias(nombre="Buenos Aires", zona="Centro", codigo=1, descripcion="Zona central cerca de la capital federal")
    provincia1.save()
    contexto = {
        'provincia': provincia1
    }

    return render (request, 'experiencias.html', contexto)