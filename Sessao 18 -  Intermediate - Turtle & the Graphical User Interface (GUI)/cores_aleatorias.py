import random
import turtle

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

tortuguita = turtle.Turtle()
turtle.colormode(255)

direcoes = [0, 90, 180, 270]

tortuguita.pensize(15)

for _ in range(200):
    tortuguita.color(random_color())
    tortuguita.forward(30)
    tortuguita.setheading(random.choice(direcoes))
