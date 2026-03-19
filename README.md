# Flight Deal Agent

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Claude](https://img.shields.io/badge/Claude-Sonnet-purple?logo=anthropic)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automatizado-black?logo=githubactions)
![Serpapi](https://img.shields.io/badge/Google_Flights-Serpapi-orange)
![Resend](https://img.shields.io/badge/Email-Resend-blue)

Agente de IA que monitora passagens aéreas para a Europa todos os dias, identifica promoções e envia notificações por email com análise gerada pela Claude API.

## Como funciona

```
GitHub Actions (todo dia às 9h)
        ↓
Busca voos em 10 cidades europeias via Google Flights
        ↓
Classifica por faixa de preço
        ↓
Claude API analisa cada promoção
        ↓
Email enviado com análise e link para reserva
```

## Funcionalidades

- Monitora 10 destinos europeus a partir de Porto Alegre
- Classifica passagens em três faixas: Imperdível, Boa oferta e Preço razoável
- Análise personalizada de cada promoção gerada pela Claude API
- Email com link direto para o Google Flights
- Roda automaticamente todo dia via GitHub Actions
- Custo operacional próximo de zero

## Classificação de preços (ida e volta)

| Classificação  | Faixa de preço      |
| -------------- | ------------------- |
| Imperdível     | Abaixo de R$ 3.500  |
| Boa oferta     | R$ 3.500 – R$ 4.500 |
| Preço razoável | R$ 4.500 – R$ 6.000 |

## Destinos monitorados

Lisboa, Londres, Paris, Madrid, Roma, Amsterdã, Frankfurt, Barcelona, Milão e Viena.

## Arquitetura

```
flight-deal-agent/
├── .github/
│   └── workflows/
│       └── agent.yml        # Agendamento via GitHub Actions
├── agent/
│   ├── searcher.py          # Busca voos via Google Flights (Serpapi)
│   ├── analyzer.py          # Classifica preços e analisa com Claude API
│   └── notifier.py          # Envia email via Resend
├── main.py                  # Ponto de entrada
├── requirements.txt
└── .env.example
```

## Stack

- **Python 3.11** — linguagem principal
- **Serpapi** — acesso ao Google Flights
- **Claude API (Anthropic)** — análise inteligente das promoções
- **Resend** — envio de emails
- **GitHub Actions** — agendamento e execução na nuvem

## Como rodar localmente

1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/flight-deal-agent.git
cd flight-deal-agent
```

2. Instale as dependências

```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente

```bash
cp .env.example .env
```

Preencha o arquivo `.env` com suas chaves:

```
ANTHROPIC_API_KEY=sua_chave_aqui
RESEND_API_KEY=sua_chave_aqui
SERPAPI_KEY=sua_chave_aqui
EMAIL_FROM=seu_email_aqui
EMAIL_TO=email_destino_aqui
```

4. Rode o agente

```bash
python main.py
```

## Configuração do GitHub Actions

As chaves de API são armazenadas como Secrets no GitHub e injetadas automaticamente no workflow. Nunca são expostas no código.

Configure os seguintes secrets em **Settings → Secrets and variables → Actions**:

- `ANTHROPIC_API_KEY`
- `RESEND_API_KEY`
- `SERPAPI_KEY`
- `EMAIL_FROM`
- `EMAIL_TO`

## Autor

Desenvolvido por Calvin Silva
