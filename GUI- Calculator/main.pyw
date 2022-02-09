from tkinter import *
import math

window = Tk()
window.title("Calculator")
window.geometry("620x520")
# I am Going to Put a icon here 
# but i am converting it in exe so i removed icon command
window.minsize(width=620, height=520)
window.maxsize(width=620, height=520)
expression = ''

def num1_func():
    entry1.insert(END, '1')

def num2_func():
    entry1.insert(END, '2')

def num3_func():
    entry1.insert(END, '3')

def num4_func():
    entry1.insert(END, '4')

def num5_func():
    entry1.insert(END, '5')

def num6_func():
    entry1.insert(END, '6')

def num7_func():
    entry1.insert(END, '7')

def num8_func():
    entry1.insert(END, '8')

def num9_func():
    entry1.insert(END, '9')

def num0_func():
    entry1.insert(END, '0')

def not_defined():
    entry1.delete(0, END)
    entry1.insert(0, 'Not Defined')

def equal_func():
    global expression
    expression = entry1.get()
    if '/0' in expression:
        not_defined()
    if 'sin' in expression:
        sin_func()
    if 'cos' in expression:
        cos_func()
    if 'tan' in expression:
        tan_func()
    result = eval(expression)
    entry1.delete(0, END)
    entry1.insert(0, result)
    entry1.update()

def subtract_func():
    entry1.insert(END, '-')

def addition_func():
    entry1.insert(END, '+')

def multiply_func():
    entry1.insert(END, '*')

def divide_func():
    entry1.insert(END, '/')

def decimal_func():
    entry1.insert(END, '.')

def ac_func():
    global expression
    entry1.delete(0, END)

def backspace_func():
    entry1.delete(len(entry1.get())-1, END)

def square_root_func():
    global expression
    entry1.insert(END, '**(1/2)')
    expression = entry1.get()
    result = eval(expression)
    entry1.delete(0, END)
    entry1.insert(0, result)
    entry1.update()

def cube_root_func():
    global expression
    entry1.insert(END, '**(1/3)')
    expression = entry1.get()
    result = eval(expression)
    entry1.delete(0, END)
    entry1.insert(0, result)
    entry1.update()

def sin_func():
    global expression
    expression = entry1.get()
    multiple = expression[0:expression.find('s')]
    angle = expression[expression.find('n')+1:len(expression)]
    angle = int(angle)
    angle = angle * math.pi/180
    multiple = float(multiple)
    value = math.sin(angle)
    expression = value*multiple
    entry1.delete(0, END)
    entry1.insert(END, expression)
    entry1.update()

def cos_func():
    global expression
    expression = entry1.get()
    multiple = expression[0:expression.find('c')]
    angle = expression[expression.find('s')+1:len(expression)]
    angle = int(angle)
    angle = angle * math.pi/180
    multiple = float(multiple)
    value = math.sin(angle)
    expression = value*multiple
    entry1.delete(0, END)
    entry1.insert(END, expression)
    entry1.update()

def tan_func():
    global expression
    expression = entry1.get()
    multiple = expression[0:expression.find('t')]
    angle = expression[expression.find('n')+1:len(expression)]
    angle = int(angle)
    angle = angle * math.pi/180
    multiple = float(multiple)
    value = math.sin(angle)
    expression = value*multiple
    entry1.delete(0, END)
    entry1.insert(END, expression)
    entry1.update()

