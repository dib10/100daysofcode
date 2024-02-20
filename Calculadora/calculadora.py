#Calculadora

#soma
def soma(n1,n2):
    return n1 + n2

#subtração
def sub(n1,n2):
    return n1 - n2

#multiplicação
def mult(n1,n2):
    return n1 * n2

#divisão
def div(n1,n2):
    return n1 / n2

operacao = {'+': soma, '-':sub, '*':mult, '/':div}

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
#imprimir as operações
print("Digite a operação desejada: ")
for i in operacao:
    print(i)
simbolo = input("Digite o simbolo da operação: ")   
calcula = operacao[simbolo]
resposta = calcula(num1,num2)
print(f"{num1} {simbolo} {num2} = {resposta}")
