import streamlit as st

st.set_page_config(
    page_title="Drive Style",
    page_icon="logo.png"
)

#---------------- sidebar

st.sidebar.title("Drive Style - Aluguel de Carros")

carros = ["Chevrole Vectra", "Chevrole Opala 71", "VW voyage G1", "VW Saveiro G3", "Supra MK5", "VW Santana Quantum"]
carro = st.sidebar.selectbox("Escolha o carro que deseja alugar", carros)

#---------------- body
st.title("Drive Style - Aluguel de Carros")
st.image(f"{carro}.png")
st.write(f"Você alugou o {carro}")

dias = st.text_input(f"Por quantos dias você alugou o {carro}?")
km = st.text_input(f"Quantos km você rodou com o {carro}?")

if carro == "Chevrole Vectra":
    diaria = 150

elif carro == "Chevrole Opala 71":
    diaria = 550

elif carro == "VW voyage G1":
    diaria = 180

elif carro == "VW Saveiro G3":
    diaria = 130

elif carro == "VW Santana Quantum":
    diaria = 150

elif carro == "Supra MK5":
    diaria = 950

if st.button("Calcular"):
    dias = int(dias)
    km = float(km)

    total = (dias * diaria) + (km * 0.15)
    
    st.warning(f"O total do aluguel a se pagar é R${total}")