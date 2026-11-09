import os
import time
from urllib.parse import unquote
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

print("=== INICIANDO COLETA AMPLIADA DE DADOS DO JORNAL EXTRA ===")

# BLINDARE SIMPLES E EFICAZ: 
# Sempre garante que a pasta 'data/raw' será criada na pasta atual onde o terminal está rodando
caminho_raw = os.path.join(os.getcwd(), "data", "raw")
os.makedirs(caminho_raw, exist_ok=True)

print(f"Diretório de destino garantido: {caminho_raw}")

# 1. Configurando e abrindo o navegador via Selenium
print("\n[Fase 1] Abrindo o navegador e carregando a página de busca...")
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

url_busca = "https://extra.globo.com/busca/?q=favela"
navegador.get(url_busca)
time.sleep(5)

# Clicando no botão "Veja mais" para expandir a janela temporal
cliques_desejados = 15
print(f"Executando {cliques_desejados} cliques no botão 'Veja mais'...")

for i in range(cliques_desejados):
    try:
        botao = navegador.find_element(By.CLASS_NAME, "pagination__load-more")
        navegador.execute_script("arguments[0].scrollIntoView();", botao)
        time.sleep(2)
        botao.click()
        print(f"  -> Clique {i+1} realizado.")
        time.sleep(3)
    except Exception as e:
        print("  -> Botão não encontrado ou fim da paginação alcançado.")
        break

# 2. Capturando o HTML da busca e fechando o navegador
print("\n[Fase 2] Extraindo e coletando os links expandidos...")
html_da_busca = navegador.page_source
navegador.quit()

sopa_busca = BeautifulSoup(html_da_busca, "html.parser")
links_coletados = []

for tag_a in sopa_busca.find_all("a"):
    href_sujo = tag_a.get("href")
    
    if href_sujo and "u=https" in href_sujo:
        parte_url = href_sujo.split("u=")[1]
        link_limpo = unquote(parte_url)
        
        if link_limpo not in links_coletados and "extra.globo.com" in link_limpo:
            links_coletados.append(link_limpo)

print(f"Total de links válidos encontrados na expansão: {len(links_coletados)}")

# 3. Entrando em cada matéria e salvando os textos na pasta correta
print("\n[Fase 3] Baixando textos e estruturando os arquivos brutos...")
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"
}

sucessos = 0
for i, link in enumerate(links_coletados):
    print(f"Baixando ({i+1}/{len(links_coletados)}): {link}")
    
    try:
        resposta = requests.get(link, headers=headers, timeout=10)
        
        if resposta.status_code == 200:
            sopa_materia = BeautifulSoup(resposta.content, "html.parser")
            
            tag_titulo = sopa_materia.find("h1", class_="content-head__title") or sopa_materia.find("h1")
            titulo = tag_titulo.get_text(strip=True) if tag_titulo else "Sem título"
            
            tag_sub = sopa_mitaeria.find("h2", class_="content-head__subtitle") if 'sopa_mitaeria' in locals() else sopa_materia.find("h2", class_="content-head__subtitle")
            tag_sub = tag_sub or sopa_materia.find("h2")
            subtitulo = tag_sub.get_text(strip=True) if tag_sub else "Sem subtítulo"
            
            paragrafos = sopa_materia.find_all("p", class_="content-text__container")
            if not paragrafos:
                paragrafos = sopa_materia.find_all("p")
                
            texto_corpo = "\n\n".join([p.get_text(strip=True) for p in paragrafos])
            
            # Salvando exatamente na pasta raw garantida
            nome_arquivo = f"materia_{i+1:03d}.txt"
            caminho_arquivo = os.path.join(caminho_raw, nome_arquivo)
            
            with open(caminho_arquivo, "w", encoding="utf-8") as f:
                f.write(f"TÍTULO: {titulo}\n")
                f.write(f"SUBTÍTULO: {subtitulo}\n")
                f.write(f"URL: {link}\n")
                f.write("-" * 50 + "\n\n")
                f.write(texto_corpo)
                
            sucessos += 1
        else:
            print(f"  -> Erro HTTP {resposta.status_code} ao acessar o link.")
            
    except Exception as e:
        print(f"  -> Erro na requisição: {e}")

print(f"\n=== COLETA AMPLIADA FINALIZADA! ===")
print(f"Sucesso: {sucessos} arquivos salvos em {caminho_raw}")