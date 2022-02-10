from django.shortcuts import render, redirect
from django.http import HttpResponse
from RecruiterApp.models import *
from .forms import PosicionForm
# Create your views here.


def base(request):
    return render(request,'RecruiterApp/base.html')


def nueva_posicion(request):
    #if request.method == 'POST':
        #posicion = request.POST["agregar_posicion"]
        #posiciones_agregadas = Puestos(nombre_puesto = posicion, estado = 'espera', etapa = 'aprobacion' )
        #posiciones_agregadas.save()
    return render(request, 'RecruiterApp/solicitud_alta.html')


def eliminar_posicion(request, id):
    #puesto = get_object_or_404(Puestos, id=id)
    #puesto.delete()
    return render(request, 'RecruiterApp/solicitud_alta.html')



def estado_busqueda_gerencia(request):
    empresas = Empresas.objects.all()
    solicitud_posicion = SolicitudDePosicion.objects.all()

    total_posiciones = solicitud_posicion.count()

    aprobadas = solicitud_posicion.filter(estado='Aprobado').count()
    espera = solicitud_posicion.filter(estado='Esperando').count()
    denegadas = solicitud_posicion.filter(estado='Denegado').count()

    contexto = {'solicitud_posicion':solicitud_posicion,
    'total_posiciones':total_posiciones, 'aprobadas':aprobadas,
    'denegadas':denegadas, 'espera':espera, 'empresas':empresas}


    return render(request, 'RecruiterApp/estado_busqueda_gerencia.html',contexto)




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



def VerEmpresa(request):
    if request.method == 'POST':
        pass
    return render(request, 'RecruiterApp/ver_empresa.html')
