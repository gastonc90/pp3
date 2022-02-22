import django_filters
from .models import *



#Filtro del buscador
class FiltroPosicion(django_filters.FilterSet):
    class Meta:
        model = SolicitudDePosicion
        filter = '__all__'
        exclude = ['fecha_de_carga', 'nota', 'cargar_archivos', 'nombre', 'apellido', 'direccion', 'email']
