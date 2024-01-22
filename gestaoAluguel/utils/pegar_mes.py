def pegar_mes(casas_pagas):

    # Lista para armazenar os nomes dos meses e valores de aluguel
    month_data = {'month_names': [], 'values': []}

    for casa in casas_pagas:
        value = casa.valor_aluguel
        month_name = casa.data_vencimento_aluguel.strftime("%B")

        month_data['month_names'].append(month_name)
        month_data['values'].append(value)
    return month_data
