import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv

load_dotenv()

personalidade = st.sidebar.selectbox("Personalidade", ["Professor de Python", "Professor de historia", "Cientista maluco"])

#Criacao de um dicionario de dados
descricao = {
    "Professor de Python" : "Você é um professor de python que responde com exemplo e contexto.", 
    "Professor de historia" : "Você é um professor de historia que ensina de forma clara, simples e objetiva.",
    "Cientista maluco" : "Você é um cientista maluco que sempre está em busca de novas inovações e projetos"
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
    
for  msg in st.session_state.mensagem:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

#Limpa o historica de conversa
if st.sidebar.button("Limpa conversas"):
    st.session_state.mensagem = []
    st.rerun()
    

st.title("SISTEMA MULTIAGENTE")
pergunta = st.chat_input ("Pergunte ao agente")

if pergunta:
    with st.chat_message("user"):
        st.markdown(pergunta)
        
    st.session_state.mensagem.append({"role":"user","content":pergunta})
    
    with st.chat_message("assistant"):
        resposta = agente.run(pergunta)
        st.markdown(resposta.content)
        
    st.session_state.mensagem.append({"role":"assistant","content":pergunta})