value = int(input('Digite um número natural: '))
print('O recíproco de', value, 'é', 1/value)

"""Traceback (most recent call last):
   File "code.py", line 1, in
    value = int(input('Digite um número natural: '))
ValueError: invalid literal for int() with base 10: ''"""

#a última linha é a mais valiosa

#is
#type(value) is int


#No mundo Python, há uma regra que diz: "É melhor pedir perdão do que pedir permissão".
#try:
     # Esse é um lugar
     # que você pode fazer algo
     # sem pedir permissão.
#except:
     # Esse lugar é dedicado
     # apenas para implorar por persão.


# try:
#     valor= int (input('Insira um número natural:'))
#     print('O recíproco de', valor, 'é', 1 / value)
# except:
#     print('Não sei o que fazer.')

## Tratar exeções:
# try:
#     value = int(input('Digite um número natural: '))
#     print('O recíproco de', value, 'é', 1/value)
# except ValueError:
#     print('Eu não sei o que fazer.')
# except ZeroDivisionError:
#     print('A divisão por zero não é permitida em nosso Universo.')


##acrescentar Anonimo:
# try:
#     value = int (input('Insira um número natural:'))
#     print('O recíproco de', value, 'é', 1 / value)
# except ValueError:
#     print('Não sei o que fazer.' )
# except ZeroDivisionError:
#     print('Divisão por zero não é permitida em nosso universo.')
# except:
#     print('algo de estranho aconteceu aqui ... Desculpe! ')

#Algumas exceções úteis
# ZeroDivisionError
# ValueError
# TypeError
# AttributeError
# SyntaxError


# usar com while
# while True:
#     try:
#         number = int(input("Digite um número int: "))
#         print(5 / number)
#         break
#     except ValueError:
#         print("Valor errado.")
#     except ZeroDivisionError:
#         print("Desculpe. Não consigo dividir por zero.")
#     except:
#         print("eu não sei o que fazer...")


