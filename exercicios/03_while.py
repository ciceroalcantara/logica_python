#%%
# Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

palavra = input("Digite uma palavra:")

qnt_caracteres = len(palavra)

print("Qnt caracteres:", qnt_caracteres)

count = 1

#%%
# Faça um programa que receba 4 alturas usando um laço de repetição e realize a soma dessas alturas.

count = 4
altura_total = 0

while count > 0:
    altura = float(input("Qual sua altura?"))
    altura_total = altura + altura_total
    count = count - 1

print("Soma das alturas:", altura_total)

#%%
# Faça um programa que receba uma quantidade indefinida de valores 
# correspondentes a “saldo em conta”, mas quando o usuário apertar 
# “enter” sem digitar valor algum, o programa para de receber valores, 
# e exibe a soma de todos os valores digitados anteriormente.

valor_total = 0

while True:

    valor = input("Digite um valor:")

    if valor == "": # Se o usuário apertar 'Enter' sem digitar nada, para o loop.
        break # So se usa 'break' dentro de laços de repetição e serve para sair do laço de repetição
    try: # O try serve para tratamento de erros em Python. Ele tenta executar um bloco de código que pode gerar erro, e se ocorrer algum erro, em vez de o programa travar, ele executa o bloco except.
        valor = float(valor)
        valor_total = valor + valor_total
        print("Valor digitado:", valor)
    except:
        print("Digite um valor válido.")

print("Valor total:", valor_total)
