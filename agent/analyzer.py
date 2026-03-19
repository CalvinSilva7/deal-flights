import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

PRECO_INCRIVEL = 3500
PRECO_BOM = 4500
PRECO_MAXIMO = 6000

DESTINOS_NOMES = {
    "LIS": "Lisboa",
    "LHR": "Londres",
    "CDG": "Paris",
    "MAD": "Madrid",
    "FCO": "Roma",
    "AMS": "Amsterdã",
    "FRA": "Frankfurt",
    "BCN": "Barcelona",
    "MXP": "Milão",
    "VIE": "Viena",
}


def classificar_preco(preco):
    if preco <= PRECO_INCRIVEL:
        return "IMPERDIVEL"
    elif preco <= PRECO_BOM:
        return "BOA OFERTA"
    elif preco <= PRECO_MAXIMO:
        return "PRECO RAZOAVEL"
    return None


def analisar_promocoes(voos):
    print("\nAnalisando precos...")

    promocoes = []

    for voo in voos:
        if not voo["preco"]:
            continue

        classificacao = classificar_preco(voo["preco"])

        if classificacao is None:
            print(f"POA → {voo['destino']}: R${voo['preco']} - acima do limite")
            continue

        analise = analisar_com_ia(voo, classificacao)
        voo["analise_ia"] = analise
        voo["classificacao"] = classificacao
        voo["cidade"] = DESTINOS_NOMES.get(voo["destino"], voo["destino"])
        promocoes.append(voo)
        print(f"POA → {voo['cidade']}: R${voo['preco']} - {classificacao}")

    promocoes.sort(key=lambda v: v["preco"])
    return promocoes[:3]


def analisar_com_ia(voo, classificacao):
    cidade = DESTINOS_NOMES.get(voo["destino"], voo["destino"])

    if classificacao == "IMPERDIVEL":
        tom = "extremamente empolgante, diga que é uma oportunidade rarissima"
    elif classificacao == "BOA OFERTA":
        tom = "empolgante mas equilibrado, diga que é uma boa oportunidade"
    else:
        tom = "racional e informativo, diga que vale considerar mas nao é excepcional"

    prompt = f"""Você é um especialista em viagens para a Europa.

Viagem: Porto Alegre → {cidade}
Ida: {voo['data_ida']} | Volta: {voo['data_volta']} (14 dias)
Preco ida e volta: R${voo['preco']}
Classificacao: {classificacao}
Duracao do voo: {voo['duracao'] // 60}h{voo['duracao'] % 60}min
Escalas: {voo['escalas']}
Companhia: {voo['companhia']}

Em 2 frases, analise esse preco e diga o que torna {cidade} especial em fevereiro.
Tom: {tom}
Sem markdown, sem asteriscos, texto simples apenas."""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}],
    )

    return message.content[0].text