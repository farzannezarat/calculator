from my_function import *


a = 1
result = 0
while a == 1:
    number_operator1 = input("enter first number,operator,second number: ").split(',')
    try:
        len_n = len(number_operator1)
        if len_n > 1 ^ len_n < 3:
            number_operator = number_operator1[1]
            if number_operator == '+':
                z = int(number_operator1[0])
                x = int(number_operator1[-1])
                result = plus(z, x)
                print(result)

            elif number_operator == '-':
                z = int(number_operator1[0])
                x = int(number_operator1[-1])
                result = minus(z, x)
                print(result)

            elif number_operator == '/':
                z = int(number_operator1[0])
                x = int(number_operator1[-1])
                result = division(z, x)
                print(result)

            elif number_operator == 'x':
                z = int(number_operator1[0])
                x = int(number_operator1[-1])
                result = multiplication(z, x)
                print(result)

            elif number_operator == 'xx':
                z = int(number_operator1[0])
                x = int(number_operator1[-1])
                result = power(z, x)
                print(result)

            elif number_operator == '//':
                z = int(number_operator1[0])
                x = int(number_operator1[-1])
                result = square_root(z, x)
                print(result)
    except IndexError:
        print('enter a valid format and operator')

    exit_or_continue = input('for continue press c and for exit press x or enter :')
    if exit_or_continue == 'c':
        pass
    else:
        a = 0
