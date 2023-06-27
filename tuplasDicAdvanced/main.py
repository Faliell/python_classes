#declarar tupla:
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125


#tupla de 1 elemento
one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,

#tupla não tem 'append'

#O q tupla pode?
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

####
var = 123

t1 = (1,)
t2 = (2,)
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)


#Dicionários

"""  
1-cada chave deve ser única - não é possível ter 
mais de uma chave com o mesmo valor;
2-uma chave pode ser qualquer tipo imutável de objeto:
pode ser um número (inteiro ou flutuante), ou até mesmo uma string, mas não uma lista;
3-um dicionário não é uma lista - uma lista contém um conjunto de valores numerados,
enquanto um dicionário contém pares de valores;
4-a função len() também funciona para dicionários,
ela retorna o número de elementos de valor-chave no dicionário;
5- um dicionário é uma ferramenta de mão única.Se você tiver um dicionário
inglês-francês, poderá procurar equivalentes em francês dos termos em inglês,
mas não vice-versa."""


"""No Python, os dicionários 3.6x tornaram-se coleções ordenadas por padrão.
Seus resultados podem variar dependendo da versão do Python que você está usando."""

# metodo key:
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

# metodo items
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)

# metodo values
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}

for french in dictionary.values():
    print(french)

#sorted
for key in sorted(dictionary.keys()):
    print(key)

#update
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
dictionary.update({"pato": "canard"})
print(dictionary)

#del
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
del dictionary['cachorro']
print(dictionary)

#popitem
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
dictionary.popitem()
print(dictionary)  # saídas: {'gato': 'chat', 'cachorro': 'chien'}

#get
pol_eng_dictionary = {"zamek": "castelo", "woda": "água", "gleba": "solo"}

item_1 = pol_eng_dictionary["gleba"]  # ex. 1
print(item_1)  # saídas: solo

item_2 = pol_eng_dictionary.get("woda")  # ex. 2
print(item_2)  # saídas: água

#update
pol_eng_dictionary = {"kwiat": "flor"}
pol_eng_dictionary.update({"gleba": "solo"})
print(pol_eng_dictionary)

#converter:
tuple()
list()

# in
pol_eng_dictionary = {"zamek": "castelo", "woda": "água", "gleba": "solo"}

if "zamek" in pol_eng_dictionary:
    print("Sim")
else:
    print("Não")

#del e clear
pol_eng_dictionary = {"zamek": "castelo", "woda": "água", "gleba": "solo"}

print(len(pol_eng_dictionary))  # saídas: 3
del pol_eng_dictionary["zamek"]  # remover um item
print(len(pol_eng_dictionary))  # saídas: 2

pol_eng_dictionary.clear()  # remove todos os itens
print(len(pol_eng_dictionary))  # saídas: 0

del pol_eng_dictionary  # remove o dicionário

#copy
pol_eng_dictionary = {"zamek": "castelo", "woda": "água", "gleba": "solo"}
copy_dictionary = pol_eng_dictionary.copy()














