from django.shortcuts import render, redirect
from django.http import HttpResponse
from RecruiterApp.models import *
from .forms import PosicionForm
from .filters import FiltroPosicion
# Create your views here.


def base(request):
    return render(request,'RecruiterApp/base.html')


def SolicitudAlta(request):
    posiciones = Puestos.objects.all()

    contexto = {'posiciones':posiciones}
    return render(request, 'RecruiterApp/solicitud_alta.html', contexto)


def ListarEmpresas(request, pk):
    empresas = Empresas.objects.get(id=pk)
    solicitudes = empresas.solicituddeposicion_set.all()
    total_solicitudes = solicitudes.count()

    filtros = FiltroPosicion(request.GET, queryset=solicitudes)
    solicitudes = filtros.qs

    contexto = {'empresas':empresas, 'solicitudes':solicitudes, 'total_solicitudes':total_solicitudes, 'filtros':filtros}
    return render(request, 'RecruiterApp/empresas.html', contexto)



def DashboardGerencia(request):
    empresas = Empresas.objects.all()
    solicitud_posicion = SolicitudDePosicion.objects.all()

    total_posiciones = solicitud_posicion.count()

    aprobadas = solicitud_posicion.filter(estado='Aprobado').count()
    espera = solicitud_posicion.filter(estado='Esperando').count()
    denegadas = solicitud_posicion.filter(estado='Denegado').count()

    contexto = {'solicitud_posicion':solicitud_posicion,
    'total_posiciones':total_posiciones, 'aprobadas':aprobadas,
    'denegadas':denegadas, 'espera':espera, 'empresas':empresas}
    return render(request, 'RecruiterApp/dashboard_gerencia.html',contexto)




def CrearPosicion(request):
    form = PosicionForm()

    if request.method == 'POST':
        form = PosicionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    contexto = {'form':form}
    return render(request, 'RecruiterApp/crear_posicion.html', contexto)



def ActualizarPosicion(request,pk):
    posicion_id = SolicitudDePosicion.objects.get(id=pk)
    form = PosicionForm(instance=posicion_id)

    if request.method == 'POST':
        form = PosicionForm(request.POST, instance = posicion_id)
        if form.is_valid():
            form.save()
            return redirect('estado_busqueda_gerencia')

    contexto = {'form':form}
    return render(request, 'RecruiterApp/crear_posicion.html', contexto)



def EliminarPosicion(request, pk):
    posicion_id = SolicitudDePosicion.objects.get(id=pk)

    if request.method == 'POST':
        posicion_id.delete()
        return redirect('base')

    contexto = {'posicion':posicion_id}
    return render(request, 'RecruiterApp/eliminar.html', contexto)
