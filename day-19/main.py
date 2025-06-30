from turtle import Turtle, Screen

tartaruga = Turtle()
screen = Screen()

def avancar_frente():
    tartaruga.forward(10)

def avancar_baixo():
    tartaruga.backward(10)

def virar_direita():
    nova_posicao = tartaruga.heading() - 10
    tartaruga.right(10)

def virar_esquerda():
    nova_posicao = tartaruga.heading() + 10
    tartaruga.left(10)

def clear():
    tartaruga.clear()
    tartaruga.penup()
    tartaruga.home()
    tartaruga.pendown()
screen.listen()
screen.onkey(avancar_frente, "w")
screen.onkey(avancar_baixo, "s")
screen.onkey(virar_direita, "d")
screen.onkey(virar_esquerda, "a")
screen.onkey(clear, "c")

screen.exitonclick()
