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

