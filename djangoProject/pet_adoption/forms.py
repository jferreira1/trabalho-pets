from django.forms import ModelForm
from .models import Pet


class PetAdoptionForm(ModelForm):
    class Meta:
        model = Pet
        fields = ['data_adocao']
