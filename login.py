print("-" * 20)
print("SISTEMA DE AUTENTICAÇÃO")
print("-" * 20)
#Entrada das informações
nomeUsuario = input("Digite o seu nome: ")
senhaUsuario= input("Digite a sua senha: ")

#Processamento e exibição das informações
if nomeUsuario == "Cleiton" and senhaUsuario == "1234":
    print("Acesso liberado")
else:
    print("Usuário ou senha incorreto. Verifique !!")
