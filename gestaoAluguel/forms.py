from django import forms
from .models import Casa, Inquilino


class DateInput(forms.DateInput):
    input_type = "date"
# creating a form


class CasaForm(forms.ModelForm):
    data_ultimo_pagamento = forms.DateField(
        label="Data do ultimo Pagamento", widget=DateInput())

    class Meta:
        model = Casa
        exclude = ('pago', 'dono')


class InquilinoForm(forms.ModelForm):
    class Meta:
        model = Inquilino
        exclude = ('dono',)
