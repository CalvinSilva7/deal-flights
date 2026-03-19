import resend
import os
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

ASSUNTOS = {
    "IMPERDIVEL": "Passagem imperdivel para a Europa por R$",
    "BOA OFERTA": "Boa oferta para a Europa por R$",
    "PRECO RAZOAVEL": "Passagem razoavel para a Europa por R$",
}


def enviar_email(promocoes):
    print("Enviando email...")

    melhor = promocoes[0]
    assunto = ASSUNTOS.get(melhor["classificacao"], "Passagens para a Europa") + str(
        melhor["preco"]
    )

    corpo = "Ola! Encontramos as seguintes opcoes de passagens para a Europa:\n\n"

    for voo in promocoes:
        link = (
            f"https://www.google.com/travel/flights/search?"
            f"q=voos+de+{voo['origem']}+para+{voo['cidade']}+em+{voo['data_ida']}"
        )

        corpo += f"{voo['classificacao']}: POA -> {voo['cidade']}\n"
        corpo += f"   Preco ida e volta: R${voo['preco']}\n"
        corpo += f"   Companhia: {voo['companhia']}\n"
        corpo += f"   Duracao: {voo['duracao'] // 60}h{voo['duracao'] % 60}min\n"
        corpo += f"   Escalas: {voo['escalas']}\n"
        corpo += f"   Ida: {voo['data_ida']} | Volta: {voo['data_volta']}\n"
        corpo += f"   Analise: {voo['analise_ia']}\n"
        corpo += f"   Reservar: {link}\n\n"

    params = {
        "from": os.getenv("EMAIL_FROM"),
        "to": os.getenv("EMAIL_TO"),
        "subject": assunto,
        "text": corpo,
    }

    response = resend.Emails.send(params)
    print(f"Email enviado! ID: {response['id']}")
