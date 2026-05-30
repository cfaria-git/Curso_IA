import streamlit as st

st.title("Bem ao cardápio da Pizzaria DiPadre 🍕")
st.header("O sabor italiano mais perto de você ")
st.markdown("teste")

st.image("pizza.jpg")
#st.image("https://pixabay.com/pt/images/download/mariya_m-salami-pizza-6593465_1920.jpg")

nomeCliente = st.text_input("Digite o nome: ")
cidade = st.text_input("Digite a cidade: ")
bairro = st.text_input("Digite o bairro: ")
opcoes = st.selectbox("Escolha as nossas opções:", ["Calabresa","Margherita", "Portuguesa", "Quartro queijos"])
aceitaTermos = st.checkbox("Aceita as opções")

if st.button("Enviar pedidos"):
    if nomeCliente and cidade and bairro and opcoes and aceitaTermos:
        st.success("Pedidos enviados com sucesso")
    else:
        st.error("Erro. Verifique as informações")
