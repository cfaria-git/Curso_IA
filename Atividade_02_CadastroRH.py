import streamlit as st

st.title("CADASTRADO DO RH 📖")
st.subheader("Página desevolvido por: Cleiton")

nome_funcionario = st.text_input("Digite o nome do funcionário: ")
email_funcionario = st.text_input("Digite o email do funcionário: ")


if st.button("Cadastrar"):
    if nome_funcionario and email_funcionario:
        st.success(f"Cadastro realizado com sucesso")
        #st.snow()
        informacoes = st.text_input("Digite a informaçao desejada: ")
        
    else:
        st.error("Ocorreu algum erro. Preencha as informações!")

