from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string



@receiver(post_save, sender=SolicitudDePosicion)
def crear_solicitud(sender, instance, created, **kwargs):

    if created:
        try:

            puesto = instance
            id = instance.id
            empresa = instance.empresas
            seniority = instance.seniority

            contexto = {'puesto':puesto, 'id':id, 'empresa':empresa, 'seniority':empresa}

            recruiter = DepartamentoRecruiter.objects.all()
            mail_recruiter = recruiter[0]
            administracion = DepartamentoAdministracion.objects.all()
            mail_administracion = administracion[0]

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

            puesto = instance
            id = instance.id
            print(id)
            empresa = instance.empresas
            seniority = instance.seniority
            estado = instance.estado
            print(estado)
            etapa = instance.etapa
            print(etapa)
            resolucion = instance.resolucion

            contexto = {'puesto':puesto, 'id':id, 'empresa':empresa, 'seniority':empresa,
            'estado':estado, 'nueva_etapa':etapa}

            recruiter = DepartamentoRecruiter.objects.all()
            mail_recruiter = recruiter[0]
            administracion = DepartamentoAdministracion.objects.all()
            mail_administracion = administracion[0]

            if etapa == 'Entrevista':

                template = render_to_string('Email/email_estado.html', contexto)

                email = EmailMessage(
                'Notificación de nueva solicitud de puesto',
                template,
                settings.EMAIL_HOST_USER,
                [mail_recruiter, mail_administracion]

                )

                email.fail_silently='False'
                email.send()
            else:
                print("no ha pasado nada")

        except Exception as e:
                print(e)








        except Exception as e:
            raise
