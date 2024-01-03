from django import forms

from despesas.models import Despesas


class DespesasForm(forms.ModelForm):
    class Meta:
        model = Despesas
        exclude = ('valor_por_pessoa',)
