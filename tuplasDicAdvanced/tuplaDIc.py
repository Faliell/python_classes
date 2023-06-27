school_class = {}

while True:
    name = input("Digite o nome do aluno: ")
    if name == '':
        break

    score = int(input("Insira a pontuação do aluno (0-10): "))
    if score not in range(0, 11):
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
    counter += 1
    print(name, ":", adding / counter)