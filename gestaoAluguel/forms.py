from django import forms
from .models import Casa, Inquilino


# creating a form
class CasaForm(forms.ModelForm):
    class Meta:
        model = Casa
        exclude = ('pago', 'dono')


class InquilinoForm(forms.ModelForm):
    class Meta:
        model = Inquilino
        exclude = ('dono',)
