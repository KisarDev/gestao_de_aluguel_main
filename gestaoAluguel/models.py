from django.db import models

# Create your models here.

class Inquilino(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=25, unique=True)
    telefone = models.CharField('Telefone', max_length=30)
    



class Casa(models.Model):
    id = models.AutoField(primary_key=True)
    representante = models.ForeignKey(Inquilino, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=80)
    valor_aluguel = models.FloatField()
    data_vencimento_aluguel = models.DateField()