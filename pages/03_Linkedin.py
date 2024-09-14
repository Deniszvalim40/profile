import streamlit as st 

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
st.subheader("Denis Valim")
# Link para o LinkedIn
linkedin_url = "https://www.linkedin.com/in/denis-zorzetti-valim-93608762/"
st.markdown(f'''
    <a href="{linkedin_url}" target="_blank">
        <button style="padding:2px 12px; background-color:#0077b5; color:white; border:none; border-radius:5px; cursor:pointer;">
            Visite meu LinkedIn
        </button>
    </a>
    
    ''', unsafe_allow_html=True)