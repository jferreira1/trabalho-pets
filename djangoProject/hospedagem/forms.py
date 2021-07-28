from django.forms import ModelForm, DateInput
from .models import ReservaHospedagem


class ReservaHospedagemForm(ModelForm):
    class Meta:
        model = ReservaHospedagem
        fields = ['data_reserva']
