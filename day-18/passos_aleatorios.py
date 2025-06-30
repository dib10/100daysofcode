import random
import turtle

tortuguita = turtle.Turtle()
colours = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']

direcoes = [0, 90, 180, 270]

tortuguita.pensize(15)

for _ in range(200):
    tortuguita.color(random.choice(colours))
    tortuguita.forward(30)
    tortuguita.setheading(random.choice(direcoes))