"""def sin_func():
    global expression
    expression = entry1.get()
    if 'sin0' in expression:
        expression.split('s', 1)
        expression = expression[0]
        expression += '*0'
        expression = eval(expression)
        entry1.delete(0, END)
        entry1.insert(0, expression)
        entry1.update()
    elif 'sin30' in expression:
        expression.split('s', 1)
        expression = expression[0]
        expression += '*1/2'
        expression = eval(expression)
        entry1.delete(0, END)
        entry1.insert(0, expression)
        entry1.update()
    elif 'sin45' in expression:
        expression.split('s', 1)
        expression = expression[0]
        expression += '*1/2**(1/2)'
        expression = eval(expression)
        entry1.delete(0, END)
        entry1.insert(0, expression)
        entry1.update()
    elif 'sin60' in expression:
        expression.split('s', 1)
        expression = expression[0]
        expression += '*3**(1/2)/2'
        expression = eval(expression)
        entry1.delete(0, END)
        entry1.insert(0, expression)
        entry1.update()
    elif 'sin90' in expression:
        expression.split('s', 1)
        expression = expression[0]
        expression += '*1'
        expression = eval(expression)
        entry1.delete(0, END)
        entry1.insert(0, expression)
        entry1.update()
    else:
        entry1.delete(0, END)
        entry1.insert(END, 'Not Valid Angle')

def cos_func():
    global expression
    expression = entry1.get()
    if 'cos0' in expression:
        expression.split('c', 1)
        expression = expression[0]
        expression += '*1'
        expression = eval(expression)
        entry1.delete(0, END)
        entry1.insert(0, expression)
        entry1.update()
    elif 'cos30' in expression:
        expression.split('c', 1)
        expression = expression[0]
        expression += '*3**(1/2)/2'
        expression = eval(expression)
        entry1.delete(0, END)
        entry1.insert(0, expression)
        entry1.update()
    elif 'cos45' in expression:
        expression.split('c', 1)
        expression = expression[0]
        expression += '*1/2**(1/2)'
        expression = eval(expression)
        entry1.delete(0, END)
        entry1.insert(0, expression)
        entry1.update()
    elif 'cos60' in expression:
        expression.split('c', 1)
        expression = expression[0]
        expression += '*1/2'
        expression = eval(expression)
        entry1.delete(0, END)
        entry1.insert(0, expression)
        entry1.update()
    elif 'cos90' in expression:
        expression.split('c', 1)
        expression = expression[0]
        expression += '*0'
        expression = eval(expression)
        entry1.delete(0, END)
        entry1.insert(0, expression)
        entry1.update()
    else:
        entry1.delete(0, END)
        entry1.insert(END, 'Not Valid Angle')

def tan_func():
    global expression
    expression = entry1.get()
    if 'tan0' in expression:
        expression.split('t', 1)
        expression = expression[0]
        expression += '*0'
        expression = eval(expression)
        entry1.delete(0, END)
        entry1.insert(0, expression)
        entry1.update()
    elif 'tan30' in expression:
        expression.split('t', 1)
        expression = expression[0]
        expression += '*1/3**(1/2)'
        expression = eval(expression)
        entry1.delete(0, END)
        entry1.insert(0, expression)
        entry1.update()
    elif 'tan45' in expression:
        expression.split('t', 1)
        expression = expression[0]
        expression += '*1'
        expression = eval(expression)
        entry1.delete(0, END)
        entry1.insert(0, expression)
        entry1.update()
    elif 'tan60' in expression:
        expression.split('t', 1)
        expression = expression[0]
        expression += '*3**(1/2)'
        expression = eval(expression)
        entry1.delete(0, END)
        entry1.insert(0, expression)
        entry1.update()
    elif 'tan90' in expression:
        expression.split('t', 1)
        expression = expression[0]
        expression = 'undefined'
        entry1.delete(0, END)
        entry1.insert(0, expression)
        entry1.update()
    else:
        entry1.delete(0, END)
        entry1.insert(END, 'Not Valid Angle')"""

def sin_add():
    entry1.insert(END, 'sin')

def cos_add():
    entry1.insert(END, 'cos')

def tan_add():
    entry1.insert(END, 'tan')

def pow_func():
    entry1.insert(END, '**')


