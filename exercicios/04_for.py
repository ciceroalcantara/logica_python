#%%
# Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

nome = "cicero alcantara"

count = 0

for i in nome:
    if i == "a":
        print(i)
        count = count + 1

print(count)

#%%
# Faça um programa que receba 4 alturas usando um laço de repetição e realize a soma dessas alturas.

altura_total = 0
quantidade = 4

for i in range(quantidade):
    altura = input("Digite sua altura:")
    altura = float(altura)
    print("Altura", i + 1, "-", altura)
    altura_total = altura_total + altura

print("Valor altura total:", altura_total)
