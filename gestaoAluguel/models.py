from datetime import timedelta
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import date


class Inquilino(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=25, unique=True)
    telefone = models.CharField('Telefone', max_length=30)

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
        return self.identificador
