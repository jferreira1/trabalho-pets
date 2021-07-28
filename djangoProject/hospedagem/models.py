from django.db import models
from django.contrib.auth.models import User


class Hospedagem(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    valor_diaria = models.FloatField()
    foto = models.CharField(max_length=500, null=True)
    locatario = models.ManyToManyField(User, through='ReservaHospedagem')

    def __str__(self):
        return f'{self.nome}'


class ReservaHospedagem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospedagem = models.ForeignKey(Hospedagem, on_delete=models.CASCADE)
    valor_total = models.FloatField()
    data_reserva = models.DateField(null=True)
