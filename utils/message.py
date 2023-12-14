import pywhatkit


def enviar_aviso(nome, casa, data_do_vencimento_do_aluguel):
    pywhatkit.sendwhatmsg_instantly(
        "+5535997233676", f"Olá, eu sou o assistente do Cesar, gostaria de alertar-lo que o inquilino :{nome}, da casa: {casa}, está com o aluguel atrasado pois venceu: {data_do_vencimento_do_aluguel}")
