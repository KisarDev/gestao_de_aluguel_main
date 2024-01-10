from datetime import timedelta
from typing import Any
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import date

from despesas.models import Despesas


class Inquilino(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=25, unique=True)
    rg = models.CharField('Rg', max_length=25, unique=True)
    profissao = models.CharField('Profissão', max_length=40)
    estado_civil = models.CharField("Estado civil", max_length=20)
    telefone = models.CharField('Telefone', max_length=30)
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    identificador_casa = models.ForeignKey('Casa', on_delete=models.CASCADE,
                                           null=True, blank=True)
    despesa = models.ManyToManyField(Despesas)

    def obter_identificador_da_casa(self):
        # Acesse um atributo específico da casa
        return self.casa.identificador

    def __str__(self):
        return self.nome


class Casa(models.Model):
    id = models.AutoField(primary_key=True)
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    identificador = models.CharField(max_length=50)
    representante = models.ForeignKey(Inquilino, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=80)
    valor_aluguel = models.FloatField()
    pago = models.BooleanField(default=False)
    data_ultimo_pagamento = models.DateField()
    data_vencimento_aluguel = models.DateField()
    adiantamento = models.JSONField(blank=True, null=True, default={
                                    "dia_do_adiantamento": "00/00/0000", "valor_do_adiantamento": 0.0})
    despesa = models.ManyToManyField(Despesas)

    def calcular_data_de_vencimento(self):
        data_de_hoje = date.today()

        if self.data_ultimo_pagamento > self.data_vencimento_aluguel:
            self.pago = False

            novo_vencimento = self.data_ultimo_pagamento + timedelta(days=30)

            ultimo_dia_do_mes = timezone.datetime(
                self.data_ultimo_pagamento.year, self.data_ultimo_pagamento.month, 1) + timedelta(days=31)
            if novo_vencimento >= ultimo_dia_do_mes.date():
                novo_vencimento = ultimo_dia_do_mes.date() - timedelta(days=1)

            self.data_vencimento_aluguel = novo_vencimento
            self.save()
        else:
            self.pago = True
            self.save()

        if data_de_hoje > self.data_vencimento_aluguel:
            self.pago = False
            self.save()

    def __str__(self):
        return str(self.identificador)


class Contrato(models.Model):
    inquilino = models.ForeignKey(Inquilino, on_delete=models.CASCADE)
    meses_de_locacao = models.IntegerField()
    tipo_de_locação = models.CharField(max_length=15, default="residencial")


# class MesRendimento(models.Model):
#     rendimento_do_mes = models.FloatField()
#     mes_choices = (
#         ('jan', 'Janeiro'),
#         ('fev', 'Fevereiro'),
#         ('mar', 'Março'),
#         ('abr', 'Abril'),
#         ('mai', 'Maio'),
#         ('jun', 'Junho'),
#         ('jul', 'Julio'),
#         ('ago', 'Agosto'),
#         ('set', 'Setembro'),
#         ('out', 'Outubro'),
#         ('nov', 'Novembro'),
#         ('dez', 'Dezembro'),
#     )
#     mes = models.CharField(max_length=3, choices=mes_choices)
#     valor_aluguel = models.ForeignKey(
#         Casa, on_delete=models.CASCADE)
