from tkinter import *

import tkinter

from tkinter import messagebox
from tkinter import Canvas

top = tkinter.Tk()

top.geometry("800x500")
def hello():
   messagebox.showinfo("Select", "Selected optionprinceNico"
                                 "")
    #print("This is the button it was clicked")
B1 = tkinter.Button(top, text="Select", command = hello)
B1.place(x = 50,y = 100)

CheckVar1 = IntVar()

C1 = Checkbutton(top, text = "Litha", variable = CheckVar1, \
     onvalue = True, offvalue = False, height=5, width = 20)
C2 = Checkbutton(top, text = "Braen", variable = CheckVar2, \
     onvalue = True, offvalue = False, height=5, width = 20)

C1.pack()

top.mainloop()