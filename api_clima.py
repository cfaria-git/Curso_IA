
import requests #Biblioteca de requisições
import os #Biblioteca de sistema

#api_key = os.getenv("OPENWEATHER_API-KEY")

api_key = "64e1988a78c3a19208e9cb2771c25118"
cidade = "Americana"

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt"

dados = requests.get(url)

resposta = dados.json()

temperatura_atual = resposta['main']['temp']
umidade = resposta['main']['humidity']

#Faz a leitura de uma descricao dentro de uma lista dentro de uma 
descricao = resposta['weather'][0]['description']

print(f"A temperatura atual em {cidade} é {temperatura_atual}°C, e a umidade está em {umidade} e o {descricao}")