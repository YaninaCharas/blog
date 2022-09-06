from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

# Create your views here.
def login_request(request):
    # if request.method == "POST":
    #     form = AuthenticationForm(request, data=request.POST)
    #
    #     if [form.is](http://form.is)_valid():
    #         data = form.cleaned_data
    #
    #         usuario = data.get('username')
    #         contrasenia = data.get('password')
    #
    #         user = authenticate(username=usuario, password=contrasenia)
    #
    #         if user:
    #             login(request, user)
    #             [messages.info](http://messages.info)(request, 'Inicio de sesion satisfactorio!')
    #
    #         else:
    #             [messages.info](http://messages.info)(request, 'inicio de sesion fallido!')
    #     else:
    #         [messages.info](http://messages.info)(request, 'inicio de sesion fallido!')
    #
    #     return redirect('AppCoderInicio')

    contexto = {
        'form': AuthenticationForm(),
    }
    return render(request, 'userblog/login.html', contexto)