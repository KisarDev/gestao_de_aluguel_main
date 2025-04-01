from django.contrib import admin

from despesas.models import Despesa

# Register your models here.


@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'id', 'casa', 'get_morador_nome', 'data_vencimento', 'valor', 'valor_por_pessoa', 'pago')
    ordering = ('casa',)

    def get_morador_nome(self, obj):
        # Assuming Morador model has a property/method named 'info'
        return ",\n".join([morador.nome for morador in obj.morador.all()])

    # def get_despesa_pago(self, obj):
    #     # Assuming Morador model has a property/method named 'info'
    #     despesas = Despesa.objects.all()
    #     for despesa in despesas:
    #         if not despesa.pago:
    #             return ",\n".join([despesa.tipo for despesa in obj.despesa.filter(pago=False)])
    #         else:
    #             return "Tudo pago"

    get_morador_nome.short_description = 'Moradores'
    # get_despesa_pago.short_description = 'Qual despesa falta pagar ?'