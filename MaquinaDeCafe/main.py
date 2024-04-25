from  art import logo

print("Bem vindo(a) a máquina de café!")
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
    print("Escolha um café: ")
    for sabor in MENU: #sabor é o que itera sobre o dicionário MENU
        print(f"{sabor} - \033[92mR${MENU[sabor]['custo']}\033[0m")
exibir_sabores()