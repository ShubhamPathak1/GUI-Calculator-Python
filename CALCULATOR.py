from tkinter import *

# from PIL import ImageTk, Image

#-----------------------------FUNCITONS DEFINITION---------------
def click(event):
    global inp_var

    bt_text = event.widget.cget('text')   # TO GET THE TEXT OF THE WIDGET

    if bt_text == '=':
        if inp_var.get().isdigit():
            value = int(inp_var.get())

        else:
            try:
                value = eval(inp_entry.get())   # EVAL EVALUATES THE STRING.

            except Exception:
                value = 'Error'


        inp_var.set(value)
        inp_entry.update()

    elif bt_text == 'C':
        inp_var.set('')  # SINCE, "C" MEANS CLEAR, THIS COMMAND WILL CHANGE THE TEXT OF ENTRY WIDGET TO "BLANK".
        inp_entry.update()

    elif bt_text == 'Del':
        def deleter():
            l = len(inp_entry.get())
            inp_entry.delete(l - 1, 'end')
            inp_entry.update()
        deleter()

    else:
        inp_var.set(inp_var.get() + bt_text)  #  TO CONVERT THE TEXT OF ENTRY WIDGET AS PER THE TEXT OF THE BUTTON
        inp_entry.update()  # TO UPDATE THE ENTRY WIDGET WITH THE NEW TEXT

root = Tk()

root.geometry('730x670')
root.maxsize(730, 670)
root.minsize(730, 670)
root.title(" MY CALCULATOR")
root.wm_iconbitmap('1calc.ico')

#-----------------------------INPUT OF USER TO CALCULATE-------------------
inp_var = StringVar()
inp_var.set("")


inp_entry = Entry(root, textvariable=inp_var, font='lucida 40 bold')
inp_entry.pack(fill=X, ipadx=8, pady=10, padx=10)


#--------------------------FRAME FOR ROW-1---------------
f1_r1 = Frame(root, bg='grey', relief=SUNKEN)

# BUTTONS ROW-1
b1 = Button(f1_r1, text='9', font='lucida 35 bold', padx=20, pady=15, relief=RAISED)
b1.pack(side=LEFT, padx=15, pady=10)
b1.bind('<Button-1>', click)

b2 = Button(f1_r1, text='8', font='lucida 35 bold', padx=20, pady=15, relief=RAISED)
b2.pack(side=LEFT, padx=15, pady=10)
b2.bind('<Button-1>', click)

b3 = Button(f1_r1, text='7', font='lucida 35 bold', padx=20, pady=15, relief=RAISED)
b3.pack(side=LEFT, padx=15, pady=10)
b3.bind('<Button-1>', click)

b_add = Button(f1_r1, text='+', font='lucida 35 bold', padx=19, pady=15, relief=RAISED)
b_add.pack(side=LEFT, padx=15, pady=10)
b_add.bind('<Button-1>', click)

bremove = Button(f1_r1, text='Del', font='lucida 35 bold', padx=4, pady=15, relief=RAISED)
bremove.pack(side=LEFT, padx=20, pady=10)
bremove.bind('<Button-1>', click)

f1_r1.pack()

#--------------------------FRAME FOR ROW-2---------------
f1_r2 = Frame(root, bg='grey', relief=SUNKEN)

# BUTTONS ROW-2
b4 = Button(f1_r2, text='6', font='lucida 35 bold', padx=20, pady=15, relief=RAISED)
b4.pack(side=LEFT, padx=15, pady=10)
b4.bind('<Button-1>', click)

b5 = Button(f1_r2, text='5', font='lucida 35 bold', padx=20, pady=15, relief=RAISED)
b5.pack(side=LEFT, padx=15, pady=10)
b5.bind('<Button-1>', click)

b6 = Button(f1_r2, text='4', font='lucida 35 bold', padx=20, pady=15, relief=RAISED)
b6.pack(side=LEFT, padx=15, pady=10)
b6.bind('<Button-1>', click)

b_sub = Button(f1_r2, text='-', font='lucida 34 bold', padx=27, pady=15, relief=RAISED)
b_sub.pack(side=LEFT, padx=15, pady=10)
b_sub.bind('<Button-1>', click)

b3zero = Button(f1_r2, font='lucida 35 bold', padx=1, pady=15, relief=RAISED, text='000')
b3zero.pack(side=LEFT, padx=20, pady=10)
b3zero.bind('<Button-1>', click)


f1_r2.pack()


#--------------------------FRAME FOR ROW-3---------------
f1_r3 = Frame(root, bg='grey', relief=SUNKEN)

# BUTTONS ROW-3
b7 = Button(f1_r3, text='3', font='lucida 35 bold', padx=20, pady=15, relief=RAISED)
b7.pack(side=LEFT, padx=15, pady=10)
b7.bind('<Button-1>', click)

b8 = Button(f1_r3, text='2', font='lucida 35 bold', padx=20, pady=15, relief=RAISED)
b8.pack(side=LEFT, padx=15, pady=10)
b8.bind('<Button-1>', click)

b9 = Button(f1_r3, text='1', font='lucida 35 bold', padx=20, pady=15, relief=RAISED)
b9.pack(side=LEFT, padx=15, pady=10)
b9.bind('<Button-1>', click)

b_mul = Button(f1_r3, text='*', font='lucida 35 bold', padx=24, pady=15, relief=RAISED)
b_mul.pack(side=LEFT, padx=15, pady=10)
b_mul.bind('<Button-1>', click)

b2zero = Button(f1_r3, text='00', font='lucida 35 bold', padx=14, pady=15, relief=RAISED)
b2zero.pack(side=LEFT, padx=20, pady=10)
b2zero.bind('<Button-1>', click)

f1_r3.pack()


#--------------------------FRAME FOR ROW-4---------------
f1_r4 = Frame(root, bg='grey', relief=SUNKEN)

# BUTTONS ROW-4
bclear = Button(f1_r4, text='C', font='lucida 34 bold', padx=21, pady=15, relief=RAISED)
bclear.pack(side=LEFT, padx=15, pady=10)
bclear.bind('<Button-1>', click)

bzero = Button(f1_r4, text='0', font='lucida 35 bold', padx=20, pady=15, relief=RAISED)
bzero.pack(side=LEFT, padx=15, pady=10)
bzero.bind('<Button-1>', click)

bdot = Button(f1_r4, text='.', font='lucida 35 bold', padx=25, pady=15, relief=RAISED)
bdot.pack(side=LEFT, padx=15, pady=10)
bdot.bind('<Button-1>', click)

b_div = Button(f1_r4, text='/', font='lucida 35 bold', padx=25, pady=15, relief=RAISED)
b_div.pack(side=LEFT, padx=15, pady=10)
b_div.bind('<Button-1>', click)

bequal = Button(f1_r4, text='=', font='lucida 35 bold', padx=27, pady=15, relief=RAISED)
bequal.pack(side=LEFT, padx=20, pady=10)
bequal.bind('<Button-1>', click)

f1_r4.pack()

root.mainloop()