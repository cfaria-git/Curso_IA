import streamlit as st

from datetime import datetime
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv
import requests

load_dotenv()

personalidade = st.sidebar.selectbox("Personalidade", ["Professor de Python", "Professor de historia", "Cientista maluco", "Economista"])

# #Criando nossas funções (habilidades/skills)
def get_moedas():
    url = "https://api.exchangerate-api.com/v4/latest/BRL"
    try:  
        dados = requests.get(url)
        resposta = dados.json()
        
        #Estamos convertendo o timestamp (segundos) para uma data legivel
        timestamp = resposta['time_last_updated']
        data_convertida = datetime.fromtimestamp(timestamp)
        
        #Conversao de moedas
        dolar = 1 / resposta ['rates']['USD']
        euros = 1 / resposta ['rates']['EUR']
        
        return f"{dolar:.2f} USD 1 BRL | {euros:.2f} EUR = 1 BRL. Dados atualizados em {data_convertida}"
    except:
        return ("Não foi possivel realizar a conversão de valores")

#Criacao de um dicionario de dados
descricao = {
    "Professor de Python" : "Você é um professor de python que responde com exemplo e contexto.", 
    "Professor de historia" : "Você é um professor de historia que ensina de forma clara, simples e objetiva.",
    "Cientista maluco" : "Você é um cientista maluco que sempre está em busca de novas inovações e projetos",
    "Economista" : "Você é um especialista em converter valor monetário e está sem atualizado sobre os valores economicos mundial"
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
        contexto = ""
        
        if personalidade == "Economista":
            if "dolar" in pergunta.lower() or "euro" in pergunta.lower() or "moedas" in pergunta.lower():
            
                if descricao == "Economista":
                    st.subheader ("Eu sou um economista, e poderia ter auxiliar nessa consulta")
                    contexto = f"O valor atual de conversão de USD e EUR para BRL é: {get_moedas()}"
            
            resposta = agente.run(pergunta + contexto)
            st.markdown(resposta.content)
        
    st.session_state.mensagem.append({"role":"assistant","content":pergunta})