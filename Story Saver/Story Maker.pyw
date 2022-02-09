# Importing Import Modules
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog as openbox
import win32print



# start = time.time()
win = Tk()
win.minsize(width=800, height=500)
win.geometry('810x500')
win.title("Untitled - StoryPad")

win.config(bg='white')

# Text Editor Text Attributes
font_ = 'consolas'
type_ = 'italic'
size_ = 12

# Main Window Option Windows Attributes
btn_font = 'consolas'
btn_size = 10
btn_type = 'bold'

text_width = 10


f_name = 'Untitled - StoryPad'

def no_response():
    pass

def get_dim():
    global width, height
    width =win.winfo_width()
    height = win.winfo_height()

def closing_try():
    close = Toplevel()
    close.grab_set()
    close.title("Warning")
    close.geometry('280x100+600+250')
    close.configure(bg='white')
    close.resizable(False, False)
    close.attributes("-topmost", True)
    # close.eval('tk::PlaceWindow . center')

    def save_b_func():
        close.destroy()
        save_func()
        win.destroy()

    def dont_save_b_func():
        close.destroy()
        win.destroy()

    def cancel_b_func():
        close.destroy()

    
    ask_lbl = Label(close, text='''Do You Want to Save File Before
Exiting?''', bg='white', font=('consolas', 10, 'normal'))
    ask_lbl.place(x=30, y=5)
    save_b = Button(close, text='Save', font=('consolas', 10, 'normal'), command=save_b_func, bg='white', width=10).place(x=9, y=50)
    dont_save_b = Button(close, text="Don't Save", font=('consolas', 10, 'normal'), command=dont_save_b_func, bg='white', width=10).place(x=100, y=50)
    cancel_b = Button(close, text='Cancel', font=('consolas', 10, 'normal'), command=cancel_b_func, bg='white', width=10).place(x=190, y=50)

    close.mainloop()

def closing_try_non_func(event):
    closing_try()

def open_func():
    open_file_window = openbox.askopenfile(title='Select File to Open', filetypes=(('All Files', '*.*'),('Text Files', '*.txt')))
    if open_file_window is not None:
        global file_path
        global text_file
        file_path = open_file_window.name
        text_file = open(file_path, 'r')
        txt = text_file.read()
        f_name = file_path.rindex('/')
        f_name = file_path[f_name+1:]
        f_name = f_name[:-4]
        win.title(f'{f_name} - StoryPad')
        text.delete(1.0, END)
        text.insert(END, txt)


