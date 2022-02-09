from django.urls import path
from RecruiterApp import views


urlpatterns = [
    path('', views.base, name='base'),
    path('solicitud_alta', views.nueva_posicion, name='solicitud_alta'),
    path('estado_busqueda_gerencia', views.estado_busqueda_gerencia, name='estado_busqueda_gerencia'),
]
