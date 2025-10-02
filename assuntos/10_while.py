#%%

# while (enquanto)
count = 1
while count <= 10:
    print("Entrei no laço!", count)
    count = count + 1

#%%

# Tabuada
numero = 2
quantidade = 10 

count = 1

while count <= quantidade:
    print(numero, "x", count, "=", numero *count)
    count = count + 1

#%%

# Quais numeros são divisiveis por 4 no intervalo de 4 a 100

count = 4

while count <= 100:
    resto = count % 4
    if resto == 0:
        print(count)

    count = count + 1
