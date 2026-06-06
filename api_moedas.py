#Api que realiza a conversão de entre moedas

import requests

#URL da api
url = "https://api.exchangerate-api.com/v4/latest/BRL";

dados = requests.get(url)

resposta = dados.json()

#Realiza a busca de informações dentre do dicionario secundário
valor_moeda_base = resposta['rates']['BRL']

valor_dolar = resposta['rates']['USD']
valor_euro = resposta['rates']['EUR']

#realizando a conversão de moedas
dolar = valor_moeda_base / valor_dolar 
euro = valor_moeda_base / valor_euro 

print(f"Conversão de valores: 1 Real corresponde a {euro:.2f} euros")