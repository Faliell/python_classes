lista = []
for i in range(10):
    lista.append(i)
print(lista)

lista2 = [x for x in range(10)]
print(lista2)

lista3 = [x + 2 for x in lista]
print(lista3)

############################################
#nested lista bidimensional:

board = [[i for i in range(8)] for j in range(8)]
print(board)

##########################################