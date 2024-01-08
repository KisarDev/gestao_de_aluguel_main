from django.shortcuts import render

from despesas.forms import DespesasForm
from despesas.models import Despesas
from django.contrib.auth.decorators import login_required


# Create your views here.


def registrar_despesas(request):
    form = DespesasForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        form.save()
    return render(request, 'despesas/registrar_despesas.html', context)


@login_required(login_url='login')
def listar_despesas(request):
    despesas = Despesas.objects.all()
    casas = []
    for despesa in despesas:
        casas_str = ', '.join([str(casa) for casa in despesa.casa.all()])
        casas.append(casas_str)
    context = {"despesas": despesas, "casas": casas}
    return render(request, "despesas/listar_despesas.html",
                  context=context)
