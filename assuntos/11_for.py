#%%

# For

nome = "Cicero Alcantara"

for letra in nome:
    print(letra)

#%%

# Tabuada

numero = 2
max_numero = 100

for count in range(1, max_numero + 1):
    print(numero, "x", count, "=", numero * count)

#%%

# Divisiveis por 4 entre 1 e 100

for i in range(1, 101):
    if i % 4 == 0:
        print(i)
        