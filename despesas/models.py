from django.db import models

tipo_choices = (
    ('A', 'Água'),
    ('E', 'Energia'),
    ('I', 'Internet'),
    ('M', 'Máquina'),
)


class Despesa(models.Model):
    tipo = models.CharField(max_length=1, choices=tipo_choices)
    casa = models.ForeignKey(
        'gestaoAluguel.Casa', related_name='casa', blank=True, on_delete=models.CASCADE)
    morador = models.ManyToManyField(
        'gestaoAluguel.Morador', related_name='morador', blank=True)
    data_chegada = models.DateField()
    data_vencimento = models.DateField()
    valor = models.FloatField()
    valor_por_pessoa = models.FloatField(blank=True, null=True)
    pago = models.BooleanField()

    def save(self, *args, **kwargs):
        # Calculate the value per person before saving
        morador_count = len(self.morador.all())
        print(morador_count)

        if morador_count > 0:
            self.valor_por_pessoa = self.valor / float(morador_count)
        else:
            self.valor_por_pessoa = 0.0

        super(Despesa, self).save(*args, **kwargs)

    def get_tipo_display(self):
        # Returns the display value for the 'tipo' field
        return dict(tipo_choices)[self.tipo]

    def __str__(self):
        return self.get_tipo_display()
