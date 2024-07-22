import random
import turtle

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

turtle.colormode(255)

tortuguita = turtle.Turtle()
tortuguita.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        tortuguita.color(random_color())
        tortuguita.circle(100)
        tortuguita.setheading(tortuguita.heading() + size_of_gap)
        tortuguita.circle(100)

draw_spirograph(5)