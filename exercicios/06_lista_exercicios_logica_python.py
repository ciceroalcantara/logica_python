# %%

# Escreva um programa que receba o nome de uma pessoa e faça uma saudação.

# “Olá fulano! Seja Bem vindo!”

nome = input("Digite seu nome: ")

print("Olá", nome, "! Seja bem vindo!")

# %%

# Escreva um programa que receba o nome e a idade de uma pessoa. Depois exiba a mensagem:

# “Olá fulano, bom saber que você tem x anos. Seja bem vindo!”

nome = input("Digite seu nome:")
idade = input("Digite sua idade:")

print("Olá", nome, "! bom saber que você tem", idade, "anos. Seja bem vindo!")

# %%

# Faça um programa que receba o raio de uma circunferência em centímetros. Retorne para o usuário qual é a área e perímetro desta circunferência no seguinte formato.

# Área:  x.xx
# Perímetro:  y.yy

raio = input("Digite o raio da circunferência:")
raio = float(raio)

pi = 3.14

area = pi * (raio ** 2)

perimetro = 2 * pi * raio

print("Área:", area)
print("Perimetro:", perimetro)

# %%

# Faça um programa que receba dois valores A e B. Faça a soma desses dois valores e retorne o resultado:

# Soma:  x.xx

valor_a = input("Digite um valor para A:")
valor_a = float(valor_a)

valor_b = input("Digite um valor para B:")
valor_b = float(valor_b)

soma = valor_a + valor_b

print("Soma:", soma)

# %%

# Faça um programa que receba dois valores A e B. Faça a potência desses dois valores e retorne o resultado:

# a ^ b = z

valor_a = input("Digite um valor para A:")
valor_a = float(valor_a)

valor_b = input("Digite um valor para B:")
valor_b = float(valor_b)

potencia = valor_a ** valor_b

print(valor_a, "^", valor_b, "=", potencia)

# %%

# Faça um programa que receba um número em segundos, converta esse número para horas, minuto e segundos. Exemplos:

# ntrada: 556
# Saída: 0:9:16

# Entrada: 140153
# Saída: 38:55:53

numero = input("Digite um numero em segundos:")
numero = int(numero)

hora = int(numero / 3600)
resto_hora = numero % 3600

minutos = int(resto_hora / 60)

segundos = resto_hora % 60

print("Saida:", hora, ":", minutos, ":", segundos)

# %%

# Faça um programa que receba o nome e a idade de uma pessoa. 

# Caso essa pessoa tenha menos de 18 anos, exiba o aviso:
#	“Fulano, você não pode dirigir nem beber”

# Para as pessoas entre 18 e 65 anos, exiba o aviso:
#	“Fulano, bebida liberada! Só não vale dirigir!”

# Para as pessoas com mais de 65 anos, exiba o aviso:
#	“Fulano, beba com muita moderação!”

nome = input("Digite seu nome:")

idade = input("Digite sua idade:")
idade = int(idade)

if idade < 18:
    print(nome, ", você não pode dirigir nem beber!")
elif idade >= 18 and idade <= 65:
    print(nome, ", bebida liberada! Só não vale dirigir!")
else:
    print(nome, ", beba com muita moderação!")

# %%

# Faça um programa que receba um número. Verifique se o número informado é par ou ímpar. Exiba o resultado da seguinte maneira:

#	O número x é impar
# ou
#	O número x é par

numero = input("Digite um numero:")
numero = int(numero)

resto = numero % 2

if resto == 0:
    print("O numero", numero, "é par.")
else:
    print("O numero", numero, "é impar.")

# %%

# Escreva um programa que solicite ao usuário um nome e uma idade, e crie um dicionário com essas informações. Em seguida, exiba o dicionário.

pessoas = {}

nome = input("Digite seu nome:")
idade = input("Digite sua idade:")
idade = int(idade)

pessoas["nome"] = nome
pessoas["idade"] = idade

print(pessoas)

# %%

# Faça um programa que receba 4 notas de um aluno. Retorne a média dessas notas, a menor e a maior nota:

# Média: x
# Menor: y
# Maior: z

notas = []
qnt_notas = 4

for i in range(qnt_notas):

    nota = float(input("Digite uma nota:"))
    notas.append(nota)
    print("Nota", i + 1, ":", nota)

