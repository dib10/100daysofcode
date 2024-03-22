from dados import data
from art import logo
import os
import random
def limpar_terminal():
    os.system('cls')  # 'cls' é o comando para limpar o terminal no Windows
def selecionar_dois_itens():
    itens_selecionados = random.sample(data, 2) #sample pega 2 itens aleatorios da lista data
    return itens_selecionados

A, B = selecionar_dois_itens()

def exibir_itens(A,B):
    print(f"A: {A['name']}, {A['description']}, {A['country']}")
    print(logo)
    print(f"B: {B['name']}, {B['description']}, {B['country']}")


def comparar_seguidores(A,B):
    seguidores_A = A['follower_count']
    seguidores_B = B['follower_count']
    if seguidores_A > seguidores_B:
        return 'A'
    else:
        return 'B'

def jogo():
    pontos = 0
    continuar = True
    while continuar:
        limpar_terminal()
        A,B = selecionar_dois_itens()
        exibir_itens(A,B)
        resposta = input("Quem tem mais seguidores? Digite 'A' ou 'B':").upper()
        resultado = comparar_seguidores(A,B)
        if resposta == resultado:
            pontos+=1
            print(f"Você acertou! Pontuação: {pontos}")
        else:
            print(f"Você errou! Pontuação final: {pontos}")
            continuar = False
jogo()



    

