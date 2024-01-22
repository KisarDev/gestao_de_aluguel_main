from django.contrib.auth.models import User
from despesas.models import Despesas
from django.utils import timezone
from datetime import timedelta
from django.db import models
from datetime import date


class Inquilino(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    rg = models.CharField('RG', max_length=10, unique=True)
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
    data_ultimo_pagamento = models.DateField('data_ultimo_pagamento')
    data_vencimento_aluguel = models.DateField('data_vencimento_aluguel')
    adiantamento = models.JSONField(blank=True, null=True, default={
                                    "dia_do_adiantamento": "00/00/0000",
                                    "valor_do_adiantamento": 0.0})
    despesa = models.ManyToManyField(Despesas)

    def calcular_data_de_vencimento(self):
        data_de_hoje = date.today()

        if self.data_ultimo_pagamento > self.data_vencimento_aluguel:
            self.pago = False

            novo_vencimento = self.data_ultimo_pagamento + timedelta(days=30)

            ultimo_dia_do_mes = timezone.datetime(
                self.data_ultimo_pagamento.year,
                self.data_ultimo_pagamento.month, 1) + timedelta(days=31)
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
