from django.http import HttpResponse, HttpResponseRedirect
from .models import Casa, Inquilino
from django.shortcuts import get_object_or_404, render
from .forms import CasaForm, InquilinoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    casas = Casa.objects.filter(dono=request.user)
    context = {"casas": casas}
    return render(request, "gestaoAluguel/pages/home.html", context)


@login_required(login_url='login')
def registrar_casa(request):
    context = {}
    form = CasaForm(request.POST or None)
    if form.is_valid():
        casa = form.save(commit=False)
        casa.dono = request.user
        form.save()
        messages.success(request, 'Casa registrada com sucesso!')

    context['form'] = form
    
    return render(request, "gestaoAluguel/pages/registrar_casa2.html", context)


@login_required(login_url='login')
def casa_home(request):
    casas = Casa.objects.filter(dono=request.user)
    context = {"casas": casas}

    return render(request, "gestaoAluguel/pages/casa_home.html", context)


@login_required(login_url='login')
def listar_casa(request):
    casas = Casa.objects.filter(dono=request.user)
    context = {"casas": casas}

    return render(request, "gestaoAluguel/pages/tabela_casas.html", context)


@login_required(login_url='login')
def registrar_inquilino(request):
    context = {}
    form = InquilinoForm(request.POST or None)
    if form.is_valid():
        inquilino = form.save(commit=False)
        inquilino.dono = request.user
        form.save()
        messages.success(request, 'Inquilino registrado com sucesso')

    context['form'] = form
    return render(request, "gestaoAluguel/pages/registrar_inquilino.html",
                  context)


@login_required(login_url='login')
def atualizar_casa(request, id):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Casa, id=id)

    # pass the object as instance in form
    form = CasaForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()

    # add form dictionary to context
    context["form"] = form
    Casa.calcular_data_de_vencimento(obj)
    return render(request, "gestaoAluguel/pages/atualizar_casa.html", context)


@login_required(login_url='login')
def atualizar_inquilino(request, id):
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
    obj = Casa.objects.filter(dono=request.user, id=id)
    context = {"casa": obj}

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/casa/")

    return render(request, "gestaoAluguel/pages/deletar_casa.html", context)


@login_required(login_url='login')
def deletar_inquilino(request, id):
    obj = Inquilino.objects.filter(dono=request.user, id=id)
    context = {"inquilino": obj}

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/dashboard/")

    return render(request, "gestaoAluguel/pages/deletar_inquilino.html", context)


@login_required(login_url='login')
def dashboard(request):
    user = request.user
    _rendimento_estimado = rendimento_estimado(request=request)
    _rendimento_atual = rendimento_atual(request=request)
    _rendimento_pendente = _rendimento_estimado - _rendimento_atual
    valores = [_rendimento_estimado, _rendimento_atual, _rendimento_pendente]
    context = {"user": user,
               "rendimento_estimando": _rendimento_estimado,
               "rendimento_atual": _rendimento_atual,
               "rendimento_pendente": _rendimento_pendente,
               "quantidade_de_alugueis": len(Casa.objects.filter
                                             (dono=request.user)),
               "valores": valores
               }
    print(valores)
    return render(request, "gestaoAluguel/dashboard/index.html",
                  context=context)


@login_required(login_url='login')
def listar_inquilinos(request):
    inquilinos = Inquilino.objects.filter(dono=request.user)
    context = {"inquilinos": inquilinos}
    return render(request, "gestaoAluguel/pages/listar_inquilino.html",
                  context=context)


def rendimento_estimado(request):
    casas = Casa.objects.filter(dono=request.user)
    rendimento_estimado = 0
    for casa in casas:
        rendimento_estimado += casa.valor_aluguel
    return rendimento_estimado


def rendimento_atual(request):
    casas = Casa.objects.filter(dono=request.user)
    rendimento_atual = 0
    for casa in casas:
        if casa.pago:
            rendimento_atual += casa.valor_aluguel
    return rendimento_atual
