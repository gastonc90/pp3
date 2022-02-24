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





class DepartamentoRecruiter(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=30, default='')


    def __str__(self):
    	return self.email




class DepartamentoGerencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=30, default='')

    def __str__(self):
    	return self.email




class DepartamentoAdministracion(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=30, default='')


    def __str__(self):
    	return self.email




class Managers(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30, default='nombre', null=True)
    usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL )
    apellido = models.CharField(max_length=30, default='apellido', null=True)
    direccion = models.CharField(max_length=30, default='direccion', null=True)
    email = models.EmailField(max_length=30, default='email')
    empresa = models.ForeignKey(Empresas, null=True, on_delete=models.SET_NULL )

    def __str__(self):
	       return self.nombre




class Puestos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_puesto = models.CharField(max_length=30)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_validacion = models.DateTimeField(auto_now_add=False)



    def __str__(self):
        return self.nombre_puesto





class SolicitudDePosicion(models.Model):
    id = models.BigAutoField(primary_key=True)

    STATUS = (('Aprobado', 'Aprobado'),
                ('Esperando', 'Esperando'),
                ('Denegado', 'Denegado'),
    )

    ETAPAS = (('Administracion', 'Administracion'),
                ('Aprobacion', 'Aprobacion'),
                ('Entrevista','Entrevista'),
                
    )

    SENIORITY = (('Junior', 'Junior'),
                ('Semi Senior', 'Semi Senior'),
                ('Senior','Senior'),
                ('Gerente','Gerente'),
    )

    RESOLUCION = (('Ingresado','Ingresado'),
                ('Descartado','Descartado'),

    )


    manager = models.ForeignKey(Managers, null=True, on_delete=models.SET_NULL)
    puesto = models.ForeignKey(Puestos, null=True, on_delete=models.SET_NULL)
    empresas = models.ForeignKey(Empresas, null=True, on_delete=models.SET_NULL)
    fecha_de_carga = models.DateTimeField(auto_now_add=True, null=True)
    estado = models.CharField(max_length=30, default='Esperando', choices=STATUS)
    etapa = models.CharField(max_length=30, default='Aprobacion', null=True, choices=ETAPAS)
    resolucion = models.CharField(max_length=30, default='En Proceso', null=True, choices=RESOLUCION)
    seniority = models.CharField(max_length=30, null=True, choices=SENIORITY)
    nota = models.TextField(max_length=300, default='Escriba información breve de utilidad en torno a la posición')
    cargar_archivos = models.FileField(upload_to="media/", null=True, blank=True)
    nombre = models.CharField(max_length=30, default='nombre', null=True)
    apellido = models.CharField(max_length=30, default='apellido', null=True)
    direccion = models.CharField(max_length=30, default='direccion', null=True)
    email = models.EmailField(max_length=30, default='email@mail.com', null=True)


    def __str__(self):
	       return self.puesto.nombre_puesto
