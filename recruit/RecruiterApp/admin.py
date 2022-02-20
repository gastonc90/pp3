from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Puestos)
admin.site.register(Empresas)
admin.site.register(SolicitudDePosicion)
admin.site.register(Managers)
