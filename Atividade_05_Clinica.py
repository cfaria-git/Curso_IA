import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv

load_dotenv()

personalidade = st.sidebar.selectbox("Personalidade", ["Nutricionista", "Persnonal Trainer", "Psicologo"])

#Criacao de um dicionario de dados
descricao = {
    "Nutricionista" : "Especialista em alimentação saudável, sugere receitas e refeições equilibradas", 
    "Personal Trainer" : "Especialista em exercicios fisico, monta treinos e dá dicas de musculção e cardio",
    "Psicologo" : "Especialista em bem-estar mental, dá dicas de gerenciamento de estresse e ansidade"
}

#Criacao do agent
agente = Agent (
    model=OpenAIChat(id="gpt-4o-mini"),
    description=descricao[personalidade],
    tools=[DuckDuckGoTools(), WikipediaTools()],
    markdown=True
)

#Avaliar se a sessão não está vazia
if "Mensagens" not in st.session_state:
    st.session_state.mensagem = []
    
for msg in st.session_state.mensagem:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

#Limpa o historico de conversa
if st.sidebar.button("Limpa conversas"):
    st.session_state.mensagem = []
    st.rerun()
    
st.title("Assitente virtua Clinica Medica Saúde é vida")
pergunta = st.chat_input ("Pergunte ao agente")

if pergunta:
    with st.chat_message("user"):
        st.markdown(pergunta)
        
    st.session_state.mensagem.append({"role":"user","content":pergunta})
    
    with st.chat_message("assistant"):
        with st.spinner("Em processamento ..."):
            resposta = agente.run(pergunta)
            st.markdown(resposta.content)
        
    st.session_state.mensagem.append({"role":"assistant","content":pergunta})