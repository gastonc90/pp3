
from django.forms import ModelForm
from .models import SolicitudDePosicion


class PosicionForm(ModelForm):
	class Meta:
		model = SolicitudDePosicion
		fields = '__all__'
