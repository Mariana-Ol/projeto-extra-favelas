import os

#pastas utilizadas no projeto

pastas = ["data/raw", "data/processed", "notebooks", "src"]

for pasta in pastas:
    #os.makedirs cria a pasta.
    #exist_ok = True diz: "Se a pasta já existir, apenas siga em frente, sem dar erro"
    os.makedirs(pasta, exist_ok = True)
    print(f"Pasta {pasta} criada.")