author = Label(window, text='This Calculator is Made By Bhavesh Bansiwal', font=('Arial', 17, 'normal'))
author.place(x=75, y=85)
entry1 = Entry(window, text='', justify=RIGHT,font=('Arial', 40, 'normal'), width=20, bd=5)
entry1.place(x=13, y=10)
# 1
num1_sign = Button(window, text="1", font=('Arial', 30, 'bold'), width=3, command=num1_func)
num1_sign.place(x=20, y=120)
# 2
num2_sign = Button(window, text="2", font=('Arial', 30, 'bold'), width=3, command=num2_func)
num2_sign.place(x=120, y=120)
# 3
num3_sign = Button(window, text="3", font=('Arial', 30, 'bold'), width=3, command=num3_func)
num3_sign.place(x=220, y=120)
# 4
num4_sign = Button(window, text="4", font=('Arial', 30, 'bold'), width=3, command=num4_func)
num4_sign.place(x=20, y=220)
# 5
num5_sign = Button(window, text="5", font=('Arial', 30, 'bold'), width=3, command=num5_func)
num5_sign.place(x=120, y=220)
# 6
num6_sign = Button(window, text="6", font=('Arial', 30, 'bold'), width=3, command=num6_func)
num6_sign.place(x=220, y=220)
# 7
num7_sign = Button(window, text="7", font=('Arial', 30, 'bold'), width=3, command=num7_func)
num7_sign.place(x=20, y=320)
# 8
num8_sign = Button(window, text="8", font=('Arial', 30, 'bold'), width=3, command=num8_func)
num8_sign.place(x=120, y=320)
# 9
num9_sign = Button(window, text="9", font=('Arial', 30, 'bold'), width=3, command=num9_func)
num9_sign.place(x=220, y=320)
# 0
num0_sign = Button(window, text="0", font=('Arial', 30, 'bold'), width=3, command=num0_func)
num0_sign.place(x=120, y=420)
# '='
equal_sign = Button(window, text="=", font=('Arial', 30, 'bold'), width=3, command=equal_func)
equal_sign.place(x=220, y=420)
# '-'
subtract_sign = Button(window, text="-", font=('Arial', 30, 'bold'), width=3, command=subtract_func)
subtract_sign.place(x=320, y=220)
# '+'
addition_sign = Button(window, text="+", font=('Arial', 30, 'bold'), width=3, command=addition_func)
addition_sign.place(x=320, y=120)
# '*'
multiply_sign = Button(window, text="X", font=('Arial', 30, 'bold'), width=3, command=multiply_func)
multiply_sign.place(x=320, y=320)
# '/'
divide_sign = Button(window, text="/", font=('Arial', 30, 'bold'), width=3, command=divide_func)
divide_sign.place(x=320, y=420)
# '.'
decimal_sign = Button(window, text=".", font=('Arial', 30, 'bold'), width=3, command=decimal_func)
decimal_sign.place(x=20, y=420)
# 'AC'
AC_sign = Button(window, text="AC", font=('Arial', 30, 'bold'), width=3, command=ac_func)
AC_sign.place(x=420, y=220)
# '<-'
backspace_sign = Button(window, text="⌫", font=('Arial', 30, 'bold'), width=3, command=backspace_func)
backspace_sign.place(x=420, y=120)
# square root
square_root_sign = Button(window, text="2√", font=('Arial', 30, 'bold'), width=3, command=square_root_func)
square_root_sign.place(x=420, y=320)
# cube root
cube_root_sign = Button(window, text="3√", font=('Arial', 30, 'bold'), width=3, command=cube_root_func)
cube_root_sign.place(x=420, y=420)
# Sin
sin_sign = Button(window, text='sin', font=('Arial', 30, 'bold'), width=3 , command=sin_add)
sin_sign.place(x=520,y=120)
# Cos
cos_sign = Button(window, text='cos', font=('Arial', 30, 'bold'), width=3, command=cos_add)
cos_sign.place(x=520, y=220)
# Tan
tan_sign = Button(window, text='tan', font=('Arial', 30, 'bold'), width=3, command=tan_add)
tan_sign.place(x=520, y=320)
# Power(^)
pow_sign = Button(window, text='^x', font=('Arial', 30, 'bold'), width=3, command=pow_func)
pow_sign.place(x=520, y=420)
window.mainloop()
