from tkinter import *


def testing():
    mytext="Hello guys"
    txtbx.insert(0, mytext)



litha = Tk()
litha.title("Litha Kane")
litha.geometry('900x800')
litha.configure(background="#8fb278")
theLabel = Label(litha, text="Hello People!", relief="solid")
theLabel.pack()
txtbx = Entry(litha, width=40)
txtbx.pack()
mybutton1 = Button(litha, text="Submit", bg="pink", command=testing)
mybutton1.pack()
litha.mainloop()
