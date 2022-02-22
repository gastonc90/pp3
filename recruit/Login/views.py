from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import NuevoUsuario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from .decorator import usuario_no_autenticado
# Create your views here.




@usuario_no_autenticado
def RegistroUsuario(request):
    form = NuevoUsuario()
    if request.method == 'POST':
        form = NuevoUsuario(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages = success(request, 'Cuenta creada para' + user)
            redirect ('login')

    contexto = {'form':form}
    return render(request, 'Login/registro.html', contexto)




@usuario_no_autenticado
def PaginaLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, 'Ingrese usuario y contraseña para iniciar sesión')
                return redirect('base')
            else:
                messages.error(request, 'Nombre o contraseña incorrecta')
        else:
            messages.error(request, 'Nombre o contraseña incorrecta')

    form = AuthenticationForm()
    contexto = {'form':form}

    return render(request, 'Login/login.html', contexto )




def PaginaLogout(request):
    logout(request)
    return redirect('login')
