from turtle import Turtle, Screen
import random
# ajustes da tela
screen = Screen()
screen.setup(width=500, height=400)

aposta_usuario = screen.textinput("Aposte na sua tartaruga", prompt="Qual cor de tartaruga irá vencer? ")
print(f"A aposta do usuário é: {aposta_usuario}")


class ConfiguracaoTela:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.configurar_tela()

    def configurar_tela(self):
        screen.setup(width=self.largura, height=self.altura)
        screen.title("Corrida de Tartarugas")

# Cria uma instância da configuração da tela
configuracao = ConfiguracaoTela(500, 400)


#classe para tartaruga
class Tartaruga(Turtle):
    def __init__(self, cor, posicao_x, posicao_y):
        super().__init__()
        self.shape("turtle")
        self.color(cor)
        self.penup()
        self.goto(x=posicao_x, y=posicao_y)
        self.pendown()

    def avancar_frente(self):
        distancia_aleatoria = random.randint(0, 10)
        self.forward(distancia_aleatoria)

## objeto tartaruga
tartaruga1 = Tartaruga("red", -240, 100)
tartaruga2 = Tartaruga("blue", -240, 50)
tartaruga3 = Tartaruga("green", -240, 0)
tartaruga4 = Tartaruga("yellow", -240, -50)
tartaruga5 = Tartaruga("purple", -240, -100)

#corrida
tartarugas = [tartaruga1, tartaruga2, tartaruga3, tartaruga4, tartaruga5]
vencedor = False

def iniciar_corrida(): ## principal
    global vencedor
    while not vencedor: ## enquanto não houver vencedor, avançar as tartarugas
        for tartaruga in tartarugas:
            tartaruga.avancar_frente()
            verifica_vencedor()
            if vencedor:
                break



def verifica_vencedor():
    global vencedor
    for tartaruga in tartarugas:
        if tartaruga.xcor() >= 230:
            vencedor = tartaruga.pencolor()
            print(f"A tartaruga {vencedor} venceu a corrida!")

def verifica_aposta():
    if vencedor == aposta_usuario:
        print("Parabéns! Você apostou na tartaruga vencedora!")
    else:
        print(f"Que pena! A tartaruga {vencedor} venceu, mas você apostou na {aposta_usuario}.")
            
# Inicia a corrida
iniciar_corrida()
verifica_aposta()




    