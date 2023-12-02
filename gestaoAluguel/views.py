from django.shortcuts import render
from .models import Casa, Inquilino
from .forms import CasaForm, InquilinoForm
from django.contrib import messages
 
def registrar_casa(request):
    context ={}
    form = CasaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Casa registrada com sucesso!')
         
    context['form']= form
    return render(request, "gestaoAluguel/pages/registrar_casa.html", context)