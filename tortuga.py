#importar modulo da tartaruga
import turtle

#criar uma tartaruga

tortuguita = turtle.Turtle()
tortuguita.shape("turtle")
tortuguita.color("red")
tortuguita.speed(1)

screen = turtle.Screen()


#programa
tortuguita.setheading(90)
tortuguita.forward(100)
tortuguita.setheading(0)
tortuguita.forward(100)
tortuguita.setheading(270)
tortuguita.forward(100)
tortuguita.setheading(180)
tortuguita.forward(100)
turtle.done()
