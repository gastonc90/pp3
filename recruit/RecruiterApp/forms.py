
from django.forms import ModelForm
from .models import SolicitudDePosicion


class PosicionForm(ModelForm):
	class Meta:
		model = SolicitudDePosicion
		fields = '__all__'


class ManagerPosicionForm(ModelForm):
	class Meta:
		model = SolicitudDePosicion
		fields = ['puesto', 'estado', 'nota']
