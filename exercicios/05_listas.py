# %%

# Escreva um programa que receba uma lista de números do usuário 
# e conte quantas vezes um número especifico aparece na lista.
# Solicite ao usuário um número e exiba a contagem.

numero_lista = []

while True:

    numero = input("Digite um número:")

    if numero == "":
        break
    try:
        numero = int(numero)
        numero_lista.append(numero)
    except:
        print("Escolha um número válido.")

print("Aqui sua lista de números:", numero_lista)

numero_escolhido = input("Digite um número para ser pesquisado na lista:")
numero_escolhido = int(numero_escolhido)

count = 0

for i in numero_lista:
    if i == numero_escolhido:
        count = count + 1

print("O número escolhido foi", numero_escolhido, ", e ele aparece", count, "x na lista.")
