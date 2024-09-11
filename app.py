import streamlit as st
import joblib
import pandas as pd
import numpy as np
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
import importlib


# Configurando a página
st.set_page_config(
    page_title="Ambiente Web",
    page_icon=":rocket:",
    layout="wide"
)

# configura as estilizações
with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home","Informações", "Previsão"],
        icons=["file-text","info-circle-fill", "code-square"],
        menu_icon="list",
        default_index=0
    )

if selected == "Home":
    home = importlib.import_module("home")
    home.run()
elif selected == "Informações":
    informacoes = importlib.import_module("informacoes")
    informacoes.run()
elif selected == "Previsão":
    previsao = importlib.import_module("previsoes")
    previsao.run()



