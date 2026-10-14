import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_csv("Tabela_Clubes.csv")

time = st.selectbox(
    "Times:",
    df["Clubes"].unique()
)

ano = st.selectbox(
    "Ano:",
    sorted(df["Ano"].unique(), reverse=True)
)

dados_time = df[
    (df["Clubes"] == time) &
    (df["Ano"] == ano)
]

st.write("Time:", time)
st.write("Ano:", ano)
st.write("Registros encontrados:", len(dados_time))

df["Ano"] = pd.to_numeric(df["Ano"], errors="coerce")

st.title(time)

if not dados_time.empty:
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        with st.container(border=True):
            st.metric("Posição", dados_time["Pos."].iloc[-1])

    with col2:
        with st.container(border=True):
            st.metric("Vitórias", dados_time["Vitorias"].iloc[-1])

    with col3:
        with st.container(border=True):
            st.metric("Empates", dados_time["Empates"].iloc[-1])

    with col4:
        with st.container(border=True):
            st.metric("Derrotas", dados_time["Derrotas"].iloc[-1])
else:
    st.warning("Nenhum dado encontrado para esse time e ano.")

st.subheader("Estatísticas completas")

st.dataframe(
    dados_time[
        ["Ano", "Pos.", "GolsF/S", "Saldo",
         "Qtd_Jogadores", "Idade_Media",
         "Estrangeiros", "Valor_total", "Media_Valor"]
    ],
    hide_index=True,
    use_container_width=True
)