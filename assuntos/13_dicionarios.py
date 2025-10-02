# %%

# Onde se usa muito o dicionário? 1 - Chamada de API e 2 - Biblioteca Pandas

# Dicionários são pares de chave/valor
# Os tipos de chaves mais utilizados são do tipo string e int.
# Para os tipos de dados dos valores nós podemos utilizar qualquer tipo de dado incluido dicionários e listas.

dados_cicero = {
    "sobrenome": "Alcântara",
    "nome": "Cícero", 
    "filhos": False,
    "formacao":["Tecnico em mineração", "Sistemas para internet"],
    "cargos":[
        {"nome": "Analista de dados Jr", "empresa": "Fiabilité"},
        {"nome": "Analista de dados Plr", "empresa": "Fiabilité"}
    ]
}

print(dados_cicero)

# %%

# Acessar valores de um dicionário:

# É preciso passar sua chave e não o índice 

dados_cicero["nome"]

# Acessando um elemento de uma lista dentro do dicionário 

dados_cicero["formacao"][-1]

# Acessando um dicionario dentro da lista de cargos

dados_cicero["cargos"][-1]["empresa"] # Esse exmplo é especifico porque nós acessamos o dicionario de 'cargos' e como cargos é uma lista eu precisei saber qual foi minha ultima empresa que trabalhei passando o '-1' e em seguida acessando a chave de 'empresa'.

# %%

# Como adicionar uma chave nova ao dicionário

dados_cicero["estado civil"] = "Solteiro"

print(dados_cicero)

# %%

# Quais nomes das chaves?

print(dados_cicero.keys())

# Quais os valores do dicionário

print(dados_cicero.values())

# Quais os pares chave/valor

print(dados_cicero.items())

# %%

# Como andar dentro de um dicionário com 'for'

# Forma 1
for i in dados_cicero:
    print(i, "->", dados_cicero[i])

# Forma 2
# [chave, valor] é o nosso 'i'
for [chave, valor] in dados_cicero.items():
    print(chave, "->", valor)
