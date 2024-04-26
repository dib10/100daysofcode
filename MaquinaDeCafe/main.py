from  art import logo
from dicionarios import MENU,recursos
import os

print("Recursos disponíveis:")
for item in recursos:
    print(f"{item}: {recursos[item]}ml")

def exibir_sabores():
    for i, sabor in enumerate(MENU,start=1): #sabor é o que itera sobre o dicionário MENU
        print(f"{i}. {sabor} - \033[92mR${MENU[sabor]['custo']}\033[0m")
    try:
        escolha = int(input("Digite o número correspondente ao café desejado:"))
    except ValueError:
        print("Por favor, insira um número.")
        return None
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
            print("\033[91mDesculpe, não há ingredientes suficientes para fazer o café {sabor}.\033[0m")
            return False
    return True
        
def processar(sabor,total_moedas):
    custo = MENU[sabor]['custo']
    if total_moedas >= custo:
        for item in MENU[sabor]['ingredientes']:
            recursos[item] -= MENU[sabor]['ingredientes'][item]
        print('-'*60)
        print(f"Você selecionou {sabor}, que custa \033[92m${custo}\033[0m")
        print(f"Você inseriu \033[92m{round(total_moedas, 2)}\033[0m.")
        troco = round(total_moedas - custo, 2)
        print(f"Seu troco é de \033[92m${troco}\033[0m")
        print('-'*60)
         
        return True
    else:
        print("\033[91mDesculpe, você não inseriu moedas suficientes.\033[0m")
        return False
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#programa principal
def main():
    print("Bem vindo(a) a máquina de café! ☕️")
    print(logo)
    exibir_relatório = input("Deseja ver o relatório de recursos? [1] para sim, [2] para não: ")
    print('-'*60)

    if exibir_relatório == '1':
        print("Recursos disponíveis:")
        for item in recursos:
            if item == 'café':
                print(f"\033[94m{item}: {recursos[item]} g\033[0m")
            else:
                print(f"\033[94m{item}: {recursos[item]} ml\033[0m")
        print('-'*60)

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
        