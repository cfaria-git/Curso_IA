import streamlit as st

from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv

load_dotenv()

modeloAgent = st.selectbox("Escolha um dos modelos de IA", ["gpt-4o-mini", "gpt-5.4-mini"])

#MissaoA - Agente responsavel pela criacao de receita
agente = Agent(
    model= OpenAIChat(id=modeloAgent),
    description="Imagine que você é um grande chef e bastante criativo no ramo culinário",
    tools=[DuckDuckGoTools(),WikipediaTools()],
    markdown=True
)

#MissaoB - Agente responsavel por sugerir dicas de viagem
agente1 = Agent(
    model= OpenAIChat(id=modeloAgent),
    description="Sou um especialista em viagem nacional e internacional",
    tools=[DuckDuckGoTools(),WikipediaTools()],
    markdown=True
)

#MissaoC - Agente responsavel por realizar planejamento de estudos
agente2 = Agent(
    model= OpenAIChat(id=modeloAgent),
    description="Imagine que você é um tutor especializado em definir planos de estudos detalhado",
    tools=[DuckDuckGoTools(),WikipediaTools()],
    markdown=True
)

#MissaoD - Agente responsavel por criar historia
agente3 = Agent(
    model= OpenAIChat(id=modeloAgent),
    description="Imagine que você seja uma pessoa bastante criativa capaz de criar pequenas historica com base em poucas informações",
    tools=[DuckDuckGoTools(),WikipediaTools()],
    markdown=True
)

##CRIAÇÃO DO FRONTEND##

st.title("Agente de I.A 🤖")
st.markdown("Agente de IA especializado em: culinária, viagem, estudos e histórias criativas")

pergunta = st.chat_input("Digite a sua pergunta")

#Avaliacao das respostas
if pergunta:
    with st.chat_message("user"):
        st.markdown(pergunta)
    with st.chat_message("assistant"):
        resposta = agente.run(pergunta)
        resposta = agente1.run(pergunta)
        resposta = agente2.run(pergunta)
        resposta = agente3.run(pergunta)
        st.markdown(resposta.content)
