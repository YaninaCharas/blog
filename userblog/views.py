from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.info(request, 'Inicio de sesion satisfactorio!')

            else:
                messages.info(request, 'inicio de sesion fallido!')
        else:
            messages.info(request, 'inicio de sesion fallido!')

        return redirect('AppBlogInicio')

    contexto = {
        'form': AuthenticationForm(),
    }
    return render(request, 'login.html', contexto)


def register(request):
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        #form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.info(request, 'Tu usuario fue registrado satisfactoriamente!')
        else:
            messages.info(request, 'Tu usuario no puso ser registrado!')
        return redirect('AppBloginicio')

    contexto = {
         'form': UserCreationForm(),
        'nombre_form' : 'Registro'
        #'form': UserRegisterForm()
    }

    return render(request, 'userblog/login.html', contexto)
