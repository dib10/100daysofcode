from arte import logo
import os
print(logo)
print("Bem-vindo ao leilão secreto!")
lances = {}
#funcao para limpar terminal
def clear():
    print("\n" * 100)
continuar = "sim"
while continuar =="sim":
    nome = input("Qual é o seu nome?: ")
    valor = int(input("Qual é o seu lance?:R$ "))
    lances[nome] = valor
    clear()  # Limpa a tela aqui
    continuar = ""
    while continuar != "sim" and continuar != "não":
        continuar = input("Há mais alguém para dar um lance? Digite apenas 'sim' ou 'não': ").lower()
#Função que verifica o maior lance
def maior_lance(lance):
    maior = 0
    for valor in lance:
        if lance[valor]> maior:
            maior = lance[valor]
            nome = valor
    print(f"O maior lance foi de R${maior} e foi dado por {nome}.")
    print("O leilão acabou!")
    print(logo)
maior_lance(lances)
print(lances) # para eu conferir se o dicionário está correto