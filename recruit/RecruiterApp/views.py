from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import PosicionForm, ManagerPosicionForm, FormularioIngreso, FormularioManager
from .filters import FiltroPosicion
from django.contrib.auth.decorators import login_required
from Login.decorator import vistas_autorizadas

# Create your views here.

@login_required(login_url='login')
def base(request):
    return render(request,'RecruiterApp/base.html')





#Dashboard principal del Manager, ver solicitudes de posicion de su empresa.
@login_required(login_url='login')
@vistas_autorizadas(allowed_roles=['managers', 'admin'])
def SolicitudAlta(request):
    # empresas = request.user.empresas_set.all()
    # solicitudes = empresas[0].solicituddeposicion_set.all()

    try:
        empresas = request.user.empresas_set.all()
        empresa = empresas[0]
        solicitudes = empresas[0].solicituddeposicion_set.all()
    except Exception as e:
        empresa = None
        solicitudes = None

    contexto = {'solicitudes':solicitudes, 'empresa':empresa}
    return render(request, 'RecruiterApp/carga_ternas.html', contexto)



#Crear posicion del Manager
@login_required(login_url='login')
@vistas_autorizadas(allowed_roles=['managers'])
def SolicitudManager(request):

    form = FormularioManager()
    if request.method == 'POST':
        form = FormularioManager(request.POST)
        if form.is_valid():
            form.save()
            return redirect('solicitud_alta')

    contexto = {'form':form}
    return render(request, 'RecruiterApp/posicion_manager.html', contexto)



#Dashboard principal del Gerente, ver solicitudes de posicion por empresa.
@login_required(login_url='login')
@vistas_autorizadas(allowed_roles=['admin'])
def ListarEmpresas(request, pk):
    empresas = Empresas.objects.get(id=pk)
    solicitudes = empresas.solicituddeposicion_set.all()
    total_solicitudes = solicitudes.count()

    filtros = FiltroPosicion(request.GET, queryset=solicitudes)
    solicitudes = filtros.qs

    contexto = {'empresas':empresas, 'solicitudes':solicitudes, 'total_solicitudes':total_solicitudes, 'filtros':filtros}
    return render(request, 'RecruiterApp/empresas.html', contexto)



#Dashboard principal del Gerente
@login_required(login_url='login')
@vistas_autorizadas(allowed_roles=['admin'])
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
@login_required(login_url='login')
@vistas_autorizadas(allowed_roles=['recruiter','admin'])
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
@login_required(login_url='login')
@vistas_autorizadas(allowed_roles=['recruiter','admin'])
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
@login_required(login_url='login')
@vistas_autorizadas(allowed_roles=['recruiter','admin'])
def ActualizarPosicion(request, pk):
    posicion_id = SolicitudDePosicion.objects.get(id=pk)
    form = PosicionForm(instance=posicion_id)

    if request.method == 'POST':
        form = PosicionForm(request.POST, request.FILES, instance=posicion_id)
        if form.is_valid():
            form.save()
            return redirect('dashboard_gerencia')

    contexto = {'form':form}
    return render(request, 'RecruiterApp/crear_posicion.html', contexto)



#Vista del recruiter
@login_required(login_url='login')
@vistas_autorizadas(allowed_roles=['recruiter','admin'])
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
@login_required(login_url='login')
@vistas_autorizadas(allowed_roles=['recruiter','admin'])
def EliminarPosicion(request, pk):
    posicion_id = SolicitudDePosicion.objects.get(id=pk)

    if request.method == 'POST':
        posicion_id.delete()
        return redirect('base')

    contexto = {'posicion':posicion_id}
    return render(request, 'RecruiterApp/eliminar.html', contexto)



#Gestionar solicitudes en Administración
@login_required(login_url='login')
@vistas_autorizadas(allowed_roles=['administracion','admin'])
def GestionarAdministracion(request):

    empresas = Empresas.objects.all()
    solicitud_posicion = SolicitudDePosicion.objects.filter(etapa='Administracion')

    total_posiciones = solicitud_posicion.count()

    aprobadas = solicitud_posicion.filter(estado='Aprobado').count()
    espera = solicitud_posicion.filter(estado='Esperando').count()
    denegadas = solicitud_posicion.filter(estado='Denegado').count()

    contexto = {'empresas':empresas, 'solicitud_posicion':solicitud_posicion,
    'total_posiciones':total_posiciones, 'aprobadas':aprobadas, 'espera':espera, 'denegadas':denegadas}
    return render(request, 'RecruiterApp/administracion.html', contexto)


#Ingresar personal
@login_required(login_url='login')
@vistas_autorizadas(allowed_roles=['administracion','admin'])
def FormularioIngresos(request, pk):

    solicitud = SolicitudDePosicion.objects.get(id=pk)
    form = FormularioIngreso(instance=solicitud)

    if request.method == 'POST':
        form = FormularioIngreso(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            return redirect('administracion')

    contexto = {'form':form}
    return render(request,'RecruiterApp/ingresos.html', contexto)
