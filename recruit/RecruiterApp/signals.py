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
            email_manager=Managers.email
            email_recruiter=DepartamentoRecruiter.email

            template = render_to_string('Email/email_solicitud.html')

            email = EmailMessage(
            'Notificación de nueva solicitud de puesto',
            template,
            settings.EMAIL_HOST_USER,
            ['milagrosrecruiting@gmail.com']

            )

            email.fail_silently='False'
            email.send()

        except Exception as e:
            print(e)
