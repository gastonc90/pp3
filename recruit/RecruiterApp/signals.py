from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string



@receiver(post_save, sender=SolicitudDePosicion)
def crear_solicitud(sender, instance, created, **kwargs):


    contexto = {'instance':instance}


    recruiter = DepartamentoRecruiter.objects.all()
    mail_recruiter = recruiter[0]
    administracion = DepartamentoAdministracion.objects.all()
    mail_administracion = administracion[0]


    template_solicitud = render_to_string('Email/email_solicitud.html', contexto)
    template_estado = render_to_string('Email/email_estado.html', contexto)
    template_etapa = render_to_string('Email/email_etapa.html', contexto)
    template_resolucion = render_to_string('Email/email_resolucion.html', contexto)



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
            def Etapa(template_etapa):
                template = render_to_string('Email/email_etapa.html', contexto)

                email = EmailMessage(
                    'Notificación de nueva solicitud de etapa',
                    template_etapa,
                    settings.EMAIL_HOST_USER,
                    [mail_recruiter, mail_administracion]

                    )
                email.fail_silently='False'
                email.send()
                print("enviado entrevista")

            if etapa == 'Entrevista':
                Etapa(template_etapa)
            if etapa == 'Administracion':
                Etapa(template_etapa)

            if estado == 'Aprobado' and etapa == 'Aprobacion':
                    print("llegue al aprobado")
                    email = EmailMessage(
                            'Notificación de nueva solicitud de estado',
                            template_estado,
                            settings.EMAIL_HOST_USER,
                            [mail_recruiter, mail_administracion]

                            )
                    email.fail_silently='False'
                    email.send()
            if estado == 'Denegado' and etapa == 'Aprobacion':
                    email = EmailMessage(
                            'Notificación de nueva solicitud de estado',
                            template_estado,
                            settings.EMAIL_HOST_USER,
                            [mail_recruiter, mail_administracion]

                            )
                    email.fail_silently='False'
                    email.send()

        except Exception as e:
                print(e)
