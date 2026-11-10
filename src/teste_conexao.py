import os
import requests

# 1. Definimos a URL de busca ou de uma matéria do Extra
url_teste = "https://extra.globo.com/busca/?q=favela"

# Simulamos um navegador real (User-Agent) para evitar bloqueios simples
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"
}

print(f"Tentando acessar: {url_teste}")

# 2. Fazemos a requisição HTTP GET
resposta = requests.get(url_teste, headers=headers)

# 3. Verificamos se a requisição foi bem-sucedida (Código 200)
print(f"Código de Status HTTP: {resposta.status_code}")

if resposta.status_code == 200:
    print("✅ Conexão estabelecida com sucesso!")
    
    # Vamos usar a biblioteca 'os' para definir onde salvar o HTML bruto para inspeção
    caminho_arquivo = os.path.join("data", "raw", "pagina_teste.html")
    
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(resposta.text)
        
    print(f"Conteúdo HTML salvo em: {caminho_arquivo}")
else:
    print(f"Falha ao acessar a página. Código: {resposta.status_code}")