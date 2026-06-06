import requests as rq

nome = input("Digite o seu nome")
cep = input("Digite o CEP de sua residencia: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = rq.get(url)

resposta = dados.json()

print(f"Você mora na rua {resposta['logradouro']}, no bairo {resposta["bairro"]}, na cidade de {resposta["localidade"]} e no estado de {resposta["estado"]}")