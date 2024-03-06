############### Projeto Blackjack #####################
#Dificuldade Normal 😎: Use todas as Dicas abaixo para concluir o projeto.
#Dificuldade Difícil 🤔: Use apenas as Dicas 1, 2, 3 para concluir o projeto.
#Dificuldade Extra Difícil 😭: Use apenas as Dicas 1 e 2 para concluir o projeto.
#Dificuldade Especialista 🤯: Use apenas a Dica 1 para concluir o projeto.
############### Regras da Casa do Blackjack #####################
#O baralho é ilimitado em tamanho.
#Não há coringas.
#O Valete/Rainha/Rei contam como 10.
#O Ás pode contar como 11 ou 1.
#Use a seguinte lista como o baralho de cartas:
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#As cartas na lista têm a mesma probabilidade de serem sorteadas.
#As cartas não são removidas do baralho à medida que são sorteadas.
#O computador é o dealer.
##################### Dicas #####################
#Dica 1: Visite este site e experimente o jogo Blackjack:
#https://games.washingtonpost.com/games/blackjack/
#Em seguida, experimente o projeto Blackjack concluído aqui:
#http://blackjack-final.appbrewery.repl.run
#Dica 2: Leia esta quebra de requisitos do programa:
#http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Em seguida, tente criar seu próprio fluxograma para o programa.
#Dica 3: Baixe e leia este fluxograma que criei:
#https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
#Dica 4: Crie uma função deal_card() que usa a lista abaixo para retornar uma carta aleatória.
#11 é o Ás.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#Dica 5: Distribua 2 cartas para o usuário e o computador usando deal_card() e append().
#user_cards = []
#computer_cards = []
#Dica 6: Crie uma função chamada calculate_score() que recebe uma lista de cartas como entrada
#e retorna a pontuação.
#Procure a função sum() para ajudá-lo a fazer isso.
#Dica 7: Dentro de calculate_score(), verifique se é um blackjack (uma mão com apenas 2 cartas: ás + 10) e retorne 0 em vez da pontuação real. 0 representará um blackjack em nosso jogo.
#Dica 8: Dentro de calculate_score(), verifique se há um 11 (ás). Se a pontuação já estiver acima de 21, remova o 11 e substitua-o por um 1. Você pode precisar procurar append() e remove().
#Dica 9: Chame calculate_score(). Se o computador ou o usuário tiverem um blackjack (0) ou se a pontuação do usuário estiver acima de 21, então o jogo termina.
#Dica 10: Se o jogo não tiver terminado, pergunte ao usuário se ele quer tirar outra carta. Se sim, use a função deal_card() para adicionar outra carta à lista user_cards. Se não, então o jogo terminou.
#Dica 11: A pontuação precisará ser reavaliada a cada nova carta tirada e as verificações na Dica 9 precisam ser repetidas até que o jogo termine.
#Dica 12: Assim que o usuário terminar, é hora de deixar o computador jogar. O computador deve continuar tirando cartas enquanto tiver uma pontuação menor que 17.
#Dica 13: Crie uma função chamada compare() e passe a user_score e computer_score. Se o computador e o usuário tiverem a mesma pontuação, então é um empate. Se o computador tiver um blackjack (0), então o usuário perde. Se o usuário tiver um blackjack (0), então o usuário ganha. Se a user_score estiver acima de 21, então o usuário perde. Se a computer_score estiver acima de 21, então o computador perde. Se nenhum dos acima, então o jogador com a pontuação mais alta ganha.
#Dica 14: Pergunte ao usuário se ele quer reiniciar o jogo. Se eles responderem sim, limpe o console e comece um novo jogo de blackjack e mostre o logotipo de art.py.


import random

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
#distribuindo cards
user_cards = []
computer_cards = []
is_game_over = False
for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
user_score = calculate_score(user_cards)
print(f" Suas cartas: {user_cards}, pontuação: {user_score}")
print(f" Cartas do computador: {computer_cards[0]}") #para mostrar apenas a primeira carta do computador
computer_score = calculate_score(computer_cards)






if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True





