from django import forms
from .models import Casa, Inquilino
 
 
# creating a form
class CasaForm(forms.ModelForm):
    class Meta:
        model = Casa
        exclude = ('pago',)

class InquilinoForm(forms.ModelForm):
    class Meta:
        model = Inquilino
        fields = '__all__'