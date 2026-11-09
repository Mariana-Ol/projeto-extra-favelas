import os
import glob
import pandas as pd

print("=== INICIANDO A CONSOLIDAÇÃO DO CORPUS ===")

# Descobrindo o diretório raiz e apontando para a pasta raw
raiz = os.getcwd()
caminho_raw = os.path.join(raiz, "data", "raw")
caminho_output = os.path.join(raiz, "data")
os.makedirs(caminho_output, exist_ok=True)

# Buscando todos os arquivos .txt na pasta raw
padrao_arquivos = os.path.join(caminho_raw, "*.txt")
arquivos_txt = glob.glob(padrao_arquivos)

print(f"Encontrados {len(arquivos_txt)} arquivos de texto para consolidar.")

dados_corpus = []

for caminho_arquivo in arquivos_txt:
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    
    # Extraindo as informações do cabeçalho estruturado
    titulo = "Sem título"
    subtitulo = "Sem subtítulo"
    url = ""
    texto_linhas = []
    
    # Flags para controle de leitura
    lendo_corpo = False
    
    for linha in linhas:
        if linha.startswith("TÍTULO:"):
            titulo = linha.replace("TÍTULO:", "").strip()
        elif linha.startswith("SUBTÍTULO:"):
            subtitulo = linha.replace("SUBTÍTULO:", "").strip()
        elif linha.startswith("URL:"):
            url = linha.replace("URL:", "").strip()
        elif linha.startswith("-----"):
            lendo_corpo = True
            continue
            
        if lendo_corpo:
            texto_linhas.append(linha)
            
    texto_completo = "".join(texto_linhas).strip()
    
    
    # Extração automatizada universal de Ano-Mês direto da URL
    # Procura por padrões de pastas na URL como /YYYY/MM/
    ano_mes = "Desconhecido"
    partes_url = url.split("/")
    
    for i in range(len(partes_url) - 1):
        parte_atual = partes_url[i]
        proxima_parte = partes_url[i+1]
        
        # Verifica se a parte atual é um ano válido (ex: 2020 a 2030) e a próxima é um mês (1 a 12 ou 01 a 12)
        if parte_atual.isdigit() and len(parte_atual) == 4 and 2020 <= int(parte_atual) <= 2030:
            if proxima_parte.isdigit() and 1 <= int(proxima_parte) <= 12:
                ano_mes = f"{parte_atual}-{proxima_parte.zfill(2)}"
                break

    dados_corpus.append({
        "arquivo": os.path.basename(caminho_arquivo),
        "titulo": titulo,
        "subtitulo": subtitulo,
        "url": url,
        "ano_mes": ano_mes,
        "texto": texto_completo
    })

# Criando o DataFrame Pandas
df_corpus = pd.DataFrame(dados_corpus)

# Salvando o corpus consolidado em CSV
caminho_csv = os.path.join(caminho_output, "corpus_favela_extra.csv")
df_corpus.to_csv(caminho_csv, index=False, encoding="utf-8")

print(f"\n=== CONSOLIDAÇÃO CONCLUÍDA COM SUCESSO! ===")
print(f"Total de matérias consolidadas: {len(df_corpus)}")
print(f"Arquivo salvo em: {caminho_csv}")

# Exibindo uma amostra rápida da distribuição temporal das matérias coletadas
if not df_corpus.empty:
    print("\nDistribuição das matérias por período:")
    print(df_corpus['ano_mes'].value_counts())