from math import sqrt


operators = {'plus': '+',
             'minus': '-',
             'multiplication': 'x',
             'division': '/',
             'power': 'xx',
             'sqrt': '//'}


def plus(first_number, second_number):
    result = first_number + second_number
    return result


def minus(first_number, second_number):
    result = first_number - second_number
    return result


def multiplication(first_number, second_number):
    result = first_number * second_number
    return result


def division(first_number, second_number):
    result = first_number / second_number
    return result


def power(first_number, second_number):
    result = first_number ** second_number
    return result


def square_root(first_number, second_number):
    result = f"first number square root is {sqrt(first_number)}\nsecond number square root is {sqrt(second_number)}"
    return result
