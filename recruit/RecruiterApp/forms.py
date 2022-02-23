
from django.forms import ModelForm
from .models import SolicitudDePosicion
from django.forms import ClearableFileInput



class PosicionForm(ModelForm):
	class Meta:
		model = SolicitudDePosicion
		fields = ['puesto', 'empresas', 'estado', 'etapa', 'seniority', 'nota', 'cargar_archivos']
		widgets = {
			'cargar_archivos':ClearableFileInput(attrs={'multiple':True}),
		}



class ManagerPosicionForm(ModelForm):
	class Meta:
		model = SolicitudDePosicion
		fields = ['puesto', 'estado', 'nota']




class FormularioIngreso(ModelForm):
	class Meta:
		model = SolicitudDePosicion
		fields = ['id','puesto', 'empresas', 'seniority', 'nombre', 'apellido', 'direccion','email', 'resolucion']




class FormularioManager(ModelForm):
	class Meta:
		model = SolicitudDePosicion
		fields = ['empresas','puesto', 'seniority', 'nota']
