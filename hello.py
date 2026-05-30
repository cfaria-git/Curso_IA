import streamlit as st

st.title("Bem-vindo a minha primeira página web")
st.subheader("Desenvolvido por Cleiton")

nome = st.text_input("Digite o seu nome: ")

if nome:
    st.success(f"Bem-vindo {nome}")
    st.balloons()