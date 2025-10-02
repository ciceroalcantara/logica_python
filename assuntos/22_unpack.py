# %%

# Unpacking é a operação de atribuir elementos de uma sequência (lista, tupla, etc.) a variáveis individuais de forma concisa

dados = ["2024-01-01", 1500, "PB"]
data, valor, estado = dados

print(data)    # "2024-01-01"
print(valor)   # 1500
print(estado)  # "SP"

# %%

# Ao ler arquivos CSV ou dados estruturados
linha = ["123", "Cícero Alcântara", "engenheiro de dados", "3000"]

id, nome, cargo, salario = linha
# Agora você tem variáveis nomeadas para trabalhar

# %%

# Resultados de queries SQL
resultado = (1, "2024-01-01", 100.50, "ativo")

id_transacao, data, valor, status = resultado

# %%

# Útil quando você quer separar alguns elementos
dados_completos = ["header", "2024-01-01", 100, 200, 300, "footer"]

cabecalho, data, *valores, rodape = dados_completos

print(valores)  # [100, 200, 300] - lista com os valores do meio

# %%

# Merge de dicionários - útil para configurações
config_base = {"host": "localhost", "port": 5432}
config_db = {"dbname": "data_warehouse", "user": "admin"}

config_completa = {**config_base, **config_db}
# {'host': 'localhost', 'port': 5432, 'dbname': 'data_warehouse', 'user': 'admin'}