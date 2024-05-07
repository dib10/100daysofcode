# from turtle import Turtle, Screen

# timmy = Turtle()  # Aqui, "Turtle" é uma classe e "timmy" é um objeto criado a partir dessa classe.
# print(timmy)

# timmy = Turtle()  # Criando outro objeto da classe "Turtle" e atribuindo-o a "timmy".
# print(timmy)
# timmy.shape("turtle")  # "shape" é um método da classe Turtle. Aqui, estamos chamando o método para mudar a forma do objeto "timmy".
# timmy.color("chocolate")  # "color" é um método da classe Turtle. Aqui, estamos chamando o método para mudar a cor do objeto "timmy".
# timmy.forward(100)  # "forward" é um método da classe Turtle. Aqui, estamos chamando o método para mover o objeto "timmy" para frente.

# my_screen = Screen()  # Aqui, "Screen" é uma classe e "my_screen" é um objeto criado a partir dessa classe.
# print(my_screen.canvheight)  # "canvheight" é um atributo da classe Screen. Aqui, estamos acessando o atributo diretamente.
# my_screen.exitonclick()  # "exitonclick" é um método da classe Screen. Aqui, estamos chamando o método para fechar a tela quando o usuário clicar nela.
from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Nome do Pokemón", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Tipo",["Elétrico","Fogo","Água"])

table.align = "l"

print(table)


