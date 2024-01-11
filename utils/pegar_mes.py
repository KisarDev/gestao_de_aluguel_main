from gestaoAluguel.models import Casa


def pegar_mes():
    datas = Casa.objects.filter(pago=True).values_list(
        'data_ultimo_pagamento', 'valor_aluguel')
    print(datas)
    
    print(casas_pagas)
    month_names = []

    for data_str in datas:
        # data_objt = datetime.strptime(data_str, "%Y-%m-%d")
        month_name = data_str.strftime("%B")
        month_names.append(month_name)
    print(month_names)
    return month_names


casas_pagas = Casa.objects.filter(pago=True).all()
valor_aluguel = casas_pagas.values_list("valor_aluguel", flat=True)
data_aluguel = casas_pagas.values_list("data_vencimento_aluguel", flat=True)

print(valor_aluguel,data_aluguel)