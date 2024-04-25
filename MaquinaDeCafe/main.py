from  art import logo

print("Bem vindo(a) a máquina de café! ☕️")
print(logo)

MENU = {
    "espresso": {
        "ingredientes": {
            "água": 50,
            "café": 18,
        },
        "custo": 1.5,
    },
    "latte": {
        "ingredientes": {
            "água": 200,
            "leite": 150,
            "café": 24,
        },
        "custo": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "água": 250,
            "leite": 100,
            "café": 24,
        },
        "custo": 3.0,
    }
}

recursos = {
    "água": 300,
    "leite": 200,
    "café": 100,
}

def exibir_sabores():
    for i, sabor in enumerate(MENU,start=1): #sabor é o que itera sobre o dicionário MENU
        print(f"{i}. {sabor} - \033[92mR${MENU[sabor]['custo']}\033[0m")
    int(input("Digite o número correspondente ao café desejado:"))


exibir_sabores()