# %%

# Listas

idades = [28, 42, 43, 35, 39, 32, 50]

print(idades)

# %%

cicero = ["Cícero", "Magro", 32, True, "Solteiro", 2342.98]

print(cicero)

# %%

# Acessar elementos da lista a partir do indice

# Idade
print(cicero[2])

# Renda
print(cicero[5])

# %%

idades = [28, 42, 43, 35, 39, 32, 50]

print("Soma idades:", sum(idades))

print("Qnt idades:", len(idades))

print("Média de idades:", sum(idades) / len(idades))

print("Qual a menor idade?", min(idades))

print("Qaul a maior idade?", max(idades))

# %%

# Acessa posições da lista

cicero = ["Cícero Alcântara", 
          32, 
          True, 
          "Solteiro", 
          ["D.a jr", "D.a pl"],
          [4000, 4500, 6500, 10000],
          ["Fernanda", "Gabi", "Thaynara", "Jayanne", "Marillian"]]

print(len(cicero))

print(cicero[6][0])

# %%

# Pegando ultimo elemento de uma lista

tamanho = len(cicero)
ultima_posicao = tamanho - 1
ex_namoradas = cicero[ultima_posicao]

print("Ultima posição de uma lista:", ex_namoradas)

# %%

# Pega o ultimo elemento da lista

cicero[-1][-2]

# %%

# Pega uma quantidade determina de posições de elementos
# Como sempre é um intervalo aberto temos que considerar todos os indices

#Syntax: cicero[start : stop]

cicero[:4] # Pega os primeiros 4 elementos da lista

# %%


# Pega os 2 ultimos empregos da lista de empregos dentro da lista 'cicero'

cicero[4][-2:]

# %%

# Acessar a lista de salarios de tras pra frente

salarios = cicero[5]

print(salarios)

salarios[::-1]

# %%

# incluir idades a uma lista de idades vazia

idades = []

while True:

    idade = input("Digite uma idade:")

    if idade == "":
        break
    try:
        idade = int(idade)
        idades.append(idade)
    except:
        print("Digite uma idade válida.")

print(idades)

print("Soma idades:", sum(idades))

print("Qnt idades:", len(idades))

print("Média de idades:", sum(idades) / len(idades))

print("Qual a menor idade?", min(idades))

print("Qaul a maior idade?", max(idades))

# %%

y = [i for i in range[1, 101]]
y

# %%


