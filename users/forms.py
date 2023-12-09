from django import forms

from users.models import Usuario


class UsuarioForm(forms.ModelForm):
    username = forms.CharField(label="username")
    password = forms.CharField(widget=forms.PasswordInput, label="passwrod")
    confirmar_password = forms.CharField(widget=forms.PasswordInput,
                                         label="confirmar_password")

    class Meta:
        model = Usuario
        fields = ['username', 'password', 'confirmar_password']
