import streamlit as st
import pandas as pd

st.set_page_config("Saudades Janaina", layout="wide")

df = pd.read_excel("saeb_aprendizado_territorios-7-2023-EM.xlsx",
sheet_name="estados", engine="openpyxl")

df_filtrado = df[
    (df["uf"].isin(["MG", "BA", "CE", "PR"]))
]

col_filtrado = ["uf", "lingua portuguesa insuficiente", "matematica insuficiente"]

pd.DataFrame(df_filtrado)

st.title("Painel SAEB: Territórios de Aprendizado")
st.header("Davi Fontana")

st.sidebar.header("Painel de Controle")
opcao = st.sidebar.radio("Selecione a visualização: ", ["Tabela", "Gráficos"])

if opcao == "Tabela":
    st.dataframe(df_filtrado, use_container_width=True, hide_index=True, column_order=col_filtrado)

elif opcao == "Gráficos":
    st.bar_chart(df_filtrado, use_container_width=True)

st.text("Fonte: https://www.gov.br/inep ")

st.text("OBS: Sentiremos saudades Jana")