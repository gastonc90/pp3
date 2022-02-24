from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string



@receiver(post_save, sender=SolicitudDePosicion)
def crear_solicitud(sender, instance, created, **kwargs):

    puesto = instance
    id = instance.id
    empresa = instance.empresas
    seniority = instance.seniority
    estado = instance.estado
    etapa = instance.etapa
    resolucion = instance.resolucion
    archivos = instance.cargar_archivos

    contexto = {'puesto':puesto, 'id':id, 'empresa':empresa, 'seniority':empresa,
                'estado':estado, 'nueva_etapa':etapa, 'archivos':archivos}

    recruiter = DepartamentoRecruiter.objects.all()
    mail_recruiter = recruiter[0]
    administracion = DepartamentoAdministracion.objects.all()
    mail_administracion = administracion[0]


    if created:
        try:
            template = render_to_string('Email/email_solicitud.html', contexto)

            email = EmailMessage(
            'Notificación de nueva solicitud de puesto',
            template,
            settings.EMAIL_HOST_USER,
            [mail_recruiter, mail_administracion]

            )

            email.fail_silently='False'
            email.send()

        except Exception as e:
            raise e

    else:
        try:

            def EstadoEtapa():
                template = render_to_string('Email/email_etapa.html', contexto)

                email = EmailMessage(
                    'Notificación de nueva solicitud de Etapa',
                    template,
                    settings.EMAIL_HOST_USER,
                    [mail_recruiter, mail_administracion]

                    )
                email.fail_silently='False'
                email.send()
                print("enviado entrevista")


            if etapa == 'Entrevista':
                EstadoEtapa()
            if etapa == 'Administracion':
                EstadoEtapa()
            if etapa == 'Ingresado':
                EstadoEtapa()
            if etapa == 'Descartado':
                EstadoEtapa()




            else:
                print("algonofunca")

            # if estado == 'Administracion':
            #
            #     template = render_to_string('Email/email_estado.html', contexto)


        except Exception as e:
                print(e)
