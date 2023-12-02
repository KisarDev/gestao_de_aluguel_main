from django.db import models

# Create your models here.

class Inquilino(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=25, unique=True)
    telefone = models.CharField('Telefone', max_length=30)
    
    def __str__(self):
        return self.nome
    



class Casa(models.Model):
    id = models.AutoField(primary_key=True)
    identicador = models.CharField(max_length=50)
    representante = models.ForeignKey(Inquilino, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=80)
    valor_aluguel = models.FloatField()
    data_vencimento_aluguel = models.DateField()

    def __str__(self) -> str:
        return self.identicador