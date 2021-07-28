from django.forms import ModelForm
from .models import ReservaEstabelecimento


class ReservaHospedagemForm(ModelForm):
    class Meta:
        model = ReservaEstabelecimento
        fields = ['agendamento']
