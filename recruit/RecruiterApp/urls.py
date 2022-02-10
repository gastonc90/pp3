from django.urls import path
from RecruiterApp import views


urlpatterns = [
    path('', views.base, name='base'),
    path('solicitud_alta', views.nueva_posicion, name='solicitud_alta'),
    path('estado_busqueda_gerencia', views.estado_busqueda_gerencia, name='estado_busqueda_gerencia'),
    path('crear_posicion', views.CrearPosicion, name='crear_posicion'),
    path('actualizar_posicion/<str:pk>/', views.ActualizarPosicion, name='actualizar_posicion'),
    path('eliminar/<str:pk>/', views.EliminarPosicion, name='eliminar'),
    path('ver_empresa', views.VerEmpresa, name='ver_empresa'),
]
