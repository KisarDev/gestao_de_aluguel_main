from .models import Inquilino
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from gestaoAluguel.utils._gerar_contrato import _gerar_contrato
from gestaoAluguel.utils.pegar_mes import pegar_mes
from .models import Casa, Inquilino
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CasaForm, InquilinoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def registrar_casa(request):
    """Essa view registra casas"""
    context = {}
    form = CasaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            casa = form.save(commit=False)
            casa.dono = request.user
            casa.save()

            return HttpResponseRedirect(reverse("dashboard"), messages.success(request, 'Casa registrada com sucesso!'))
        else:
            # Adicione mensagens de erro ao contexto
            messages.error(
                request, 'Erro ao registrar a casa. Por favor, corrija os erros no formulário.')

    context['form'] = form
    return render(request, "gestaoAluguel/pages/registrar_casa2.html", context)


@login_required(login_url='login')
def casa_home(request):
    """Essa view lista cards com informações sobre todas as casas de um usuário"""
    casas = Casa.objects.filter(dono=request.user)
    context = {"casas": casas}

    return render(request, "gestaoAluguel/pages/casa_home.html", context)


@login_required(login_url='login')
def listar_casa(request):
    """Essa view lista todas as casas em formato tabular de um usuário"""
    casas = Casa.objects.filter(dono=request.user)
    context = {"casas": casas}

    return render(request, "gestaoAluguel/pages/tabela_casas.html", context)


@login_required(login_url='login')
def registrar_inquilino(request):
    """Essa view lista registra novos Inquilinos => moradores das casas."""
    context = {}
    form = InquilinoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            inquilino = form.save(commit=False)
            inquilino.dono = request.user
            form.save()
            messages.success(request, 'Inquilino registrado com sucesso')
            return redirect("dashboard")
        else:
            messages.error(
                request, 'Erro ao registrar a casa. Por favor, corrija os erros no formulário.')

    context['form'] = form
    return render(request, "gestaoAluguel/pages/registrar_inquilino.html",
                  context)


@login_required(login_url='login')
def atualizar_casa(request, id):
    """Essa view atualiza informações das casas"""
    context = {}
    obj = get_object_or_404(Casa, id=id)
    form = CasaForm(request.POST or None, instance=obj)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Casa atualizada com sucesso')
            return HttpResponseRedirect(reverse("dashboard"))
        else:
            messages.error(
                request, "Houve um erro na operação. Tente novamente")

    Casa.calcular_data_de_vencimento(obj)
    context["form"] = form
    return render(request, "gestaoAluguel/pages/atualizar_casa.html", context)


@login_required(login_url='login')
def atualizar_inquilino(request, id):
    """Essa view atualiza os dados dos inquilinos."""
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Inquilino, id=id)

    # pass the object as instance in form
    form = InquilinoForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()

    # add form dictionary to context
    context["form"] = form

    return render(request, "gestaoAluguel/pages/atualizar_inquilino.html", context)


# delete view for details
@login_required(login_url='login')
def deletar_casa(request, id):
    """Essa view deleta uma casa escolhida pelo usuário"""
    obj = Casa.objects.filter(dono=request.user, id=id)
    context = {"casa": obj}

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/casa/")

    return render(request, "gestaoAluguel/pages/deletar_casa.html", context)


@login_required(login_url='login')
def deletar_inquilino(request, id):
    """Essa view deleta os dados de um inquilino escolhido pelo usuário"""
    obj = Inquilino.objects.filter(dono=request.user, id=id)
    context = {"inquilino": obj}

    if request.method == "POST":
        obj.delete()
        messages.success(request, "Inquilino deletado com Sucesso.")
        return HttpResponseRedirect("/dashboard/")

    return render(request, "gestaoAluguel/pages/deletar_inquilino.html", context)


@login_required(login_url='login')
def dashboard(request):
    """Essa view apresenta é uma dashboard que contém gráficos e informações sobre rendimento atual, pendente e esperado"""
    user = request.user
    _rendimento_estimado = rendimento_estimado(request=request)
    _rendimento_atual = rendimento_atual(request=request)
    _rendimento_pendente = _rendimento_estimado - _rendimento_atual
    valores = [_rendimento_estimado, _rendimento_atual, _rendimento_pendente]
    casas_pagas = Casa.objects.filter(pago=True).all()
    month_data = pegar_mes(casas_pagas)
    context = {"user": user,
               "rendimento_estimando": _rendimento_estimado,
               "rendimento_atual": _rendimento_atual,
               "rendimento_pendente": _rendimento_pendente,
               "quantidade_de_alugueis": len(Casa.objects.filter
                                             (dono=request.user)),
               "valores": valores,
               "month_data": month_data
               }
    return render(request, "gestaoAluguel/dashboard/index.html",
                  context=context)


@login_required(login_url='login')
def listar_inquilinos(request):
    """Essa view lista todos os inquilinos"""
    inquilinos = Inquilino.objects.filter(dono=request.user)
    context = {"inquilinos": inquilinos}
    if request.method == "GET":
        return render(request, "gestaoAluguel/pages/listar_inquilino.html",
                      context=context)
    else:
        return HttpResponse("Metodo não permitido")


def rendimento_estimado(request):
    """Essa view calcula o rendimento estimado para a dashboard"""
    casas = Casa.objects.filter(dono=request.user)
    rendimento_estimado = 0
    for casa in casas:
        rendimento_estimado += casa.valor_aluguel
    return rendimento_estimado


def rendimento_atual(request):
    """Essa view calcula o rendimento atual para a dashboard"""
    casas = Casa.objects.filter(dono=request.user)
    rendimento_atual = 0
    for casa in casas:
        if casa.pago:
            rendimento_atual += casa.valor_aluguel
    return rendimento_atual


# def spider(request):
#     """Essa função verifica as casas em divida e cria um alerta no whatsapp"""
#     id_casa = verificador_de_cobranca(user=request.user)
#     casas = Casa.objects.filter(dono=request.user, id=id_casa)
#     for casa in casas:
#         nome = casa.representante
#         nome_da_casa = casa.identificador
#         data_de_vencimento = casa.data_vencimento_aluguel

#     enviar_aviso(nome=nome, casa=nome_da_casa,
#                  data_do_vencimento_do_aluguel=data_de_vencimento)
#     return HttpResponse("Aviso enviado com sucesso!")

@login_required(login_url='login')
def gerar_contrato(request, id):
    """Essa view chama uma função que gera um contrato de forma automática"""
    return _gerar_contrato(usuario=request.user, id=id)
