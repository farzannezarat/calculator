from my_function_operator import *


operator = None
a = 1
while a == 1:
    number_operator = input("enter first number,operator,second number: ")
    for m in operators:
        w = operators[m]
        len_n = len(number_operator.split(w))
        if len_n > 1:
            operator = number_operator.split(w)
            if w == '+':
                z = int(operator[0])
                x = int(operator[-1])
                print(plus(z, x))

            elif w == '-':
                z = int(operator[0])
                x = int(operator[-1])
                print(minus(z, x))

            elif w == '/':
                z = int(operator[0])
                x = int(operator[-1])
                print(division(z, x))

            elif w == 'x':
                z = int(operator[0])
                x = int(operator[-1])
                print(multiplication(z, x))

            elif w == 'xx':
                z = int(operator[0])
                x = int(operator[-1])
                print(power(z, x))

            elif w == '//':
                z = int(operator[0])
                x = int(operator[-1])
                print(square_root(z, x))
            else:
                print('enter a valid format and operator')

    exit_or_continue = input('for continue press c and for exit press x or enter :')
    if exit_or_continue == 'c':
        pass
    else:
        a = 0
