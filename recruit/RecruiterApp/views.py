from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import PosicionForm, ManagerPosicionForm, FormularioIngreso, FormularioManager
from .filters import FiltroPosicion
from django.contrib.auth.decorators import login_required
from Login.decorator import vistas_autorizadas
import csv
from django.utils import timezone
from datetime import datetime
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile


# Create your views here.

@login_required(login_url='login')
def base(request):

    empresas = Empresas.objects.all()
    solicitud_posicion = SolicitudDePosicion.objects.all()

    total_solicitudes = solicitud_posicion.count()

    aprobadas = solicitud_posicion.filter(estado='Aprobado').count()
    espera = solicitud_posicion.filter(estado='Esperando').count()
    denegadas = solicitud_posicion.filter(estado='Denegado').count()
    ingresados = solicitud_posicion.filter(resolucion='Ingresado').count()
    junior = solicitud_posicion.filter(seniority='Junior').count()
    semi_senior = solicitud_posicion.filter(seniority='Semi Senior').count()
    senior = solicitud_posicion.filter(seniority='Senior').count()
    gerente = solicitud_posicion.filter(seniority='Gerente').count()
    etapa_administracion = solicitud_posicion.filter(etapa='Administracion').count()
    etapa_aprobacion = solicitud_posicion.filter(etapa='Aprobacion').count()
    etapa_entrevista = solicitud_posicion.filter(etapa='Entrevista').count()



    contexto = {'aprobadas':aprobadas,'denegadas':denegadas,
                'total_solicitudes':total_solicitudes, 'ingresados':ingresados,
                'junior':junior, 'semi_senior':semi_senior, 'senior':senior,
                'gerente':gerente, 'etapa_administracion':etapa_administracion,
                'etapa_aprobacion':etapa_aprobacion, 'etapa_entrevista':etapa_entrevista}
    return render(request,'RecruiterApp/base.html', contexto)





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
        total_solicitudes = solicitudes.count()
        sol_aprob = solicitudes.filter(estado='Aprobado').count()
        sol_den = solicitudes.filter(estado='Denegado').count()
        sol_esp = solicitudes.filter(estado='Espera').count()


    except Exception as e:
        empresa = None
        solicitudes = None
        total_solicitudes = None
        sol_aprob = None
        sol_den = None
        sol_esp = None

    contexto = {'solicitudes':solicitudes, 'empresa':empresa,
                'total_solicitudes':total_solicitudes, 'sol_aprob':sol_aprob,
                 'sol_den':sol_den, 'sol_esp':sol_esp}
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

    contexto = {'empresas':empresas, 'solicitudes':solicitudes, 'total_solicitudes':total_solicitudes,
     'filtros':filtros}
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
                'total_posiciones':total_posiciones, 'empresas':empresas, 'aprobadas':aprobadas,
                'espera':espera, 'denegadas':denegadas}

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



#Gestionar solicitudes en Administraci??n
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
                'total_posiciones':total_posiciones, 'aprobadas':aprobadas,
                'espera':espera, 'denegadas':denegadas}

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


#Exportar CSV
@login_required(login_url='login')
@vistas_autorizadas(allowed_roles=['administracion','admin'])
def exportar_csv(request):
    solicitudes = SolicitudDePosicion.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-disposition'] = 'attachment; filename=reporte_recruiterapp' + \
    str(datetime.now())+'.csv'

    writer = csv.writer(response)
    writer.writerow(['ID','POSICION','EMPRESA','FECHA_ORDEN','ESTADO','ETAPA','RESOLUCION'])

    for solicitud in solicitudes:
        writer.writerow([solicitud.id,solicitud.puesto,solicitud.empresas,solicitud.fecha_de_carga,
                        solicitud.estado,solicitud.etapa,solicitud.resolucion])

    return response


@login_required(login_url='login')
@vistas_autorizadas(allowed_roles=['administracion','admin'])
def pdf_administracion(request):

    empresas = Empresas.objects.all()
    solicitud_posicion = SolicitudDePosicion.objects.filter(etapa='Administracion')


    contexto = {'empresas':empresas, 'solicitud_posicion':solicitud_posicion}

    response = HttpResponse(content_type='text/pdf')
    response['Content-disposition'] = 'inline; attachment; filename=reporte_recruiterapp_pdf' + \
    str(datetime.now())+'.pdf'


    response['Content-transfer-encoding'] = 'binary'
    html_string = render_to_string('RecruiterApp/pdf_administracion.html',contexto)
    html = HTML(string=html_string)
    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

        return response
