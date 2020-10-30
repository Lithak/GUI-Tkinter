from tkinter import *
from tkinter import Tk
from tkinter.font import Font

root = Tk()
root.geometry('600x600')
root.title('Calculator')


lb1 = Label(root, text="First number:", background="#DF4A44", font="Bold")
lb1.grid(row=1, column=0)
lb1 = Entry(root)
lb1.grid(row=1, column=1)

lb2 = Label(root, text="Second number:", background="#DF4A44", font="Bold")
lb2.grid(row=2, column=0)
lb2 = Entry(root)
lb2.grid(row=2, column=1)

lb3 = Label(root, text="Answer:", background="#DF4A44", font="Bold")
lb3.grid(row=3, column=0)
lb3_result = Label(root)
lb3_result.grid(row=3, column=1)


def Add():
    a = int(lb1.get())
    b = int(lb2.get())
    result = a + b
    lb3_result.configure(text=result)


button1 = Button(text='Add', background="#B0201B", command=Add)
button1.grid(row=4, column=0)


def clear():
    lb1.delete(0, END)
    lb2.delete(0, END)
    lb3_result.configure(text="")


button2 = Button(text="Clear", background="#B0201B",command=clear)
button2.grid(row=4, column=1)

root.mainloop()
