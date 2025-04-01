from django.contrib import admin
from gestaoAluguel.models import Casa, Despesa, Morador, Inquilino


@admin.register(Casa)
class CasaAdmin(admin.ModelAdmin):
    list_display = ('identificador', 'representante', 'get_morador_nome',
                    'valor_aluguel', 'data_vencimento_aluguel',
                    'pago', 'get_despesa_pago')
    ordering = ('id',)

    def get_morador_nome(self, obj):
        # Assuming Morador model has a property/method named 'info'
        return ",\n".join([morador.nome for morador in obj.morador.all()])

    def get_despesa_pago(self, obj):
        # Assuming Morador model has a property/method named 'info'
        despesas = Despesa.objects.all()
        count = 0
        for despesa in despesas:
            pago = despesa.pago
            if not pago:
                count += 1
                return ",\n".join(["ID: " + str(despesa.id) for despesa
                                   in obj.despesa.filter(pago=False)])
            elif count == 0:
                return "Tudo pago"

    get_morador_nome.short_description = 'Moradores'
    get_despesa_pago.short_description = 'Qual despesa falta pagar ?'


admin.site.register(Morador)
admin.site.register(Inquilino)
