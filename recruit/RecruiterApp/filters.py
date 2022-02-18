import django_filters
from .models import *



#Filtro del buscador
class FiltroPosicion(django_filters.FilterSet):
    class Meta:
        model = SolicitudDePosicion
        filter = '__all__'
        exclude = ['empresas', 'fecha_de_carga', 'nota']
