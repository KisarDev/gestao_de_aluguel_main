from django import forms

from despesas.models import Despesa


class DespesasForm(forms.ModelForm):
    class Meta:
        model = Despesa
        exclude = ('valor_por_pessoa',)