def save_func():
    global file_path
    txt = text.get('1.0', END)
    if 'file_path' in globals():
        save_file = Toplevel()
        save_file.grab_set()
        save_perm = 'no'
        save_file.title('Save')
        save_file.geometry('200x80+600+250')
        save_file.resizable(False, False)
        save_file.attributes("-topmost", True)
        # save_file.eval('tk::PlaceWindow . center')
        save_file.configure(bg='white')

        def yes_func():
            global save_perm
            save_perm = 'yes'
            save_file.destroy()
            text_file = open(file_path, "w+")
            text_file.write(txt)
            text_file.close()

        def no_func():
            global save_perm
            save_perm = 'no'
            save_file.destroy()


        save_text = Label(save_file, text='Do You Want to Save File', font=('consolas', 10, 'normal'), bg='white')
        save_text.place(x=10, y=5)

        save_yes = Button(save_file, text='Yes', font=('consolas', 10, 'normal'),bg='white', command=yes_func, width=8)
        save_yes.place(x=20, y=40)

        save_no = Button(save_file, text='No', font=('consolas', 10, 'normal'), bg='white', command=no_func, width=8)
        save_no.place(x=110, y=40)

        save_file.mainloop()

        if save_perm=='yes':
            pass
        else:
            return
    else:
        global text_file
        text_savefile_window = openbox.asksaveasfile(initialfile = 'Untitled.txt',title='Select Name and Path', defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if text_savefile_window is not None:
            file_path = text_savefile_window.name
            text_file = open(file_path, "w+")
            text_file.write(txt)
            text_file.close()
            f_name = file_path.rindex('/')
            f_name = file_path[f_name+1:]
            f_name = f_name[:-4]
            win.title(f'{f_name} - StoryPad')

def save_as_func():
    global text_file, file_path
    save_as_window = openbox.asksaveasfile(initialfile = 'Untitled.txt',title='Select Name and Path', defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if save_as_window is not None:
        file_path = save_as_window.name
        text_file = open(file_path, "w+")
        text_file.write(txt)
        text_file.close()
        f_name = file_path.rindex('/')
        f_name = file_path[f_name+1:]
        f_name = f_name[:-4]
        win.title(f'{f_name} - StoryPad')


def reset_func():
    global file_path, txt, text_file
    reset = Toplevel()
    reset.grab_set()
    reset.geometry('190x90+600+250')
    reset.title("Warning")
    reset.config(bg='white')
    reset.attributes('-topmost', True)
    reset.resizable(False, False)

    def yes_func():
        global file_path, txt, text_file
        text.delete(1.0, END)
        if 'file_path' in globals():
            del file_path
        if 'txt' in globals():
            del txt
        if 'text_file' in globals():
            del text_file
        win.title('Untitled - StoryPad')
        reset.destroy()

    def no_func():
        reset.destroy()

    reset_lbl = Label(reset, bg='white',font=('consolas', 10, 'normal'),text='''Do You Really Want to
Reset Text Data?''')
    reset_lbl.place(x=20, y=0)

    yes_btn = Button(reset, text='Yes', font=('consolas', 10, 'normal'), width=8, bg='white', command=yes_func)
    yes_btn.place(x=20, y=40)

    no_btn = Button(reset, text='No', font=('consolas', 10, 'normal'), width=8, bg='white', command=no_func)
    no_btn.place(x=105, y=40)

    reset.mainloop()


def print_func():
    print = Toplevel()
    print.grab_set()
    print.title("Confirmation")
    print.geometry('190x90+600+250')
    print.resizable(False, False)
    print.attributes('-topmost', True)
    print.config(bg='white')

    def fin_print():
        printer_s = win32print.OpenPrinter(win32print.GetDefaultPrinter())
        win32print.StartDocPrinter(printer_s, 1, ("Print", None, 'RAW'))
        win32print.WritePrinter(printer_s, bytes(text.get(1.0, END).encode('utf-8', 'ignore')))
        win32print.EndDocPrinter(printer_s)
        win32print.GetJob(printer_s, 1, 'JobInfo', 'JOB_CONTROL_LAST_PAGE_EJECTED')
        win32print.ClosePrinter(printer_s)
        print.destroy()

    print_lbl = Label(print, text='''Do You Really Want to 
Print Text?''', font=('consolas', 10, 'normal'), bg='white')
    print_lbl.place(x=20, y=0)

    print_yes = Button(print, text='Yes', font=('consolas', 10, 'normal'), bg='white', width=8, command=fin_print)
    print_yes.place(x=20, y=40)

    print_no = Button(print, text='No', font=('consolas', 10, 'normal'), bg='white', width=8, command=print.destroy)
    print_no.place(x=105, y=40)

    print.mainloop()
     

def cut_func():
    sel_text = text.selection_get()
    win.clipboard_clear()
    win.clipboard_append(sel_text)
    text.delete(SEL_FIRST, SEL_LAST)

def clip_func():
    sel_text = text.selection_get()
    win.clipboard_clear()
    win.clipboard_append(sel_text)

def paste_func():
    ind = text.index(INSERT)
    copied_text = win.clipboard_get()
    text.insert(ind, copied_text)

def replace_func():
    replace = Toplevel()
    replace.grab_set()
    replace.configure(bg='white')
    replace.title("Replace")
    replace.geometry('170x170+600+250')
    replace.config(bg='white')
    replace.resizable(False, False)
    # replace.eval('tk::PlaceWindow . center')
    replace.attributes("-topmost", True)
    def ok_func():
        global before_word
        global after_word
        global txt
        before_word = before_entry.get()
        after_word = after_entry.get()
        unedited = text.get(1.0, END)
        txt = unedited.replace(before_word, after_word)
        text.delete(1.0, END)
        text.insert(END, txt)
        replace.grab_release()
        replace.destroy()

    def close_release_replace():
        replace.grab_release()
        replace.destroy()

    before_label = Label(replace, text='Word to be Replaced', font=('consolas', 10, 'normal'), bg='white').place(x=10, y=0)
    before_entry = Entry(replace, font=('consolas', 10, 'italic'), width=20, bd=2)
    before_entry.place(x=10, y=25)
    after_label = Label(replace, text='Word to Replace With', font=('consolas', 10, 'normal'), bg='white').place(x=10, y=60)
    after_entry = Entry(replace, font=('consolas', 10, 'italic'), width=20, bd=2)
    after_entry.place(x=10, y=85)
    ok_button = Button(replace, text='Ok',font=('consolas', 10, 'normal'), command=ok_func, bg='white', width=8).place(x=10, y=120)
    cancel_button = Button(replace, text='Cancel', font=('consolas', 10, 'normal'), command=replace.destroy, bg='white', width=8).place(x=90, y=120)
    
    replace.protocol("WM_DELETE_WINDOW", close_release_replace)

    replace.mainloop()

def shortcuts_func():
    shortcuts = Toplevel()
    shortcuts.grab_set()
    shortcuts.geometry('660x660+100+25')
    shortcuts.resizable(False, False)
    shortcuts.title("KeyBoard Shortcuts Documentation")

    def close_release_shortcuts():
        shortcuts.grab_release()
        shortcuts.destroy()

    title = Label(shortcuts, text='             Keyboard Shortcuts                         ', font=('courier', 18, 'bold'), bg='white', fg='purple')
    title.pack(anchor=NW)
    l1 = Label(shortcuts, font=('consolas', 11, 'bold'), text=f"""    
    Home : Move cursor to beginning of current line         
    End : Move cursor to end of current line        
    Ctrl + Home : Move cursor to top of the text entry field        
    Ctrl + End : Move cursor to bottom of the text entry field      
    Page Up : Scrolls Down using Keyboard       
    Page Down : Scrolls Up using Keyboard       
    Shift + ← → - Selecting Text from Left to Right         
    Shift + ↑ ↓ : Selecting Text from Top to Bottom         
    Shift + Ctrl + ← → : Select words from Left to Right        
    Shift + Ctrl + ↑ ↓ : Select paragraphs.         
    Shift + Home : Selects from current to starting of line         
    Shift + End : Selects from current to ending of line        
    Shift + Ctrl + Home : Selecting text from current to Top        
    Shift + Ctrl + End : Selecting text from current to End         
    Shift + Page Down : Selects from current to end of current frame        
    Shift + Page Up : Selects from current to top of current frame          
    Ctrl + A : Select all text.
    Ctrl + C : Copy selected text.
    Ctrl + X : Cut selected text.
    Ctrl + V : Paste text at cursor
    Ctrl + Z : Undo.
    Ctrl + Y : Redo.
    Ctrl + B : Bold.
    Ctrl + I : Italic.
    Ctrl + U : Underline.
    F3 : Find next.
    Shift + F3 : Find previous.
    Ctrl + O : Open.
    Ctrl + S : Save.
    Ctrl + N : New document.
    Ctrl + P : Print.
    Alt + F : Open File menu.
    Alt + E : Open Edit menu.
    Alt + V : Open View menu.
{('    ')*12}{chr(66)}{chr(121)}{chr(32)}{chr(45)}{chr(32)}{chr(66)}{chr(104)}{chr(97)}{chr(118)}{chr(101)}{chr(115)}{chr(104)}{chr(32)}{chr(66)}{chr(97)}{chr(110)}{chr(115)}{chr(104)}{chr(105)}{chr(119)}{chr(97)}{chr(108)}
    """, bg='white', justify=LEFT)
    l1.pack(anchor=NW)

    shortcuts.protocol("WM_DELETE_WINDOW", close_release_shortcuts)

    shortcuts.mainloop()

def about_func():
    about = Toplevel()
    about.grab_set()
    about.title("Build - 0.0.0.0")
    about.attributes('-topmost', True)
    # about.config(bg='white')
    about.resizable(False, False)
    about.geometry('400x300+500+250')
    label1 = Label(about, text="""
Story Saver
Version (Build : 1.0.0.0)
Made By Bhavesh Banshiwal
© CopyRight Bhavesh Banshiwal
""", font=('consolas', 11, 'normal'))
    label1.place(x=80, y=80)


    about.mainloop()

def do_right_click(event):
    right_click.tk_popup(event.x_root, event.y_root)
    right_click.grab_release()

# When User Attemps to Press These Keys func(event) event must be used inside it
win.protocol('WM_DELETE_WINDOW', closing_try)
win.bind('<Escape>', closing_try_non_func)
win.bind('<Button-3>', do_right_click)

right_click = Menu(win, tearoff=0)
right_click.add_command(label="Cut", command=cut_func)
right_click.add_command(label="Copy", command=clip_func)
right_click.add_command(label="Paste", command=paste_func)
right_click.add_separator()
right_click.add_command(label="Reload", command=win.update)

open_button = Button(win, text='Open', font=(btn_font, btn_size, btn_type), width=10, command=open_func)
open_button.place(x=5, y=2)

save_button = Button(win, text='Save', font=(btn_font, btn_size, btn_type), width=10, command=save_func)
save_button.place(x=85, y=2)

save_as_button = Button(win, text='Save As', font=(btn_font, btn_size, btn_type), width=text_width, command=save_as_func)
save_as_button.place(x=165, y=2)

reset_button = Button(win, text='Reset', font=(btn_font, btn_size, btn_type), width=10, command=reset_func)
reset_button.place(x=245, y=2)

print_button = Button(win, text='Print', font=(btn_font, btn_size, btn_type), width=10, command=print_func)
print_button.place(x=325, y=2)

copy_to_clipboard = Button(win, text='Copy', font=(btn_font, btn_size, btn_type), width=text_width, command=clip_func)
copy_to_clipboard.place(x=405, y=2)

paste_from_clipboard = Button(win, text='Paste', font=(btn_font, btn_size, btn_type), width=text_width, command=paste_func)
paste_from_clipboard.place(x=485, y=2)

replace_button = Button(win, text='Replace', font=(btn_font, btn_size, btn_type), width=text_width, command=replace_func)
replace_button.place(x=565, y=2)

shortcuts_button = Button(win, text='Shortcuts', font=(btn_font, btn_size, btn_type), width=text_width, command=shortcuts_func)
shortcuts_button.place(x=645, y=2)

about_button = Button(win, text='About', font=(btn_font, btn_size, btn_type), width=text_width, command=about_func)
about_button.place(x=725, y=2)

# Text Widget
text = ScrolledText(win, font=(font_, size_, type_), wrap=WORD, bd=0, state=NORMAL)
text.pack(expand=True, fill=BOTH, padx=5, pady=(33, 10), side=BOTTOM)

# end = time.time()
# print(f"The Execution Time is {end-start}")
win.mainloop()
# IF main (.win) Window is Closed Then The All windows will close
# and Exit The Program
exit()