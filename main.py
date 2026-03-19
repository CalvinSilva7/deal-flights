from agent.searcher import buscar_voos
from agent.analyzer import analisar_promocoes
from agent.notifier import enviar_email


def main():
    print("Iniciando o agente de passagens...")

    voos = buscar_voos()
    promocoes = analisar_promocoes(voos)

    if promocoes:
        enviar_email(promocoes)
    else:
        print("Nenhuma promocao encontrada hoje.")


if __name__ == "__main__":
    main()