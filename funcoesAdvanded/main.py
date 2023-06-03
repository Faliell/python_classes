"""Function: Native, modules, code"""

""" parameters live inside functions (this is their natural environment)
    arguments exist outside functions, and are carriers of values passed to
 corresponding parameters."""


# Parameter and Var == ????
def message(number):
    print("Enter a number:", number)

number = 1234
message(1)
print(number)

# The parameter named number is a completely different entity
# from the variable named number.

#Positional parameter
def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)

#Keyword argument
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")


#Mixing positional and keyword arguments

#you have to put positional arguments before keyword arguments.
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(3, c = 1, b = 2)

#default (predefined) values
def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction("James", "Doe")





