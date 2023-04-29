# If Else observações:

# you mustn't use else without a preceding if;
# else is always the last branch of the cascade, regardless of whether you've used elif or not;
# else is an optional part of the cascade, and may be omitted;
# if there is an else branch in the cascade, only one of all the branches is executed;
# if there is no else branch, it's possible that none of the available branches is executed.

########################################
# # triple """
# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)
# #continue exemplo:
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.")
#
# #While com else:
# i = 1
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else:", i)
#
#
# #Qual a saida?
#
# #Exercicio1:
# x, y, z = 5, 10, 8
#
# print(x > z)
# print((y - 5) == x)
#
# #Exercicio2":
# for i in range(0, 6, 3):
#     print(i)
#
# #Exercicio3:
# n = 3
#
# while n > 0:
#     print(n + 1)
#     n -= 1
# else:
#     print(n)
# #Exercicio4:
# n = range(4)
#
# for num in n:
#     print(num - 1)
# else:
#     print(num)