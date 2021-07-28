from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    nome = models.CharField(max_length=50)
    especie = models.CharField(max_length=25)
    idade = models.IntegerField()
    foto = models.CharField(max_length=500, null=True)
    video = models.CharField(max_length=500, null=True)
    data_adocao = models.DateField(null=True)
    dono = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nome}'
