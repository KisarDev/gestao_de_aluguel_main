from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from users.forms import UsuarioForm
from django.contrib.auth.hashers import make_password

from users.models import Usuario

# Create your views here.


def registrar_usuario(request):
    form = UsuarioForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        confirmar_password = form.cleaned_data['confirmar_password']
        password = make_password(password)
        confirmar_password = make_password(confirmar_password)
        user = Usuario(username=username, password=password,
                       confirmar_password=confirmar_password)
        user.save()
        messages.success(request, 'Usuário registrado com sucesso')
        return redirect("registrar_usuario")
    return render(request, 'users/pages/registrar_usuario.html', context)
