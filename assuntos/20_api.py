# %%

# Como faço pra acessar o link da url?

import requests # biblioteca para fazer requisições na web
import json # Para tratar listas/dicionarios para arquivos json
from tqdm import tqdm # pra usar tem que dar um 'pip install tqdm' no terminal cmd
import pandas as pd

# %%

url = "https://viacep.com.br/ws/58102337/json/" # Link que queremos fazer a requisição

resposta = requests.get(url) # Obtem a resposta da requisição da url

# %%

# Observe que quando pedimos a resposta da requisição que criamos ela retorna com algum tipo de status se deu certo ou errado, no exemplo nós tivemos o status:
#   <Response [200]>
# Esse tipo de status '200' significa que a resposta da requisição que fizemos foi de sucesso ou OK e está me retornando os dados que eu pedi.

resposta.json() # 'json' serve para retornar o que tem dentro da requisição em forma de 'json', isso se eu tenho certeza que o retorno da requisição é um 'json' 

# %%

dados = resposta.json()
dados

# %%

ceps = [
    "58102337",
    "13329120",
    "19060100",
    "01311902",
]

url = "https://viacep.com.br/ws/{cep}/json/" # '{cep}' é como se fosse um parametro que vamos passar

dados = []

for i in tqdm(ceps): # Navego em todos os ceps da minha lista de ceps, o 'tqdm' cria a barra de progresso do for
    resposta = requests.get(url.format(cep = i)) # Obtenho a resposta pro cep em especifico
    if resposta.status_code == 200: # Verifico se a resposta da requisição foi '200' ou OK
        dados.append(resposta.json()) # Se foi 200 eu vou pegar a resposta , transformar em json e adicionar na minha lista de dados.

dados

# %%

# Criar um data set com os dados e transformar em um csv

data_set = pd.DataFrame(dados)
data_set.to_csv("ceps.csv", sep = ";")

# %%

# Salvar os dados em um arquivo json

print(dados)

with open("ceps.json", "w", encoding='utf-8') as open_file: # nós abrimos o arquivo "ceps.json" em modo write com enconding 'utf-8'
    json.dump(dados, open_file, ensure_ascii = False, indent = 4) # Em seguida uso a bibliota json utiliza o metodo dump, passa os dados que quero fazer o dump o arquivo que abrimos para fazer a escrita, 'ensure_ascii = False' serve para ignorar a tabela ascii de caracteres e não bugar os acentos/caracteres especiais e por fim o ident serve para formar o arquivo
