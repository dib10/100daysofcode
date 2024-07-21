#importar modulo da tartaruga
import turtle
import random

#criar uma tartaruga
tortuguita = turtle.Turtle()
colours = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']
def desenhar_forma(num_lados):
    angulo = 360 / num_lados
    for _ in range(num_lados):
        tortuguita.forward(100)
        tortuguita.right(angulo)

for shape_side_n in range(3, 11):
    tortuguita.color(random.choice(colours))
    desenhar_forma(shape_side_n)