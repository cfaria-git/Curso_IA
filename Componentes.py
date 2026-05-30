import streamlit as st

st.title("Secretária SENAI Americana")
st.subheader("Conheça os nossos cursos")

st.write("I.A Gerenativa, Power BI, Empilhadeira, Excel, Eletricista Instalador")
st.markdown("**Atenção** : Verifique se existe vagas disponiveis")

nome = st.text_input("Digite o seu nome: ")
idade = st.number_input("Digite a sua idade: ", min_value=16, max_value=99)
cursoEscolhido = st.selectbox("Cursos disponiveis", ["I.A Gerenativa", "Power BI", "Empilhadeira", "Excel", "Eletricista Instalador"])
aceitaTermos = st.checkbox("Ao clicar aqui você aceita os termos e condições")

if st.button("Enviar resposta"):
    if nome and idade and cursoEscolhido and aceitaTermos:
        st.success(f"Olá {nome}, você tem {idade} anos e escolheu o curso {cursoEscolhido}")
    else:
        st.error("Ocorreu alguma falha. Verifique!")