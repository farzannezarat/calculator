from my_function import *

a = 1
while a:
    try:
        first_number = int(input("enter your first number: "))
        operator = input("what work + - x / xx //: ")

        if operator == '+':
            second_number = int(input("enter your second number: "))
            print(plus(first_number, second_number))
        elif operator == '-':
            second_number = int(input("enter your second number: "))
            print(minus(first_number, second_number))
        elif operator == 'x':
            second_number = int(input("enter your second number: "))
            print(multiplication(first_number, second_number))
        elif operator == '/':
            second_number = int(input("enter your second number: "))
            print(division(first_number, second_number))
        elif operator == 'xx':
            second_number = int(input("enter your second number: "))
            print(power(first_number, second_number))

        elif operator == '//':
            second_number = int(input("enter your second number: "))
            print(square_root(first_number, second_number))

        else:
            print('enter a valid letter')
    except ValueError:
        exception = 'please enter a number'
        print(exception)
    exit_or_continue = input('for continue press c and for exit press x or enter :')
    if exit_or_continue == 'c':
        pass
    else:
        a = 0
        break
