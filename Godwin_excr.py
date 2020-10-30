from tkinter import *
from tkinter import Tk

root = Tk()
root.geometry('400x400')
root.title('Calculator')
root.configure(background="#DF4A44")

fst_num = IntVar()
sec_num = IntVar()
third_num = IntVar()

L1 = Label(root, text="Enter first number:")
L2 = Label(root, text="Enter second number:")
L3 = Label(root, text='Answer = ')

txEntry1 = Entry(root, textvariable=fst_num)
txEntry2 = Entry(root, textvariable=sec_num)
txEntry3 = Entry(root, textvariable=third_num)

def add():
    txEntry1.insert(0,fst_num.get()+sec_num.get())
    
button1 = Button(root, text='Add', command=add)

def clear():
    txEntry1.delete(0, END)
    txEntry2.delete(0, END)
    txEntry3.delete(0, END)

button2 = Button(root, text='Clear', command=clear)

fst_num.pack()
sec_num.pack()
third_num.pack()

txEntry1.pack()
txEntry2.pack()
txEntry3.pack()

button1.pack()
button2.pack()



root.mainloop()
