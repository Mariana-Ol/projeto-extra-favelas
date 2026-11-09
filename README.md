# Projeto Jornal Extra Favelas: EDA, Indexação Vetorial e RAG

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Mariana-Ol/projeto-extra-favelas/blob/main/notebooks/indexacao_vetorial.ipynb)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-em%20andamento-yellow.svg)]()

## 📌 Sobre o projeto
Este projeto desenvolve uma pipeline de Processamento de Linguagem Natural (PLN) e Recuperação Aumentada por Geração (RAG) aplicada a um corpus de notícias do jornal *Extra* sobre favelas. O objetivo principal é estruturar, limpar e indexar textual e semanticamente os dados jornalísticos, permitindo consultas inteligentes e análises exploratórias avançadas por meio de bancos de dados vetoriais.

## 🛠️ Tecnologias utilizadas
* **Linguagem:** Python
* **Banco de Dados Vetorial:** ChromaDB
* **Processamento de Texto:** spaCy (POS/NER) e Pandas
* **Visualização:** Matplotlib
* **Ambiente:** Jupyter Notebook

## 📂 Estrutura do repositório
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
