print("-" * 15)
print("# CALCULADORA #")
print("-" * 15)
      
#Entrada dos dados
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
operacao = input("Qual operacao matematica (+,-,*,/) desejar utilizar ?: ")

#Execução e exibição das informações
if operacao == "+":
    resultado = valor1 + valor2
    print(f"O Resultado é {resultado}")
else:
    if operacao == "-":
        resultado = valor1 - valor2
        print(f"O Resultado é {resultado}")
    else:
        if operacao == "*":
            resultado = valor1 * valor2
            print(f"O Resultado é {resultado}")
        else:
            if operacao == "/":
                resultado = valor1 / valor2
                print(f"O Resultado é {resultado:.2f}")
            else:
                print("operacao invalida")