from datetime import time
import numpy as np
import pandas as pd
import streamlit as st
from annotated_text import annotated_text
st.set_page_config(
    page_title="Denis Zorzetti Valim",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://denisvalim.streamlit.app',
        'Report a bug': "https://denisvalim.streamlit.app/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.subheader("Seja bem vindo!")
st.write("Esse site tem como objetivo mostrar meu conhecimento em desenvovimento de WebApps em Python.")
st.subheader('Principais skills')
annotated_text(
    ("Digital Solutions", " "),
    " | ", ("Desenvolvedor Python ",""),
    " | ",("Analista de Dados  ","*"),
    " | ",("Automação  ", " "),
    " | ",("Desenvolvedor Blockchain", " "),
    "."
)
def stream_data():
    # Gerar palavras uma por uma com delay
    for word in texto_resumo.split(" "):
        yield word + " "
        time.sleep(0.02)

texto_resumo = """
Profissional com grande aptidão em desenvolvimento, com foco na solução de problemas de negócios, experiência de mais de 18 anos no ramo automobilístico e toda cadeia logística. Conhecedor de diversas linguagens de programação: Python, SQL, HTML, RPA, JavaScript, VBA, Solidity, Node.js e JSON. Capacitado em análise de dados e desenvolvimento de automação de relatórios e dashboards, com conhecimento em programação de Smart Contracts na rede Ethereum. Habilidades avançadas em softwares corporativos (SAP - MM, SD e WM, formação ABAP na academia SAP), desenvolvimento de scripts via VBA, Excel Avançado e Python, utilização de ferramentas de business intelligence (Power BI, QLink), GKO (pagamentos de fretes) e SharePoint. Atualmente me dedico a adquirir novos conhecimentos na tecnologia de blockchain voltada ao setor logístico.
"""
st.subheader('Resumo profissional')
with st.container(border=True):
    st.write(stream_data())



