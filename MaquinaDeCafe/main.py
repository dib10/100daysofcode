from  art import logo
from dicionarios import MENU,recursos
import os

print("Recursos disponíveis:")
for item in recursos:
    print(f"{item}: {recursos[item]}ml")

def exibir_sabores():
    for i, sabor in enumerate(MENU,start=1): #sabor é o que itera sobre o dicionário MENU
        print(f"{i}. {sabor} - \033[92mR${MENU[sabor]['custo']}\033[0m")
    escolha = int(input("Digite o número correspondente ao café desejado:"))
    if escolha == 1:
        return "espresso"
    elif escolha == 2:
        return "latte"
    elif escolha == 3:
        return "cappuccino"
    else:
        print("Opção inválida.")

def inserir():
    moedas = {
        'Quarters($ 0,25)': 0.25,
        'Dimes($ 0,10)': 0.10,
        'Nickels($ 0,05)': 0.05,
        'Pennies($ 0,01)': 0.01
    }
    total_moedas = 0
    for moeda in moedas:
        total_moedas += int(input(f"Quantas moedas de {moeda} você deseja inserir?")) * moedas[moeda]
    return total_moedas

def verifica_recursos(sabor):
    for item in MENU[sabor]['ingredientes']:
        if MENU[sabor]['ingredientes'][item] > recursos[item]:
            print(f"Desculpe, não há ingredientes suficientes para fazer o café {sabor}.")
            return False
    return True
        
def processar(sabor,total_moedas):
    custo =MENU[sabor]['custo']
    if total_moedas >=custo:
        for item in MENU[sabor]['ingredientes']:
            recursos[item] -=MENU[sabor]['ingredientes'][item]
            print(f"Você selecionou {sabor}, que custa ${custo}")
            print(f"Você inseriu {round(total_moedas, 2)}.")
            print(f"Troco: ${round(total_moedas - custo,2)}")
            return True
    else:
        print("Desculpe, não há dinheiro suficiente.")
        return False
    
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#programa principal
def main():
    print("Bem vindo(a) a máquina de café! ☕️")
    print(logo)
    exibir_relatório = input("Deseja ver o relatório de recursos? [1] para sim, [2] para não: ")
    if exibir_relatório == '1':
        print("Recursos disponíveis:")
        for item in recursos:
            print(f"{item}: {recursos[item]}ml")
    sabor = exibir_sabores()
    if verifica_recursos(sabor):
        total_moedas = inserir()
        if processar(sabor,total_moedas):
            print(f"Aqui está o seu: {sabor} ☕️. Aproveite!")
    continuar = input("Deseja fazer outro café? aperte [1] para sim, e [2] para não: ")
    if continuar == '2':
        return
    else:
        limpar_terminal()

# Loop principal do programa
while True:
    limpar_terminal()
    main()
        