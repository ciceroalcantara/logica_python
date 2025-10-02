#%%
# Faça um programa que vende uma garrafa de água:
# a) Se o cliente escolher água mineral natural, será cobrado R$1,50
# b) Se o cliente escolher água mineral com gás, será cobrado R$2,50

agua = int(input("Natural = 1 | Gás = 2 -- Escolha sua água:"))

valor = 0

if agua == 1:
    valor = 1.5
elif agua == 2:
    valor = 2.5

if valor == 0:
    print("Escolha uma opção válida.")
else:
    print("sua conta é: R$", valor)

#%%
# Altere o programa anterior para considerar a quantidade de garrafas de água

agua = int(input("Natural = 1 | Gás = 2 -- Escolha sua água:"))

valor_item = 0

if agua == 1:
    valor_item = 1.5
elif agua == 2:
    valor_item = 2.5

if valor_item == 0:
    print("Escolha uma opção válida.")
else:
    quantidade = int(input("Quantas garrafas?"))
    valor_total = valor_item * quantidade
    print("Sua conta é: R$", valor_total)

#%%
# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# a) Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# b) Sabor do sorvete: morango, creme, chocolate
# c) Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

tipo_sorvete = input("Tipo de sorvete: casquinha (R$1,00), cascao (R$2,50), cestinha (R$4,00)")
sabor_sorvete = input("Sabor do sorvete: morango, creme, chocolate")
cobertura = input("Cobertura: caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)")

if tipo_sorvete == "casquinha":
    valor_tipo_sorvete = 1
elif tipo_sorvete == "cascao":
    valor_tipo_sorvete = 2.5
elif tipo_sorvete == "cestinha":
    valor_tipo_sorvete = 4

if cobertura == "caramelo" or cobertura == "morango" or cobertura == "chocolate":
    valor_cobertura = 1.5
elif cobertura == "sem cobertura":
    valor_cobertura = 0

print("Tipo sorvete:", tipo_sorvete, "Valor:", valor_tipo_sorvete)
print("Sabor sorvete:", sabor_sorvete)
print("Cobertura:", cobertura, "Valor:", valor_cobertura)
print("Valor total:", valor_tipo_sorvete + valor_cobertura)

#%%
# Faça um programa que verifique se a pessoa pertence à família “calvo”.

sobrenome = input("qual sobrenome da sua familia:")

if sobrenome == "calvo":
    print("Você é da familia calvo!!")
else:
    print(sobrenome, "- Não é da familia calvo.")

#%%
# Faça um programa que verifique se a pessoa pertence à família “calvo” ou “silva”.

sobrenome = input("qual sobrenome da sua familia:")

if sobrenome == "calvo" or sobrenome == "silva":
    print("Você é da familia", sobrenome, "!!")
else:
    print(sobrenome, "- Não é da familia calvo ou silva.")

#%%
# Faça um programa que verifique se o item que a pessoa escolheu para comprar na loja está na lista: laranja, cerveja, miojo, carvão, picanha.

produto = input("O que você deseja comprar:")

estoque = ["laranja", "cerveja", "miojo", "carvao", "picanha"]

if produto in estoque:
    print("O produto -", produto, "- existe no estoque!!")
else:
    print("O produto -", produto, "- não existe no estoque!!")
