import streamlit as st

from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv

load_dotenv()

#Criacao do agente com base na Tupla "()" sem alteracao de informações
agente = Agent(
    model= OpenAIChat(id="gpt-4o-mini"),
    description="Você é um professor de Python",
    tools=[DuckDuckGoTools(),WikipediaTools()],
    markdown=True
) 

#Cricao do frontend
st.title("Agente de I.A 🤖")

pergunta = st.chat_input("Digite a sua pergunta")

if pergunta:
    with st.chat_message("user"):
        st.markdown(pergunta)
    with st.chat_message("assistant"):
        with st.spinner("Em processamento..."):
            resposta = agente.run(pergunta)
            st.markdown(resposta.content)
        