from django.urls import path
from RecruiterApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.base, name='base'),
    path('posiciones', views.SolicitudAlta, name='posiciones'),
    path('empresas/<str:pk>/', views.ListarEmpresas, name='empresas'),
    path('dashboard_gerencia', views.DashboardGerencia, name='dashboard_gerencia'),
    path('crear_posicion', views.CrearPosicion, name='crear_posicion'),
    path('actualizar_posicion/<str:pk>/', views.ActualizarPosicion, name='actualizar_posicion'),
    path('solicitud_alta', views.SolicitudAlta, name='solicitud_alta'),
    path('eliminar/<str:pk>/', views.EliminarPosicion, name='eliminar'),
    path('carga_ternas/', views.ManagerPosicion, name='carga_ternas'),
    path('recruiter/', views.RecruiterTool, name='recruiter'),
    path('administracion/', views.GestionarAdministracion, name='administracion'),
    path('ingresos/<str:pk>/', views.FormularioIngresos, name='ingresos'),
    path('posicion_manager/', views.SolicitudManager, name='posicion_manager'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
