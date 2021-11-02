while True:
    try:
        def plus():
            result = first_number + second_number
            return result
        def minus():
            result = first_number - second_number
            return result
        def multiplication():
            result = first_number / second_number
            return result
        def division():
            result = first_number / second_number
            return result

        first_number = int(input("enter your first number: "))
        work = input("what work + - x /: ")
        second_number = int(input("enter your second number: "))
        if work == '+':
            print(plus())
        elif work == '-':
            print(minus())
        elif work == 'x':
            print(multiplication())
        elif work == '/':
            print(division())
        else:
            print('enter a valid letter')    

    except ValueError:
        exception = 'please enter a number:'
        print(exception)



