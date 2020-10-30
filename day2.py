# import tkinter
from tkinter import *

# to initialise tkinter we have to create a Tk root widget
# this is basically an ordinary window, with a title bar and other decoration as necessary
# the root widget (only one can be created for each program) must be created before any other widgets
root = Tk()

# creating and packing a Label which says "Login Screen"
w = Label(root, text="Login Screen")
w.pack()
# creating and packing a Label which is the Site/App!
e1 = Label(root, text="Whatsapp")
e1.pack()
# creating and packing a Label which says "Username"
w1 = Label(root, text="Username")
w1.pack()

# creating and packing a text entry input box (this will come under Username)
e = Entry(root)
e.pack()

# creating and packing a Label which says "Password"
w2 = Label(root, text="Password")
w2.pack()

# creating and packing a second text entry input box (this will come under Password)
e1 = Entry(root)
e1.pack()

# This is another interesting layout feature - it creates a tool bar
toolbar = Frame(root)

# creates a button (variable b) called 'Enter'
b = Button(toolbar, text="Enter", width=9)
b.pack(side=LEFT, padx=2, pady=2)

# creates a button called 'Cancel'
b = Button(toolbar, text="Cancel", width=9)
b.pack(side=LEFT, padx=2, pady=2)


# This is the interesting bit - it's a function called 'callback
# it has an IF function that asks for two specific text inputs for username and password
# it displays a label message depending on whether the input was valid
def callback():
    if e.get() == "Hello" and e1.get() == "God":
        welcome = Label(root, text="Welcome - Access Granted")
        welcome.pack()
    else:
        denied = Label(root, text="Sorry, Access Denied")
        denied.pack()


# This produces a final 'Sign up' button -it's in order, so goes after the 'Cancel' Button
# Notice it is this button that contains a CALL to the callback function above.
b = Button(toolbar, text="Sign-Up", command=callback, width=9)
b.pack(side=LEFT, padx=2, pady=2)
# this defines the position and layout of the toolbar.
toolbar.pack(side=TOP, fill=X)

root.mainloop()
