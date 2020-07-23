from django.db import models
from django.utils import timezone
import datetime


class Paciente(models.Model):
    class Tipo_Teste(models.TextChoices):
        opcao1 = "1","RT-PCR"
        opcao2 = "2","Sorologia"
        opcao3 = "3","Teste Rápido - Antígenos"
        opcao4 = "4","Teste Rápido - Anticorpos"
    
    tipo = models.CharField(
        max_length=100,
        choices=Tipo_Teste.choices,
    )
    nome = models.CharField(max_length=100)

    resultado = models.BooleanField()
    data = models.DateTimeField('Data de Nascimento')   


    def __str__(self):
        return self.nome
