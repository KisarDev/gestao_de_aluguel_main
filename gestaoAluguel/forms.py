from django import forms
from .models import Casa, Inquilino


class CasaForm(forms.ModelForm):
    data_ultimo_pagamento = forms.DateField(widget=forms.TextInput(
        attrs={'data-mask': "00/00/0000"}), label="data_ultimo_pagamento")
    data_vencimento_aluguel = forms.DateField(widget=forms.TextInput(
        attrs={'data-mask': "00/00/0000"}), label="data_vencimento_aluguel")

    class Meta:
        model = Casa
        exclude = ('pago', 'dono')


class InquilinoForm(forms.ModelForm):
    cpf = forms.CharField(widget=forms.TextInput(
        attrs={'data-mask': "000.000.000-00"}), label="CPF")
    rg = forms.CharField(widget=forms.TextInput(
        attrs={'data-mask': "000.000.000"}), label="RG")
    telefone = forms.CharField(widget=forms.TextInput(
        attrs={'data-mask': "(00) 0 0000-0000"}), label="telefone")

    class Meta:
        model = Inquilino
        exclude = ('dono',)
