
from django.forms import ModelForm
from .models import SolicitudDePosicion
from django.forms import ClearableFileInput


class PosicionForm(ModelForm):
	class Meta:
		model = SolicitudDePosicion
		fields = '__all__'
		widgets = {
			'cargar_archivos':ClearableFileInput(attrs={'multiple':True}),
		}


class ManagerPosicionForm(ModelForm):
	class Meta:
		model = SolicitudDePosicion
		fields = ['puesto', 'estado', 'nota']



#class CargaArchivos(ModelForm):
	#class Meta:
		#model = SolicitudDePosicion
		#fields = ['cargar_archivos']
		#widgets = {
			#'cargar_archivos':ClearableFileInput(attrs={'multiple':True}),
		#}