print("Média:", sum(notas) / len(notas))
print("Menor:", min(notas))
print("Maior:", max(notas))

# %%

# Considere a lista: [120, “Python”, 120.01, “asw”, False, [10,20] ]

# Faça um programa que retorne as seguintes informações:
# Elemento na posição -1 da lista
# Elemento na primeira posição da lista
# O último caractere do segundo elemento da lista

# Elemento -1: x
# Primeiro elemento: y
# Último caractere do segundo elemento: z

lista = [120, "Python", 120.01, "asw", False, [10,20] ]

print("Elemento -1:", lista[-1])

print("Primeiro elemento:", lista[0])

lista_2 = []

for i in lista[1]:
    lista_2.append(i)
    
print("Último caractere do segundo elemento:", lista_2[-1])

# %%

# Escreva um programa que solicite ao usuário duas strings e as concatene em uma única String. Em seguida, exiba a String resultante.

string_1 = input("Digite a primeira palavra:")
string_2 = input("Digite a segunda string")

string_concatenada = string_1 + " " + string_2

print(string_concatenada)

# %%

# Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.

# Maçã: R$1,50
# Banana: R$2,75
# Uva: R$1,90
# Pera: R$1,25
# Laranja: R$0,65
# Limão: R$1,25
# Goiaba: R$2,15
# Abacaxi: R$3,20
# Jaca: R$5,80

frutas = [
    {"fruta": "maça", "valor": 1.50},
    {"fruta": "banana", "valor": 2.75},
    {"fruta": "uva", "valor": 1.90},
    {"fruta": "pera", "valor": 1.25},
    {"fruta": "laranja", "valor": 0.65},
    {"fruta": "limao", "valor": 1.25},
    {"fruta": "goiaba", "valor": 2.15},
    {"fruta": "abacaxi", "valor": 3.20},
    {"fruta": "jaca", "valor": 5.80}
]

fruta_get = input("Qual fruta gostaria de saber o valor?")

for i in frutas:
    if i["fruta"] == fruta_get:
        print("O valor de", i["fruta"], "é R$:", i["valor"])
        break
else:
    print("Fruta", fruta_get, "não encontrada.")

# %%

# Faça um programa que receba um número. Este número corresponde a uma posição na sequência de Fibonacci: 1, 1, 2, 3, 5,...

# Exiba o número da sequência cuja posição foi informada:
#	A posição x corresponde ao número y

numero = int(input("Digite um número:"))

fibonacci = [0, 1]

for i in range(1000):
    proximo_numero = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_numero)

print("A posição", numero, "corresponde ao número", fibonacci[numero - 1])

# %%

# Faça um programa com uma função que recebe uma frase. Para cada palavra nesta frase, inverta a ordem das letras. Exiba o resultado:

#	Esta é a frase original

#	atsE é a esarf lanigiro

frase = input("Digite uma frase:")

lista_palavra = frase.split()

lista_palavra_invertida = []

for i in lista_palavra:
    i = i[::-1]
    lista_palavra_invertida.append(i)

frase_invertida = " ".join(lista_palavra_invertida)

print(frase_invertida)

# %%

# aça um programa que receba um número. Verifique se este número é primo ou não, e retorne o resultado:

#	O número x é primo
# ou
#	O número x não é primo



# %%

# Escreva um programa que exiba os números de 1 a 100. 
# Caso o número seja divisível por 3, exiba “Fizz” no seu lugar, 
# e para múltiplos de 5 exiba “Buzz”. Caso seja divisível por ambos, 
# exiba “FizzBuzz”.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        i = "FizzBuzz"
    elif i % 5 == 0:
        i = "Buzz"
    elif i % 3 == 0:
        i = "Fizz"
    
    print(i)

# %%

# Faça um programa que receba um número e exiba seu fatorial.

numero = int(input("Digite um número:"))

resultado = 1 # Por que 1? Porque 1 é o elemento neutro da multiplicação (assim como 0 é da soma)

for i in range(numero):
    i = i + 1
    resultado = resultado * i 

print("O fatorial de", numero, "é", resultado, ".")

# %%

# Considere a seguinte lista:
# [123, 435, 987, 1984, 2, 19, 423, -178, 320]

# Faça um programa que retorne a posição do menor e do maior valor encontrado:

