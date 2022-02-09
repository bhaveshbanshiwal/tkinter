from tkinter import *
import win32api

win = Tk()
win.minsize(width=1280, height=720)
win.geometry('1280x720')
win.title("Asha Mool Restaurant")

total_amount = 0
srl_no = 1

def entry_gst():
    check = per_var.get()
    if check == 1:
        percent_entry.config(state=NORMAL)
    else:
        percent_entry.config(state=NORMAL)
        percent_entry.delete(0, END)
        percent_entry.insert(END, '18')
        percent_entry.config(state=DISABLED)

def discount_rs_check():
    disc_rs = discount_rs_var.get()
    if disc_rs == 1:
        discount_rs_entry.config(state=NORMAL)
    else:
        discount_rs_entry.delete(0, END)
        discount_rs_entry.insert(END, 0)
        discount_rs_entry.config(state=DISABLED)

def save_file():
    global file
    billno = bill_entry.get()
    file = open("billno{}.txt".format(billno),"w+")
    txt = preview.get("1.0", END)
    print(file)
    file.write(txt)
    file.close()

def print_text():
    win32api.ShellExecute(0, "print", file, None, ".", 0)


def submit_details():
    preview.delete('1.0', 'end')
    consumer_name = consumer_entry.get()
    mobile_no = mobile_entry.get()
    gst_no = GST_entry.get()
    gst_in_percentage = percent_entry.get()
    address = address_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    bill_no = bill_entry.get()
    from datetime import date
    today = date.today()
    date = today.strftime("%d/%m/%Y")
    preview.insert('end', 'Ashamool Enterprises')
    preview.insert('end', '\n\nConsumer name : ')
    preview.insert('end', consumer_name)
    preview.insert('end', '\nMobile no : ')
    preview.insert('end', mobile_no)
    preview.insert('end', '\nGST No : ')
    preview.insert('end', gst_no)
    preview.insert('end', '\nGST Amount in % : ')
    preview.insert('end', gst_in_percentage)
    preview.insert('end', '\nAddress : ')
    preview.insert('end', address)
    preview.insert('end', '\nCity : ')
    preview.insert('end', city)
    preview.insert('end', '\nState : ')
    preview.insert('end', state)
    preview.insert('end', '\nBill No : ')
    preview.insert('end', bill_no)
    preview.insert('end', '\nDate : ')
    preview.insert('end', date)
    preview.insert('end', '\n\nProducts List -\n')


def add_product():
    global srl_no
    global total_amount
    product_name = pro_name.get()
    product_price = price.get()
    quantity = qty.get()
    preview.insert('end', '\n\n')
    preview.insert('end', srl_no)
    preview.insert('end', ' :- ')
    preview.insert('end', product_name)
    preview.insert('end', '\n       Price : ')
    preview.insert('end', product_price)
    preview.insert('end', '     Quantity : ')
    preview.insert('end', quantity)
    preview.insert('end', '    Total : ')
    pro_name.delete(0, END)
    price.delete(0, END)
    qty.delete(0, END)   
    a = int(product_price)
    b = int(quantity)
    preview.insert('end', a*b)
    srl_no += 1
    total_amount += a*b
    total_amount_entry.delete(0, END)
    total_amount_entry.insert(END, total_amount)
    

def reset_bill():
    preview.delete('1.0', 'end')


company = Label(win, text='AshaMool Enterprises', font=('cambria', 40, 'bold'), fg='#052aad')
company.place(x=400, y=10)

print_icon = PhotoImage(file='print.png')
print_button = Button(win, image=print_icon, command=print_text)
print_button.place(x=20, y=100)

save_icon = PhotoImage(file='save.png')
save_button = Button(win, image=save_icon)
save_button.place(x=130, y=100)

reset_icon = PhotoImage(file='reset.png')
reset_button = Button(win, image=reset_icon, command=reset_bill).place(x=240, y=100)

preview = Text(win, font='cambria', width=50, bd=2)
preview.place(x=20, y=150)

label1 = Label(win, text='Product Name : ', font=('cambria', 15, 'normal')).place(x=500, y=150)
pro_name = Entry(win, text='', font=('cambria', 15, 'normal'), bd=2, width=32)
pro_name.place(x=640, y=150)

