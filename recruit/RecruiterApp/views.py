from django.shortcuts import render, redirect, get_object_or_404
from RecruiterApp.models import *
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
