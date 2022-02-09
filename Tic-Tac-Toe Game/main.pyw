from tkinter import *
window = Tk()
window.minsize(width=282, height=390)
window.maxsize(width=282, height=390)
window.title('Tic-Tac-Toe Game')
show = 'Player 1 Turn'
var = 1

def btn1():
    global var
    if var==1:
        var = 0
        btn1.config(text='X')
        ent.delete(0, END)
        ent.insert(END, 'Player 2 Turn')
    elif var==0:
        btn1.config(text='O')
        var = 1
        ent.delete(0, END)
        ent.insert(END, 'Player 1 Turn')
    btn1.config(state=DISABLED)

def btn2():
    global var
    if var==1:
        btn2.config(text='X')
        var = 0
        ent.delete(0, END)
        ent.insert(END, 'Player 2 Turn')
    elif var==0:
        btn2.config(text='O')
        var = 1
        ent.delete(0, END)
        ent.insert(END, 'Player 1 Turn')
    btn2.config(state=DISABLED)
    
def btn3():
    global var
    if var==1:
        btn3.config(text='X')
        var = 0
        ent.delete(0, END)
        ent.insert(END, 'Player 2 Turn')
    elif var==0:
        btn3.config(text='O')
        var = 1
        ent.delete(0, END)
        ent.insert(END, 'Player 1 Turn')
    btn3.config(state=DISABLED)

def btn4():
    global var
    if var==1:
        btn4.config(text='X')
        var = 0
        ent.delete(0, END)
        ent.insert(END, 'Player 2 Turn')
    elif var==0:
        btn4.config(text='O')
        var = 1
        ent.delete(0, END)
        ent.insert(END, 'Player 1 Turn')
    btn4.config(state=DISABLED)

def btn5():
    global var
    if var==1:
        btn5.config(text='X')
        var = 0
        ent.delete(0, END)
        ent.insert(END, 'Player 2 Turn')
    elif var==0:
        btn5.config(text='O')
        var = 1
        ent.delete(0, END)
        ent.insert(END, 'Player 1 Turn')
    btn5.config(state=DISABLED)

def btn6():
    global var
    if var==1:
        btn6.config(text='X')
        var = 0
        ent.delete(0, END)
        ent.insert(END, 'Player 2 Turn')
    elif var==0:
        btn6.config(text='O')
        var = 1
        ent.delete(0, END)
        ent.insert(END, 'Player 1 Turn')
    btn6.config(state=DISABLED)

def btn7():
    global var
    if var==1:
        btn7.config(text='X')
        var = 0
        ent.delete(0, END)
        ent.insert(END, 'Player 2 Turn')
    elif var==0:
        btn7.config(text='O')
        var = 1
        ent.delete(0, END)
        ent.insert(END, 'Player 1 Turn')
    btn7.config(state=DISABLED)

def btn8():
    global var
    if var==1:
        btn8.config(text='X')
        var = 0
        ent.delete(0, END)
        ent.insert(END, 'Player 2 Turn')
    elif var==0:
        btn8.config(text='O')
        var = 1
        ent.delete(0, END)
        ent.insert(END, 'Player 1 Turn')
    btn8.config(state=DISABLED)

def btn9():
    global var
    if var==1:
        btn9.config(text='X')
        var = 0
        ent.delete(0, END)
        ent.insert(END, 'Player 2 Turn')
    elif var==0:
        btn9.config(text='O')
        var = 1
        ent.delete(0, END)
        ent.insert(END, 'Player 1 Turn')
    btn9.config(state=DISABLED)

def restart():
    global var
    ent.delete(0, END)
    ent.insert(END, 'Player 1 Turn')
    btn1.config(text='', state=NORMAL)
    btn2.config(text='', state=NORMAL)
    btn3.config(text='', state=NORMAL)
    btn4.config(text='', state=NORMAL)
    btn5.config(text='', state=NORMAL)
    btn6.config(text='', state=NORMAL)
    btn7.config(text='', state=NORMAL)
    btn8.config(text='', state=NORMAL)
    btn9.config(text='', state=NORMAL)
    var = 1

