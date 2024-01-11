from datetime import datetime

from gestaoAluguel.models import Casa


def pegar_mes():
    data = Casa.objects.values_list('data_ultimo_pagamento', flat=True)
    data_objt = datetime.strptime(data, "%Y-%m-%d")
    month_name = data_objt.strftime("%B")
    print(month_name)
    return month_name


