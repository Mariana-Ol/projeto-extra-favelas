# Projeto: Análise de matérias do portal de notícias do jornal Extra que mancionam o termo "favela"
## O projeto envolve EDA, indexação vetorial e RAG

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-em%20andamento-yellow.svg)]()

## Sobre o projeto
Este projeto desenvolve uma pipeline de Processamento de Linguagem Natural (PLN) e Recuperação Aumentada por Geração (RAG) aplicada a um corpus de notícias do jornal *Extra* sobre favelas. Os objetivos principais são desenvolver análises a respeito de matérias que mencionam o termo "favela" veiculados neste portal de notícias, com a intenção de responder a perguntas como:
* Quando o território é notícia, quem é o protaginista da ação? Quais agentes ganham mais destaque nessas matérias: os moradores? As instituições públicas? Os criminosos?
* A favela aparece majoritariamente relacionada a casos de violência urbana ou a projetos sociais/culturais?
* Há territórios super-representados pelo portal? Qual é a geografia das notícias?

Para alcançar esses objetivos, pretendo, além de realizar uma análise exploratória dos dados coletados, utlizando técnicas de PLN, indexar os dados, indexar os dados jornalísticos e utilizar uma arquitetura RAG para permitir consultas inteligentes e análises exploratórias avançadas por meio de bancos de dados vetoriais.

## O que foi feito:
* Coleta automatizada de matérias do portal de notícias Extra utilizando Selenium e consolidação dos dados em um csv: **corpus_favela_extra.csv**. Foram coletadas as matérias que contêm a palavra-chave "favela".
* Análise exploratória
* Criação de banco vetorial

## Próximos passos:
* Experimentação utilizando LLM

## Tecnologias utilizadas
* **Linguagem:** Python
* **Banco de Dados Vetorial:** ChromaDB
* **Processamento de Texto:** spaCy (POS/NER) e Pandas
* **Visualização:** Matplotlib
* **Ambiente:** Jupyter Notebook

## Estrutura do repositório
```text
projeto-extra-favelas/
├── data/
│   ├── chroma_banco_vetorial/       <- Base vetorial local indexada (ChromaDB)
│   ├── raw/                         <- Dados brutos coletados
│   └── corpus_favela_extra.csv      <- Base consolidada para análise (lida via URL)
├── notebooks/
│   ├── indexacao_vetorial.ipynb     <- Notebook de chunking e indexação vetorial
│   └── pipeline_rag.ipynb           <- Execução e testes da pipeline RAG
├── src/
│   ├── coletor_extra.py             <- Script de raspagem de dados do portal Extra
│   ├── consolidacao_de_corpus.py    <- Tratamento, limpeza e estruturação do texto
│   ├── eda.ipynb                    <- Análise Exploratória de Dados (EDA) e gráficos
│   └── teste_conexao.py             <- Validação de serviços e ambiente
├── requirements.txt                 <- Dependências do projeto
└── setup.py                         <- Configurações do pacote
