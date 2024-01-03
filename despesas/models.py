from typing import Any
from django.db import models

from gestaoAluguel.models import Casa, Inquilino

tipo_choices = (
    ('A', 'Água'),
    ('E', 'Energia'),
    ('I', 'Internet'),
    ('M', 'Máquina'),
)


class Despesas(models.Model):
    tipo = models.CharField(max_length=1, choices=tipo_choices)
    identificador = models.CharField(max_length=50)
    data_chegada = models.DateField()
    data_vencimento = models.DateField()
    qtd_pessoas = models.IntegerField()
    valor = models.FloatField()
    valor_por_pessoa = models.FloatField(blank=True, null=True)
    casa = models.ManyToManyField(Casa)
    inquilino = models.ManyToManyField(Inquilino)

    def save(self, *args, **kwargs):
        # Calcula o valor por pessoa antes de salvar
        self.valor_por_pessoa = self.valor / float(self.qtd_pessoas)
        super(Despesas, self).save(*args, **kwargs)
