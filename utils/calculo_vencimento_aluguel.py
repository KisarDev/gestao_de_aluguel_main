from datetime import datetime, timedelta

# Data de vencimento inicial (exemplo: 10/01/2024)
data_vencimento = datetime.strptime('10/01/2024', '%d/%m/%Y')

# Marca o aluguel como pago em 10/01/2024
data_pagamento = datetime.strptime('10/01/2024', '%d/%m/%Y')

# Verifica se o pagamento ocorreu antes ou na data de vencimento
if data_pagamento <= data_vencimento:
    # Adiciona um mês à data de vencimento
    nova_data_vencimento = data_vencimento + timedelta(days=30)

    # Exibe a nova data de vencimento
    print("Data de vencimento anterior:", data_vencimento.strftime("%d/%m/%Y"))
    print("Nova data de vencimento:", nova_data_vencimento.strftime("%d/%m/%Y"))
else:
    print("O pagamento foi realizado após a data de vencimento.")
