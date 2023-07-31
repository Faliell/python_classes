# import turtle
#
# tutu = turtle.Turtle()
# tutu.shape("turtle")
# tela = turtle.Screen()
#
# tutu.forward(100)
# tutu.color("blue")
# tela.exitonclick()
# print(tela.canvheight)

from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokemon Name",['Pikachu', 'Bulbasaur', 'Charizard'])
table.add_column("Type",['Elétrico', 'Planta', 'Fogo'])
# alinhar a esquerda:
table.align = "l"
print(table)