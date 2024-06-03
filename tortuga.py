#importar modulo da tartaruga
import turtle

#criar uma tartaruga

tortuguita = turtle.Turtle()
tortuguita.shape("turtle")
tortuguita.color("red")
tortuguita.speed(1)

screen = turtle.Screen()


#programa
for i in range(4):
    tortuguita.forward(100)
    tortuguita.right(90)

turtle.done()