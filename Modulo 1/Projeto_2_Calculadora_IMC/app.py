import streamlit as st

#SINDEBAR -------------------------------------------------------------------------------
st.sidebar.title("Calculadora de IMC")
st.sidebar.image("ref.png")
#BODY------------------------------------------------------------------------------------
st.title("Calculadora de IMC")

peso = st.text_input("Digite seu peso: ")
altura = st.text_input("Digite sua altura: ")

if st.button("Calcular"):
    peso = float(peso)
    altura = float(altura)

    imc = peso / (altura ** 2)

    if imc < 18.5:
        class_imc = "abaixo_peso"
        st.warning(f"Seu IMC é {imc:.2f} Você está abaixo do peso")

    elif imc < 24.9:
        class_imc = "peso_saudavel"
        st.success(f"Seu IMC é {imc:.2f} Você tem um peso saudável!")

    elif imc < 29.9:
        class_imc = "sobrepeso"
        st.warning(f"Seu IMC é {imc:.2f} Você está cima do peso")

    elif imc < 34.9 :
        class_imc = "obesidade_1"
        st.warning(f"Seu IMC é {imc:.2f} Você tem obesidade grau 1 ")

    elif imc < 39.9:
        class_imc = "obesidade_2"
        st.error(f"Seu IMC é {imc:.2f} Você tem obdesidade grau 2")
    
    else:
        class_imc = "obesidade_3"
        st.error(f"Seu IMC é {imc:.2f} Você tem obesidade grau 3")

    st.markdown("---")
    
    with open(f"{class_imc}.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
    st.markdown(conteudo)
#python -m streamlit run .\app.py