from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()

class Empresas(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL )
    nombre_empresa = models.CharField(max_length=30)
    nombre_manager = models.CharField(max_length=30)
    telefono = models.FloatField(default=0)
    email = models.EmailField(max_length=30, default='')

    def __str__(self):
        return self.nombre_empresa



class Puestos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_puesto = models.CharField(max_length=30)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_validacion = models.DateTimeField(auto_now_add=False)



    def __str__(self):
        return self.nombre_puesto



class Archivos(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    archivo_cargado = models.FileField(upload_to="media/")
    fecha_de_carga = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo




class SolicitudDePosicion(models.Model):
    id = models.BigAutoField(primary_key=True)

    STATUS = (('Aprobado', 'Aprobado'),
                ('Esperando', 'Esperando'),
                ('Denegado', 'Denegado'),
    )

    ETAPAS = (('Administracion', 'Administracion'),
                ('Aprobacion', 'Aprobacion'),
                ('Entevista','Entrevista'),
    )

    puesto = models.ForeignKey(Puestos, null=True, on_delete=models.SET_NULL)
    empresas = models.ForeignKey(Empresas, null=True, on_delete=models.SET_NULL)
    fecha_de_carga = models.DateTimeField(auto_now_add=True, null=True)
    estado = models.CharField(max_length=30, null=True, choices=STATUS)
    etapa = models.CharField(max_length=30, null=True, choices=ETAPAS)

    def __str__(self):
	       return self.puesto.nombre_puesto
