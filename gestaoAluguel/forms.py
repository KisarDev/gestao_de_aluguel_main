from django import forms
from .models import Casa, Inquilino
 
 
# creating a form
class CasaForm(forms.ModelForm):
    class Meta:
        model = Casa
        fields = '__all__'

class InquilinoForm(forms.ModelForm):
    class Meta:
        model = Inquilino
        fields = '__all__'