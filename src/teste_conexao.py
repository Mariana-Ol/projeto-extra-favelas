import os
import requests

# URL de uma notícia real do Extra sobre favela/comunidade
url_teste = "https://extra.globo.com/casos-de-policia/noticia/2024/01/operacao-da-policia-civil-mira-traficantes-na-comunidade-do-salgueiro.ghtml"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"
}

print(f"Baixando matéria real: {url_teste}")

resposta = requests.get(url_teste, headers=headers)

if resposta.status_code == 200:
    caminho_arquivo = os.path.join("data", "raw", "materia_teste.html")
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(resposta.text)
    print(f"Matéria salva com sucesso em: {caminho_arquivo}")
else:
    print(f"Erro ao baixar matéria: {resposta.status_code}")