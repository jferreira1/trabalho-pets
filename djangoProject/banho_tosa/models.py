from django.db import models
from django.contrib.auth.models import User


class Estabelecimento(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    valor = models.FloatField()
    foto = models.CharField(max_length=500, null=True)
    contratante = models.ManyToManyField(User, through='ReservaEstabelecimento')

    def __str__(self):
        return f'{self.nome}'


class ReservaEstabelecimento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    valor_total = models.FloatField()
    agendamento = models.DateField(null=True)