# O maior valor está na posição x
# O menor valor está na posição y

lista = [123, 435, 987, 1984, 2, 19, 423, -178, 320]

menor_valor = min(lista)
maior_valor = max(lista)

print("O menor valor está na posição", lista.index(menor_valor))
print("O maior valor está na posição", lista.index(maior_valor))

# %%

# Escreva um programa que receba uma lista de números do usuário 
# e conte quantas vezes um número específico aparece na lista. 
# Solicite ao usuário um número e exiba a contagem.

lista = []

while True:

    numero_add_lista = input("Digite um numero:")

    if numero_add_lista == "":
        break
    try:
        numero_add_lista = int(numero_add_lista)
        lista.append(numero_add_lista)
    except:
        print("Digite um numero válido.")

print(lista)

numero_pesquisa = int(input("Digite um numero que gostaria de pesquisar na lista:"))

contador = 0

for i in lista:
    if i == numero_pesquisa:
        contador = contador + 1
    
print("O número", numero_pesquisa, "aparece", contador, "x na lista gerada.")

# %%

# Escreva um programa que solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

numero = int(input("Digite um número:"))

qnt_repeticao = 10

count = 0

for i in range(1, qnt_repeticao + 1):
    print(i, "x", numero, "=",i * numero)

# %%

# Escreva um programa que solicite ao usuário uma palavra e verifique se a palavra é um palíndromo (ou seja, é a mesma palavra quando lida de trás para frente).

palavra = input("Digite uma palavra:")

palavra_invertida = palavra[::-1]

if palavra_invertida == palavra:
    print("O palindromo de", palavra, "é", palavra_invertida)
else:
    print("A palavra", palavra,"não tem palindromo.")

# %%

# Escreva um programa que solicite ao usuário frases. Para parar de solicitar frases, ele pode apenas apertar o “enter”.

# Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.

dados = {}

while True:
    frase = input("Digite uma frase:")
    if frase == "":
        break

    if frase not in dados:
        dados[frase] = 1 # Cria uma chave nova no dicionario. Como é uma chave nova a gente adciona 1 portque ela so apareceu 1x
    else:
        dados[frase] += 1 # Se a frase existir a gente adciona 1 

for i, j in dados:
    print(i, "->", dados[i])

# %%

# Construa um programa que realiza o sorteio de um número entre 1 e 15.

# O usuário terá 3 chances de acertar o valor.

# A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.

# Caso o usuário acerte, dê os parabéns.

import random

def get_input():
    while True:
        try: # Tenta fazer isso que está dentro do 'try'
            numero_escolhido = int(input("Digite o numero que voce acha que sera sorteado entre 1 e 15:"))

        except ValueError: # Se der erro no input de cima entra nessa exeção de erro, no caso o tipo do dado do input pode ser o errado e se não for int vai dar erro.
            print("Entre com um número válido.")
            continue # Se der erro do tipo do dado o codigo vai ignorar o if de baixo ou o restante do while e voltar pro inicio do 'while True' e continuar recebendo valores no input ate ser um valor válido

        if 1 <= numero_escolhido <= 15:
            return numero_escolhido
        
        print("O número escolhido", numero_escolhido, "é inválido. Entre com um valor inteiro entre 1 e 15.")

def validar_numero(numero_sorteado, numero_escolhido, tentativas_restantes):
    if numero_escolhido == numero_sorteado:
        print("Parabens! O numero sorteado foi:", numero_sorteado, "e o número escolhido foi", numero_escolhido)
        return True

    elif numero_escolhido > numero_sorteado:
        print("O chute", numero_escolhido, "é maior! Restam", tentativas_restantes, "tentativas.")
        return False

    elif numero_escolhido < numero_sorteado:
        print("O chute", numero_escolhido, "é menor! Restam", tentativas_restantes, "tentativas.")
        return False

numero_sorteado = random.randint(1, 15)

chances = 3

for i in range(chances):

    tentativas_restantes = (chances - i) - 1
    numero_escolhido = get_input()

    if validar_numero(numero_sorteado, numero_escolhido ,tentativas_restantes): # Se validar_numero for verdadeiro é pra parar
        break

else: # 'Else' do 'for'
    print("Suas tentativas acabaram!")

print("Número sorteado", numero_sorteado)
