# %%

texto = "Meu novo arquivo."

nome_arquivo = "historia_02.txt"

with open(nome_arquivo, mode = "w") as open_file: # Usa o mode igual a 'w' para escrever no arquivo.
    open_file.write(texto)