def checkresult():
    if (btn1['text']=='X' and btn2['text']=='X' and btn3['text']=='X' or
        btn4['text']=='X' and btn5['text']=='X' and btn6['text']=='X' or
        btn7['text']=='X' and btn8['text']=='X' and btn9['text']=='X' or
        btn1['text']=='X' and btn4['text']=='X' and btn7['text']=='X' or
        btn2['text']=='X' and btn5['text']=='X' and btn8['text']=='X' or
        btn3['text']=='X' and btn6['text']=='X' and btn9['text']=='X' or
        btn1['text']=='X' and btn5['text']=='X' and btn9['text']=='X' or
        btn3['text']=='X' and btn5['text']=='X' and btn7['text']=='X'):
        ent.delete(0, END)
        ent.insert(END, 'Player 1 Won')

    elif (btn1['text']=='X' and btn2['text']=='X' and btn3['text']=='X' or
        btn4['text']=='X' and btn5['text']=='X' and btn6['text']=='X' or
        btn7['text']=='X' and btn8['text']=='X' and btn9['text']=='X' or
        btn1['text']=='X' and btn4['text']=='X' and btn7['text']=='X' or
        btn2['text']=='X' and btn5['text']=='X' and btn8['text']=='X' or
        btn3['text']=='X' and btn6['text']=='X' and btn9['text']=='X' or
        btn1['text']=='X' and btn5['text']=='X' and btn9['text']=='X' or
        btn3['text']=='X' and btn5['text']=='X' and btn7['text']=='X'):
        ent.delete(0, END)
        ent.insert(END, 'Player 2 Won')
    else:
        ent.delete(0, END)
        ent.insert(END, 'Draw')

# Player Turn Indentifier
ent = Entry(window, font=('Arial', 20, 'bold'),bd=2, width=17, justify=CENTER)
ent.place(x=10, y=10)
ent.insert(END, 'Player 1 Turn')

# button 1
btn1 = Button(window, text='', font=('Arial', 30, 'bold'),bd=4, width=3, command=btn1, bg='white')
btn1.place(x=8, y=60)
# button 2
btn2 = Button(window, text='', font=('Arial', 30, 'bold'),bd=4, width=3, command=btn2, bg='white')
btn2.place(x=98, y=60)
# button 3
btn3 = Button(window, text='', font=('Arial', 30, 'bold'),bd=4, width=3, command=btn3, bg='white')
btn3.place(x=188, y=60)
# button 4
btn4 = Button(window, text='', font=('Arial', 30, 'bold'),bd=4, width=3, command=btn4, bg='white')
btn4.place(x=8, y=150)
# button 5
btn5 = Button(window, text='', font=('Arial', 30, 'bold'),bd=4, width=3, command=btn5, bg='white')
btn5.place(x=98, y=150)
# button 6
btn6 = Button(window, text='', font=('Arial', 30, 'bold'),bd=4, width=3, command=btn6, bg='white')
btn6.place(x=188, y=150)
# button 7
btn7 = Button(window, text='', font=('Arial', 30, 'bold'),bd=4, width=3, command=btn7, bg='white')
btn7.place(x=8, y=240)
# button 8
btn8 = Button(window, text='', font=('Arial', 30, 'bold'),bd=4, width=3, command=btn8, bg='white')
btn8.place(x=98, y=240)
# button 9
btn9 = Button(window, text='', font=('Arial', 30, 'bold'),bd=4, width=3, command=btn9, bg='white')
btn9.place(x=188, y=240)
# Restart
restart = Button(window, text='Restart', font=('book antiqua', 16, 'bold'), command=restart, bg='light green')
restart.place(x=10, y=335)
# CheckResult
checkresult = Button(window, text='Check Result', font=('book antiqua', 16, 'bold'), command=checkresult, bg='light blue')
checkresult.place(x=122, y=335)

window.mainloop()