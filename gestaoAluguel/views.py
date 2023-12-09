from django.http import HttpResponseRedirect
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
    obj = get_object_or_404(Casa, id=id)
    context = {"casa": obj}

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/casa/")

    return render(request, "gestaoAluguel/pages/deletar_casa.html", context)


@login_required(login_url='login')
def dashboard(request):
    user = request.user
    context = {"user": user}

    return render(request, "gestaoAluguel/dashboard/index.html",
                  context=context)


@login_required(login_url='login')
def listar_inquilinos(request):
    inquilinos = Inquilino.objects.filter(dono=request.user)
    context = {"inquilinos": inquilinos}
    return render(request, "gestaoAluguel/pages/listar_inquilino.html",
                  context=context)
