from django.urls import path
from RecruiterApp import views


urlpatterns = [
    path('', views.base, name='base'),
    path('posiciones', views.SolicitudAlta, name='posiciones'),
    path('empresas/<str:pk>/', views.ListarEmpresas, name='empresas'),
    path('dashboard_gerencia', views.DashboardGerencia, name='dashboard_gerencia'),
    path('crear_posicion', views.CrearPosicion, name='crear_posicion'),
    path('actualizar_posicion/<str:pk>/', views.ActualizarPosicion, name='actualizar_posicion'),
    path('solicitud_alta', views.SolicitudAlta, name='solicitud_alta'),
    path('eliminar/<str:pk>/', views.EliminarPosicion, name='eliminar'),
]
