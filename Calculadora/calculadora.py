from art import logo
print(logo)

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
def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    #imprimir as operações
    print("Digite a operação desejada: ")
    for i in operacao:
        print(i)
    deve_continuar = True
    while deve_continuar:
        simbolo = input("Digite o simbolo da operação: ")   
        num2 = float(input("Digite o próximo número: "))
        calcula = operacao[simbolo]
        resposta = calcula(num1,num2)
        print(f"{num1} {simbolo} {num2} = {resposta}")
        if input(f"Deseja continuar a operação com o resultado {resposta}? (s/n): ") == 's':
            num1 = resposta
        else:
            deve_continuar = False
            calculadora()

calculadora()
        