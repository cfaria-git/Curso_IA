#Entrada de dados
nomeAluno = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
nota4 = float(input("Digite a quarta nota do aluno: "))

#Execução de calcula
media = (nota1 + nota2 + nota3 + nota4) / 4

#Exibe o resultado
print (f"A média do aluno {nomeAluno} é {media}")

if media >= 6:
    print("Parabéns! Aluno está aprovado") 
else:
    print("Aluno está reprovado")

