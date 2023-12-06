from .models import Casa, Inquilino
from django.shortcuts import render
from .forms import CasaForm, InquilinoForm
from django.contrib import messages


def home(request):
    casas = Casa.objects.all()
    context = {"casas": casas}
    return render(request, "gestaoAluguel/pages/home.html", context)


def registrar_casa(request):
    context = {}
    form = CasaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Casa registrada com sucesso!')

    context['form'] = form
    return render(request, "gestaoAluguel/pages/registrar_casa.html", context)


def casa_home(request):
    casas = Casa.objects.all()
    context = {"casas": casas}

    return render(request, "gestaoAluguel/pages/casa_home.html", context)


def listar_casa(request):
    casas = Casa.objects.all()
    context = {"casas": casas}

    return render(request, "gestaoAluguel/pages/teste.html", context)


def registrar_inquilino(request):
    context = {}
    form = InquilinoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Inquilino registrado com sucesso')

    context['form'] = form
    return render(request, "gestaoAluguel/pages/registrar_inquilino.html", context)
