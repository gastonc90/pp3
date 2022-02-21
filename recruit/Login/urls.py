from django.urls import path
from Login import views


urlpatterns = [
    path('login', views.PaginaLogin, name='login'),
    path('registro', views.RegistroUsuario, name='registro'),
    path('logout', views.PaginaLogout, name='logout'),

    ]
