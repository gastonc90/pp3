from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import PosicionForm, ManagerPosicionForm
from .filters import FiltroPosicion
# Create your views here.


def base(request):
    return render(request,'RecruiterApp/base.html')





#Dashboard principal del Manager, ver solicitudes de posicion de su empresa.

def SolicitudAlta(request):

    return render(request, 'RecruiterApp/solicitud_alta.html')



#Dashboard principal del Gerente, ver solicitudes de posicion por empresa.

def ListarEmpresas(request, pk):
    empresas = Empresas.objects.get(id=pk)
    solicitudes = empresas.solicituddeposicion_set.all()
    total_solicitudes = solicitudes.count()

    filtros = FiltroPosicion(request.GET, queryset=solicitudes)
    solicitudes = filtros.qs

    contexto = {'empresas':empresas, 'solicitudes':solicitudes, 'total_solicitudes':total_solicitudes, 'filtros':filtros}
    return render(request, 'RecruiterApp/empresas.html', contexto)



#Dashboard principal del Gerente

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



#Crear todas las posiciones (Dashboard Gerente)

def CrearPosicion(request):
    form = PosicionForm()

    if request.method == 'POST':
        form = PosicionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    contexto = {'form':form}
    return render(request, 'RecruiterApp/crear_posicion.html', contexto)


#Crear posiciones Manager)

def ManagerPosicion(request):
    form = ManagerPosicionForm()

    if request.method == 'POST':
        form = ManagerPosicionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    contexto = {'form':form}
    return render(request, 'RecruiterApp/carga_ternas.html', contexto)



#Actualizar posiciones (Gerente)

def ActualizarPosicion(request,pk):
    posicion_id = SolicitudDePosicion.objects.get(id=pk)
    form = PosicionForm(instance=posicion_id)

    if request.method == 'POST':
        form = PosicionForm(request.POST, instance=posicion_id)
        if form.is_valid():
            form.save()
            return redirect('dashboard_gerencia')

    contexto = {'form':form}
    return render(request, 'RecruiterApp/crear_posicion.html', contexto)



#Vista del recruiter
def RecruiterTool(request):
    empresas = Empresas.objects.all()
    solicitud_posicion = SolicitudDePosicion.objects.filter(etapa='Entrevista')

    total_posiciones = solicitud_posicion.count()

    aprobadas = solicitud_posicion.filter(estado='Aprobado').count()
    espera = solicitud_posicion.filter(estado='Esperando').count()
    denegadas = solicitud_posicion.filter(estado='Denegado').count()

    contexto = {'solicitud_posicion':solicitud_posicion,
    'total_posiciones':total_posiciones, 'empresas':empresas, 'aprobadas':aprobadas, 'espera':espera, 'denegadas':denegadas}

    return render(request, 'RecruiterApp/recruiter.html', contexto)



#Eliminar posiciones

def EliminarPosicion(request, pk):
    posicion_id = SolicitudDePosicion.objects.get(id=pk)

    if request.method == 'POST':
        posicion_id.delete()
        return redirect('base')

    contexto = {'posicion':posicion_id}
    return render(request, 'RecruiterApp/eliminar.html', contexto)
