from gestaoAluguel.models import Casa


def verificador_de_cobranca(user):
    casas = Casa.objects.filter(dono=user)
    for casa in casas:
        if not casa.pago:
            return casa.id
