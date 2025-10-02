# %%

# Funções

# Funções são blocos de código reutilizáveis que realizam uma tarefa específica. 
# Elas ajudam a organizar o código e evitar repetição.

# Sintaxe básica

def funcao(parametros):
    resultado = 1 + parametros
    return resultado

funcao(10)

# %%

# Juros compostos com função

def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """'juros_compostos' serve para calcular o retorno financeiro a partir de um aporte. 
Deve-se considerar como parametros: o valor (aporte), a taxa de juros atual e o tempo, em anos, para calculo do valor a ser retornado.

aporte: 
    um número inteiro que represente o valor em reais.
taxa: 
    um numero float, entre 0 e 1, que represente o valor taxa de juros
anos: 
    um número inteiro maior ou igual a 1 que representa o tempo que o investimento terá liquidez
return: 
    um float
    """
    return aporte * (1 + taxa) ** anos

juros_compostos(1000, 0.13, 4)
# ou
juros_compostos(aporte = 1000, taxa = 0.13, anos = 4)

# %%

# Bom para definir mensagens que são exibidas muitas vezes no código.

def ola_mundo():
    print("Olá mundo!")

ola_mundo()

# %%

# Faça uma função que descubra se o número é par ou impar

def par_impar(numero:int):
    if numero % 2 == 0:
        print("O numero é par!")
    else:
        print("O número é impar!")

numero = input("Entre com um número:")
numero = int(numero)

par_impar(numero)

# %%

# Um exemplo de que pode usar funções dentro de outras funções usando '*args'

def soma(a:float, b:float, *args)->float: # *args são argumentos opcionais e sempre coloca ao final dos argumetos.
    valores = [a, b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args)->float:
    return soma(a, b, *args) / (len(args) + 2)

a = float(input("Digite um valor para 'a':"))
b = float(input("Digite um valor para 'b':"))
c = float(input("Digite um valor para 'c':")) # Esse numero esta indo pra dentro do '*args' as duas outras são obrigatórias.

print("Média:", media(a, b, c))

# %%

# **kwargs (dicionário)
# Criar uma função para calcular o imposto de um determinado produto.

def calc_imposto(preco:float, tx_base:float, **kwargs)->float:
    imposto = preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto

impostos_gerais = {
    "municipio": 0.01, 
    "estadual": 0.005, 
    "nacional": 0.001
}

calc_imposto(100, 0.03, **impostos_gerais)
# ou
calc_imposto(100, 0.03, municipio=0.01, estadual= 0.005, nacional= 0.001)
