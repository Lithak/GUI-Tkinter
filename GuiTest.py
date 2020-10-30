from tkinter import *
from tkinter import Tk

root = Tk()
root.geometry('600x600')
root.title('Tempreture')
root.configure(background="#DF4A44")

lb1 = Label(root, text="Convert celsius", background="#DF4A44", font="Bold")
lb1.grid(row=4, column=0)
lb1 = Entry(root)
lb1.grid(row=4, column=1)

lb2 = Label(root, text="Convert fahrenheit", background="#DF4A44", font="Bold")
lb2.grid(row=8, column=0)
lb2 = Entry(root)
lb2.grid(row=8, column=1)

lb3 = Label(root, text="Answer:", background="#DF4A44", font="Bold")
lb3.grid(row=12, column=0)
lb3_result = Label(root)
lb3_result.grid(row=12, column=1)


def celsius(args):
    pass
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print('%.2f Celsius is: %0.2f Fahrenheit' % (celsius, fahrenheit))
    lb3_result.configure(text=print)


btn1 = Button(root, text="Calculate Celcius", command=celsius)
btn1.grid(row=16, column=0)


def fahrenheit():
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print('%.2f Fahrenheit is: %0.2f Celsius' % (fahrenheit, celsius))
    lb3_result.configure(text="")


btn2 = Button(root, text="Calculate fahrenheit", command=fahrenheit)
btn2.grid(row=16, column=1)

def clear():
    lb1.delete(0, END)
    lb2.delete(0, END)
    lb3_result.configure(text="")


btn2 = Button(text="Clear", background="#B0201B",command=clear)
btn2.grid(row=4, column=3)

lb3.focus()

root.mainloop()
