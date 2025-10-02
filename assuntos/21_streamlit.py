# %%

# Como rodar o codigo com streamlit?
# Roda o comando 'streamlit run 21_streamlit.py'

import streamlit as st
import pandas as pd
import requests

url = "https://viacep.com.br/ws/{cep}/json/"

st.title("Buscar CEP")

cep = st.text_input("Busque seu cep")

if cep != "":

    try:
        resp = requests.get(url.format(cep=cep))
        data = pd.DataFrame([resp.json()])
        st.dataframe(data, hide_index = True)

    except Exception as err:
        st.error("Entre com um cep válido.")
