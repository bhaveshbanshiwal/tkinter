from tkinter import *

win = Tk()
win.maxsize(width=330, height=350)
win.minsize(width=330, height=350)
win.title("Seasonal Sales Calculator")
# Calculate Function
def calculate():
    net.config(state=NORMAL)
    amt = base_amount.get()
    net.delete(0, END)
    net.insert(END, amt)
    seas = season.get()
    clot = cloth.get()
    net.insert(END, '-(')
    net.insert(END, amt)
    if seas == 1:
        if clot == 1:
            net.insert(END, '*25/100)')
        else:
            net.insert(END, '*5/100)')
    else:
        if clot == 1:
            net.insert(END, '*20/100)')
        else:
            net.insert(END, '*7/100)')
    cal = net.get()
    cal = eval(cal)
    net.delete(0, END)
    net.insert(END, cal)
    net.insert(0, 'Rs. ')
    net.config(state=DISABLED)
# Entry To Get Base Amount
base_label = Label(win, text='Enter Base Amount -', font=('cambria',12, 'normal')).place(x=10, y=5)
base_amount = Entry(win, text='', font=('cambria', 20, 'normal'), bd=5, width=20)
base_amount.place(x=10, y=30)
# Defining values of RadioButtons
season = IntVar()
cloth = IntVar()
# Making RadioButtons to Choose B/w Seasons
label1 = Label(win, text='Choose Season..', font=('cambria',12, 'normal')).place(x=60, y=80)
season1 = Radiobutton(win, text='Winter', value='1', font=('cambria',12, 'normal'), variable=season).place(x=10, y=110)
season2 = Radiobutton(win, text='Summer', value='0', font=('cambria',12, 'normal'), variable=season).place(x=150, y=110)
label2 = Label(win, text='Choose Cloth Type..', font=('cambria',12, 'normal')).place(x=50, y=150)
cloth1 = Radiobutton(win, text='Cotton', value='1', font=('cambria', 12, 'normal'), variable=cloth).place(x=10, y=180)
cloth1 = Radiobutton(win, text='Woolen', value='0', font=('cambria', 12, 'normal'), variable=cloth).place(x=150, y=180)
# Defining a Image Button
calc = PhotoImage(file='calculate.png')
calculate_button = Button(win, image=calc, command=calculate, borderwidth=0).place(x=70, y=220)
# Entry To Get Output
net = Entry(win, text='', font=('cambria', 20, 'normal'), bd=5, width=20, state=DISABLED)
net.place(x=10, y=290)
total_label = Label(win, text='Total Net Amount - ', font=('cambria', 12, 'normal'))
total_label.place(x=10, y=260)

win.mainloop()