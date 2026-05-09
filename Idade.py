import os 

print("=" * 50)
print("Seja bem-vindo ao meu primeiro script Python 🤖")
print("=" * 50)

#Entrada de dados
nome = input("Digite o seu nome: ") #Recebe o nome do usuário
email = input("Digite o seu email: ") #Recebe o email do usuário
cidade = input("Digite a sua cidade: ") #Recebe o estado do usuário
estado = input("Digite o seu estado: ") #Recebe o estado do usuário
pais = input("Digite o seu pais: ") #Recebe o pais do usuário
anoNascimento = int (input("Digite o ano de nascimento: ")) #Padrão camel case
anoAtual = int (input("Digite o ano atual: ")) #Padrão camel case
idade = anoAtual - anoNascimento #Calcula a idade

# Função para limpar a tela
def limpar_tela():
    # Windows: 'nt' | Linux/MacOS: 'posix'
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()

#Exibição das mensagens personalizadas
print (f"Olá {nome}, o seu email é {email}, você mora na cidade de {cidade}, localizado no estado de {estado} e no pais {pais}. A sua idade atual é {idade}")