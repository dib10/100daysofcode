import random
import os
from arte import logo

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
def deal_card(): 
    '''Retorna uma carta aleatória do baralho'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''Pega uma lista de cartas e retorna a pontuação calculada'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Empate"
    elif computer_score == 0:
        return "Você perdeu, o computador tem um Blackjack"
    elif user_score == 0:
        return "Você ganhou com um Blackjack"
    elif user_score > 21:
        return "Você perdeu, ultrapassou 21"
    elif computer_score > 21:
        return "Você ganhou, o computador ultrapassou 21"
    elif user_score > computer_score:
        return "Você ganhou"
    else:
        return "Você perdeu"

def play_game():
    print(logo)
    print("Bem-vindo ao Blackjack")
    #distribuindo cards
    user_cards = []
    computer_cards = []
    is_game_over = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        print(f" Suas cartas: {user_cards}, pontuação: {user_score}")
        print(f" Cartas do computador: {computer_cards[0]}") #para mostrar apenas a primeira carta do computador
        computer_score = calculate_score(computer_cards)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should = input("Deseja comprar mais uma carta? (s/n): ")
            if user_should == "s":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Suas cartas: {user_cards}, pontuação: {user_score}")
    print(f"Cartas do computador: {computer_cards}, pontuação: {computer_score}")
    print(compare(user_score, computer_score))

while input("Você quer jogar BlackJack? (s/n):") == "s":
    clear_terminal()
    play_game()