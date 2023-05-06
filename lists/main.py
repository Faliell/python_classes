"""Um método é um tipo específico de função - ele se comporta
como uma função e se parece com uma função,
mas difere na maneira como age e em seu estilo de invocação.

Uma função não pertence a nenhum dado ‒ ela obtém dados,
pode criar novos dados e (geralmente) produz um resultado.

Um método faz todas essas coisas, mas também é capaz de alterar o estado
de uma entidade selecionada.

Um método é propriedade dos dados para os quais trabalha,
enquanto uma função é propriedade de todo o código."""

#function:
#result = function(arg)
#method:
#result = data.method(arg)

#list Method:
#list.append(value)
#list.insert(location, value)

#funcion
#len(list)

###########################################
variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1
###########################################
#reverter lista:
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)
################################################
length = len(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

#################################################
'''A lista é um tipo de dados em Python usado para armazenar vários objetos.
 É uma coleção ordenada e mutável de itens separados por vírgula entre colchetes'''

my_list = [1, None, True, 'I am a string', 256, 0]
#################################################
my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # outputs: [1, 2, 4]

del my_list
##################################################
#The bubble sort:

#list.sort()
#list.reverse()

my_list = [8, 10, 6, 2, 4]  # list to sort

for i in range(len(my_list) - 1):
    if my_list[i] > my_list[i + 1]:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

#######################

my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

##########################################################
# Entender listas storage:

list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

'''Os dois nomes (lista_1 e lista_2) identificam o mesmo local
na memória do computador. Modificar um deles afeta o outro e vice-versa.'''

####################################################
#slice:
#my_list[start:end] #pode usar negativo
#my_list[start:len(my_list)] #equivalente
#del my_list[1:3]
#del my_list[:]
#####################################################
#copiar uma lista:

list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

######################################################
#indices negativos:
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']


###################################################

#in e not in
#elem in my_list
#elem not in my_list

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
#######################################################

#exercicio 1:

# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2
#
# del list_1[0]
# del list_2[:]
#
# print(list_3)

####################################################
#exercicio 2

# list_1 = ["A", "B", "C"]
# list_2 = list_1[:]
# list_3 = list_2[:]
#
# del list_1[0]
# del list_2[0]
#
# print(list_3)

####################################################

