# %%

nome_arquivo = "dados.csv"

with open(nome_arquivo) as open_file:
    csv = open_file.readlines()

# %%

# Percorre as linhas de um arquivo csv.

for linha in csv:
    print(linha)

# %%

# Transformar o conteudo do csv em um dicionário

dados = dict()

# Define quais são as chaves do dicionario com os campos da primeira linha do csv
chaves = csv[0].strip("\n").split(";") # O 'strip' remove os caracteres e o 'split' separa pelo separador que a gente escolher

# Percorrer cada umas das chaves e criar uma lista vazia para cada chave criada.
for i in chaves:
    dados[i] = []

# %%

# Percorrer o restante dos registros do csv

for i in csv[1:]: # leio da segunda linha ate a ultima

    valores = i.strip("\n").split(";") # Crio os dados de cada linha e salvo numa variavel do tipo lista

    for i in range(0, len(valores)): # Passo por todas as chaves do dicionario e salvo esses valores

        dados[chaves[i]].append(valores[i])

dados

# %%

# Calcular a média de idades 

idades = []

for i in dados["idade"]:
    idades.append(int(i))

media = sum(idades) / len(idades)
media
