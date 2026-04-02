import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

ORIGEM = "POA"

DESTINOS_EUROPA = [
    "LIS",
    "LHR",
    "CDG",
    "MAD",
    "FCO",
    "AMS",
    "FRA",
    "BCN",
    "MXP",
    "VIE",
]

DATA_IDA = "2027-02-01"
DATA_VOLTA = "2027-02-15"


def buscar_voos():
    print("Buscando voos para a Europa")

    todos_voos = []

    for destino in DESTINOS_EUROPA:
        print(f"Buscando POA -> {destino}")

        params = {
            "engine": "google_flights",
            "departure_id": ORIGEM,
            "arrival_id": destino,
            "outbound_date": DATA_IDA,
            "return_date": DATA_VOLTA,
            "type": "1",
            "currency": "BRL",
            "hl": "pt",
            "adults": "1",
            "sort_by": "1",
            "api_key": SERPAPI_KEY,
        }

        busca = GoogleSearch(params)
        resultados = busca.get_dict()

        if resultados.get("error"):
            print(f"Sem resultados para {destino}")
            continue

        voos = resultados.get("best_flights", []) + resultados.get("other_flights", [])

        if not voos:
            print(f"Nenhum voo encontrado para {destino}")
            continue

        melhor = min(voos, key=lambda v: v.get("price", 9999999))

        todos_voos.append(
            {
                "origem": ORIGEM,
                "destino": destino,
                "preco": melhor.get("price"),
                "data_ida": DATA_IDA,
                "data_volta": DATA_VOLTA,
                "duracao": melhor.get("total_duration"),
                "escalas": len(melhor.get("flights", [])) - 1,
                "companhia": melhor.get("flights", [{}])[0].get("airline", ""),
            }
        )

    todos_voos.sort(key=lambda v: v.get("preco", 9999999))
    return todos_voos
