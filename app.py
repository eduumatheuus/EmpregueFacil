import streamlit as st
import requests
from request import app_id, api_key  

st.set_page_config(
    page_title="EmpregueFacil - Sistema de Recomendação de Vagas",
    page_icon=":briefcase:",  # Pode ser um emoji ou um caminho para um ícone
    layout="wide"  # Ou "centered" para centralizar o conteúdo
)

st.title('EmpregueFacil - Sistema de Recomendação de Vagas')
st.text('Feito por Eduardo Matheus')

app_id = app_id
api_key = api_key

def buscar_vagas(what, where):
    url = f"https://api.adzuna.com/v1/api/jobs/br/search/1?app_id={app_id}&app_key={api_key}&results_per_page=30&what={what}&where={where}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()['results']
    else:
        st.error("Erro ao buscar vagas")
        return []


what = st.text_input("Cargo ou Palavra-Chave", "Auxiliar")
where = st.text_input("Localização", "Uberlândia")


if st.button("Buscar Vagas"):
    vagas = buscar_vagas(what, where)
    
    if vagas:
        for vaga in vagas:
            st.subheader(vaga['title'])
            st.text(f"Empresa: {vaga['company']['display_name']}")
            st.text(f"Local: {vaga['location']['display_name']}")
            st.text(vaga['description'])
            st.markdown(f"[Link para a vaga]({vaga['redirect_url']})")
    else:
        st.write("Nenhuma vaga encontrada.")

