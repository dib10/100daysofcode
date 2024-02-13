# Passo 3
import random
from importacao import estados
from importacao import lista_palavras
# ou seja o sétimo estado é o jogo perdido
# Lista de palavras
# Escolha aleatória de uma palavra da lista
palavra_escolhida = random.choice(lista_palavras)
# Comprimento da palavra escolhida
comprimento_palavra = len(palavra_escolhida)
# Código de teste para exibir a solução (apenas para testes)
# Criar espaços em branco para exibir as letras a serem adivinhadas
exibicao = []
for _ in range(comprimento_palavra):
    exibicao += "_"
vidas = 6
print(estados[vidas]) 
# Variável para verificar se o jogo acabou
fim_do_jogo = False
while not fim_do_jogo:
    palpite = input("Adivinhe uma letra: ").lower()
    # Verifique a letra adivinhada
    for posicao in range(comprimento_palavra):
        letra = palavra_escolhida[posicao]
        # print(f"Posição atual: {posicao}\n Letra atual: {letra}\n Letra adivinhada: {palpite}")
        if letra == palpite:
            exibicao[posicao] = letra
    if palpite not in palavra_escolhida:
        vidas -= 1
        print(estados[vidas])
        print(f'Você possui', vidas, 'vidas')

        if vidas == 0:
            fim_do_jogo = True
            print("Você perdeu.")
    exibicao_formatada = " ".join(exibicao) #aqui eu transformo a lista em uma string, "" é o separador e join é o método que transforma a lista em string
    print(exibicao_formatada)
    # Verifique se não há mais "_" restantes em 'display'. Todas as letras foram adivinhadas.
    if "_" not in exibicao:
        fim_do_jogo = True
        print("Você venceu.")
    if vidas == 0:
        fim_do_jogo = True
        print("Você perdeu.")
