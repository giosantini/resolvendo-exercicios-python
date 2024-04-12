n1 = int(input("digite o primeiro numero: "))
n2 = int(input("digite o segundo numero: "))

#escolhendo as opções 
print("escolha uma opção: ")
print("1.Soma")
print("2.Subtração")
print("3.Divisão")
print("4.Multiplicação")

opcao = int(input("digite um numero de operação: "))

if opcao == 1:
    resultado = n1 + n2
    operacao = "Soma"

elif opcao == 2:
    resultado = n1 - n2
    operacao = "Subtração"

elif opcao == 3:
    resultado = n1 / n2
    operacao = "Divisao"

elif opcao == 4:
    resultado = n1 * n2
    operacao = "Multiplicação"

else:
    print("Opção invalida")
    exit()

print("O resultado da conta é: ", operacao, "é: ", resultado)


