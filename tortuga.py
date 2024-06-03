#importar modulo da tartaruga
import turtle

#criar uma tartaruga

tortuguita = turtle.Turtle()
tortuguita.shape("turtle")
tortuguita.color("red")
tortuguita.speed(1)

screen = turtle.Screen()


#programa
for i in range(10):
    tortuguita.forward(10)
    tortuguita.penup()
    tortuguita.forward(10)
    tortuguita.pendown()

turtle.done()