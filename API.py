#Passo 1:
#Instalar as biblioteca
#pip install requests

#Segundo passo: adicionar/importar ao codigo
import requests

#Informações para inserção dos dados
nome = input("Digite o seu nome: ")
email = input("Digite o seu email: ")
telefone = input ("Digite o seu telefone: ")
CEP = input(f"Digite o seu CEP: ")

#acionando o link da api
url = f"https://viacep.com.br/ws/{CEP}/json/"

#variavel recebe a informações contidas na varial "url"
dados = requests.get(url).json()

#Filtra das informações
rua = dados['logradouro']
bairro = dados['bairro']
cidade = dados['localidade']

#Exibição das informações. Utilizado o f para adcionar as variaves
print(f"Bem vindo {nome} ao meu sistema de API, você mora na {rua} no bairro {bairro} localizado na cidade {cidade}")