# %%

nome_arquivo = "historia.txt"

# %%

# 1 - Abre o arquivo para trabalho

open_file = open(nome_arquivo)
print(open_file)

# %%

# 2 - Leitura do conteudo do arquivo

conteudo = open_file.read()
print(conteudo)

# %%

# 3 - Caso outra aplicação precise usar o arquivo é interessante que ele esteja fechado e disponivel para trabalho, sem perigo de corromper o arquivo.

open_file.close()

# %%

# Forma simplificada e ideal.

# Abre o arquivo com o 'with', atribui o arquivo a variável 'open_file', depois acessa o conteudo usando o 'read' e por fim quando sair do 'with' ja vai encerrar com o 'close' de forma automatica.

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)