label2 = Label(win, text='Price : ', font=('cambria', 15, 'normal')).place(x=500, y=200)
price = Entry(win, text='', font=('cambria', 15, 'normal'), bd=2, width=8)
price.place(x=570, y=200)

label3 = Label(win, text='Quantity : ', font=('cambria', 15, 'normal')).place(x=750, y=200)
qty = Entry(win, text='', font=('cambria', 15, 'normal'), bd=2, width=13)
qty.place(x=850, y=200)

add_icon = PhotoImage(file='add product.png')
add_prod = Button(win, image=add_icon, command=add_product).place(x=500, y=250)

consumer_label = Label(win, text='Consumer Name : ', font=('cambria', 15, 'normal')).place(x=500, y=300)
consumer_entry = Entry(win, text='', font=('cambria', 15, 'normal'), bd=2, width=30)
consumer_entry.place(x=660, y=300)

mobile_label = Label(win, text='Mobile No. : ', font=('cambria', 14, 'normal')).place(x=500, y=350)
mobile_entry = Entry(win, text='', font=('cambria', 15, 'normal'), bd=2, width=12)
mobile_entry.place(x=610, y=350)

city_label = Label(win, text='City : ', font=('cambria', 15, 'normal')).place(x=770, y=350)
city_entry = Entry(win, text='', font=('cambria', 15, 'normal'), bd=2, width=15)
city_entry.place(x=825, y=350)

GST_label = Label(win, text='GST No. :  ', font=('cambria', 15, 'normal')).place(x=500, y=400)
GST_entry = Entry(win, text='', font=('cambria', 15, 'normal'), bd=2, width=16)
GST_entry.place(x=600, y=400)

state_label = Label(win, text='State : ', font=('cambria', 15, 'normal')).place(x=790, y=400)
state_entry = Entry(win, text='', font=('cambria', 15, 'normal'), bd=2, width=12)
state_entry.place(x=855, y=400)

percent = Label(win, text='GST in % : ', font=('cambria', 15, 'normal')).place(x=500, y=450)
percent_entry = Entry(win, text='18', font=('cambria', 15, 'normal'), bd=2, width=4)
percent_entry.insert(END, '18')
percent_entry.config(state=DISABLED)
percent_entry.place(x=610, y=450)

per_var = IntVar()
per_check = Checkbutton(win, variable=per_var, onvalue=1, offvalue=0, command=entry_gst).place(x=580, y=453)

address_label = Label(win, text='Address : ', font=('cambria', 15, 'normal')).place(x=500, y=500)
address_entry = Entry(win, text='', font=('cambria', 15, 'normal'), bd=2, width=36)
address_entry.place(x=590, y=500)

bill_label = Label(win, text='Bill no : ', font=('cambria', 15, 'normal')).place(x=680, y=450)
bill_entry = Entry(win, text='', font=('cambria', 15, 'normal'), bd=2, width=20, justify=RIGHT)
bill_entry.place(x=765, y=450)

submit_icon = PhotoImage(file='submitur.png')
submit_button = Button(win, image=submit_icon, command=submit_details)
submit_button.place(x=500, y=550)

total_amount = Label(win, text='Total Amount : ', font=('cambria', 15, 'normal')).place(x=20, y=620)
total_amount_entry = Entry(win, text='', font=('cambria', 15, 'normal'), bd=2, width=10)
total_amount_entry.place(x=160, y=620)

discount_rs = Label(win, text='Discount : ', font=('cambria', 15, 'normal')).place(x=290, y=620)
discount_rs_var = IntVar()
discount_rs_check = Checkbutton(win, variable=discount_rs_var, onvalue=1, offvalue=0, command=discount_rs_check).place(x=380, y=623)
discount_rs_entry = Entry(win, text='', font=('cambria', 15, 'normal'), bd=2, width=7)
discount_rs_entry.insert(END, '0')
discount_rs_entry.config(state=DISABLED)
discount_rs_entry.place(x=400, y=620)

recalculate_icon = PhotoImage(file='recalculate.png')
recalculate_button = Button(win, image=recalculate_icon).place(x=800, y=618)

net_amount_label = Label(win, text='Total Net Amount : ', font=('cambria', 15, 'normal')).place(x=500, y=620)
net_amount_entry = Entry(win, text='', font=('cambria', 15, 'normal'), bd=2, width=10)
net_amount_entry.place(x=670, y=620)

win.mainloop()