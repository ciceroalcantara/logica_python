# %%

# Construa um programa que realiza o sorteio de um número entre 1 e 15.

# O usuário terá 3 chances de acertar o valor.

# A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.

# Caso o usuário acerte, dê os parabéns.

# Faça com o streamlit.

import streamlit as st
import random

# Inicializar o número sorteado
if 'numero_sorteado' not in st.session_state: # Primeiro a gente verifica se o numero sorteado existe na 'session_state' que é um dicionário especial do streamlit que mantem as variaveis entre execuções.
    st.session_state.numero_sorteado = random.randint(1, 15) # Se o número não existir ele é criado dentro da session_state
    st.session_state.tentativas = 0 # É criado tambem uma variavel de tentativas que inicia com 0
    st.session_state.jogo_ativo = True # Começamos com o jogo ativo porque o usuario tem 3 tentativas

st.title("Jogo de Sorteio - 3 tentativas!")

if st.session_state.jogo_ativo:
    with st.form("palpite_form"):
        #if st.session_state.jogo_ativo:
        numero_escolhido = st.text_input("Digite um número entre 1 e 15:")
        enviar = st.form_submit_button("Verificar palpite")
        #else:
        #    st.text_input("Jogo encerrado", placeholder="Clique em 'Jogar Novamente'", disabled=False)
        #    enviar = st.form_submit_button("Jogo Encerrado", disabled=True)

        if enviar and numero_escolhido:
            try:
                # Incrementa o número de tentativas
                numero_escolhido = int(numero_escolhido)
                st.session_state.tentativas += 1

                # Mostrar tentativas restantes
                tentativas_restantes = 3 - st.session_state.tentativas
                st.write(f"Tentativas restantes: {tentativas_restantes}")

                # Nesse tercho é feito a validação do numero digitado pelo usuário, primeiro se é um numero entre 1 e 15
                if 1 <= numero_escolhido <= 15:
                    # Caso o numero escolhido seja igual ao numero sorteado o usuario ganha e é exibido uma mensagem de sucesso, o 'jogo_ativo' fica como 'False' e o jogo encerra
                    if numero_escolhido == st.session_state.numero_sorteado:
                        st.success(f"Parabéns! Você acertou! O número era {st.session_state.numero_sorteado}")
                        st.session_state.jogo_ativo = False
                    else:
                        # Nesse trecho verifica se o usuario ja gastou todas as tentativas dele que são 3 e se for maior que 3 o jogo encerra
                        if st.session_state.tentativas >= 3:
                            st.error(f"Game Over! O número era {st.session_state.numero_sorteado}")
                            st.session_state.jogo_ativo = False
                            st.rerun()
                        # Caso o usuario esteja dentro das 3 tentativas o jogo continua e ainda recebe dicas
                        else:
                            if numero_escolhido < st.session_state.numero_sorteado:
                                st.warning("Tente um número MAIOR!")
                            else:
                                st.warning("Tente um número MENOR!")
                # Caso o numero que o usuario digitar não esteja entre 1 e 15 não conta tentativas e é mostrado uma mensagem de erro.
                else:
                    st.error("Por favor, digite um número entre 1 e 15.")
                    st.session_state.tentativas -= 1  # Não conta tentativa inválida
            # Caso o usuario digite uma string não conta tentativa e é apresentado uma mensagem de erro.        
            except ValueError:
                st.error("Por favor, digite um número válido entre 1 e 15.")
                st.session_state.tentativas -= 1  # Não conta tentativa inválida
# Caso o 'jogo_ativo' fique como False o jogo é encerrado 
else:
    st.error(f"Game Over, suas tentativas acabaram! O número era {st.session_state.numero_sorteado}")

# Botão para reiniciar o jogo
if not st.session_state.jogo_ativo:
    if st.button("Jogar Novamente"):
        st.session_state.numero_sorteado = random.randint(1, 15)
        st.session_state.tentativas = 0
        st.session_state.jogo_ativo = True
        st.rerun()
