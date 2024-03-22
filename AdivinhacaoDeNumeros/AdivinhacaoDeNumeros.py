# Objetivos do Jogo de Adivinhação de Números:

# Incluir um logotipo em arte ASCII.
# Permitir que o jogador envie um palpite para um número entre 1 e 100.
# Verificar o palpite do usuário contra a resposta real. Imprimir "Muito alto." ou "Muito baixo." dependendo da resposta do usuário.
# Se o jogador acertar a resposta, mostrar a resposta real ao jogador.
# Rastrear o número de turnos restantes.
# Se eles ficarem sem turnos, fornecer feedback ao jogador.
# Incluir dois níveis de dificuldade diferentes (por exemplo, 10 tentativas no modo fácil, apenas 5 tentativas no modo difícil).

from art import logo
import random
print("Bem-vindo ao jogo de adivinhação de números!")
print(logo)
print("Estou pensando em um número entre 1 e 100.")
numero_secreto = random.randint(1,100) # Gera um número aleatório entre 1 e 100
print("Número secreto é: ", numero_secreto) # Apenas para testes
dificuldade = input("Escolha um nível de dificuldade. [A] para fácil ou [B] para difícil: ").upper()
if dificuldade == "A":
    tentativas = 10
else:
    tentativas = 5

def adivinhacao():
    global tentativas # Define a variável tentativas como global para que possa ser acessada dentro da função
    while tentativas > 0:
        print(f"Você tem {tentativas} tentativas restantes para adivinhar o número.")
        palpite = int(input("Adivinhe o número:"))
        if palpite == numero_secreto:
            print(f"Você acertou! O número secreto é {numero_secreto}.")
            break
        elif palpite > numero_secreto:
            print("Você chutou mais alto")
        else:
            print("Você chutou mais baixo")
        tentativas -= 1
    if tentativas == 0:
        print("Suas tentativas acabaram. Você perdeu!")
        
adivinhacao()# Chama a função adivinhacao() para iniciar o jogo
        

