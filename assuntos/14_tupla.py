# %%

# Tuplas são listas que não podem ser alteradas

tupla_cicero = (32, 1, "solteiro", "Engenheiro de dados Jr")

print(type(tupla_cicero))
print(tupla_cicero)

# %%

# Se eu tentar alterar 1 elemento da tupla que não seja um objeto mutavel (lista e dicionario) da erro, porem se esse elemento for um objeto mutavel (lista e dicionario) é possivel alterar esse elemento dentro da tupla.

print(tupla_cicero[0])

tupla_cicero[0] = 28
