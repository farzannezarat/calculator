from tkinter import *
from my_function import *

window = Tk()
window.title('calculator v2.0')
window.geometry('400x500')
window.resizable(width=False, height=False)
window.config(bg='orange')


def number_operator2():
    number_operator1 = (int(first_number_e.get()), work_e.get(), int(second_number_e.get()))
    try:
        # len_n = len(number_operator1)
        # if len_n > 1 ^ len_n < 3:
        number_operator = number_operator1[1]
        if number_operator == '+':
            z = number_operator1[0]
            x = number_operator1[-1]
            result = plus(z, x)
            result_label1.config(text=result)
        elif number_operator == '-':
            z = number_operator1[0]
            x = number_operator1[-1]
            result = minus(z, x)
            result_label1.config(text=result)

        elif number_operator == '/':
            z = number_operator1[0]
            x = number_operator1[-1]
            result = division(z, x)
            result_label1.config(text=result)

        elif number_operator == 'x':
            z = number_operator1[0]
            x = number_operator1[-1]
            result = multiplication(z, x)
            result_label1.config(text=result)

        elif number_operator == 'xx':
            z = number_operator1[0]
            x = number_operator1[-1]
            result = power(z, x)
            result_label1.config(text=result)

        elif number_operator == '//':
            z = number_operator1[0]
            x = number_operator1[-1]
            result = square_root(z, x)
            result_label1.config(text=result)
        else:
            result_label1.config(text='enter a valid letter')
    except IndexError:
        result_label1.config(text='enter a valid format and operator')


def clear():
    first_number_e.delete(0, END)
    second_number_e.delete(0, END)
    work_e.delete(0, END)
    result_label1.config(text='')


Label(window, text='first number', bg='orange').place(x=80, y=5)
first_number_e = Entry(window, font=5)
first_number_e.place(x=35, y=35, width=150, height=30)


Label(window, text='second number', bg='orange').place(x=227, y=5)
second_number_e = Entry(window, font=5)
second_number_e.place(x=209, y=35, width=150, height=30)


Label(window, text='work', bg='orange').place(x=185, y=5)
work_e = Entry(window, font=5)
work_e.place(x=187, y=35, width=20, height=30)


result_label1 = Label(window, text='', font=('', 40), bg='orange')
result_label1.place(x=35, y=250)

result_label2 = Label(window, text='', font=('', 40), bg='orange')
result_label2.place(x=35, y=320)

result_btn = Button(window, text='result', command=number_operator2)
result_btn.place(x=150, y=90)

clear_btn = Button(window, text='clear', command=clear)
clear_btn.place(x=200, y=90)


window.mainloop()
