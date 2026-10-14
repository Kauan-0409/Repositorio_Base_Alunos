import streamlit as st
st.title("Tabuada")
st.subheader("Tabuada do 1 ao 100")

tabuada = st.number_input("Digite o número da tabuada desejada: ")

if st.button("Calcular"):
    for i in range(1,101):
        st.text(f"{i} X {tabuada} = {i * tabuada}")
elif tabuada == 67.67:
    st.image("https://i.pinimg.com/736x/37/a4/ee/37a4ee572bd7f2cb6c357c8f4c69bcd7.jpg")
