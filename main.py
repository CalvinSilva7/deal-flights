from agent.searcher import buscar_voos
from agent.analyzer import analisar_promocoes
from agent.notifier import enviar_email, enviar_email_status


def main():
    print("Iniciando o agente de passagens")

    voos = buscar_voos()
    promocoes = analisar_promocoes(voos)

    if promocoes:
        enviar_email(promocoes)
    else:
        mensagem = (
            "O agente rodou hoje e nao encontrou passagens "
            "dentro da faixa de preco configurada.\n\n"
            "Destinos monitorados: Lisboa, Londres, Paris, Madrid, "
            "Roma, Amsterda, Frankfurt, Barcelona, Milao, Viena\n"
            "Faixa de preco: ate R$6.000 ida e volta\n"
            "Data monitorada: 01/02/2027 - 15/02/2027\n\n"
            "O agente continua monitorando e vai te avisar assim "
            "que aparecer uma boa oferta!"
        )
        enviar_email_status(mensagem)
        print("Email de status enviado")


if __name__ == "__main__":
    main()