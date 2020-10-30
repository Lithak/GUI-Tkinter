import tkinter as tk

# Declare global variables
temp_c = None
temp_f = None

# This function is called whenever the button is pressed
def convert():

    global temp_c
    global temp_f

    # Convert Celsius to Fahrenheit and update label (through textvariable)
    try:
        val = temp_c.get()
        temp_f.set((val * 9.0 / 5) + 32)
    except:
        pass

root = tk.Tk()
root.title("Temperature Converter")
root.geometry('500x500')
root.configure(background="yellow")

# Variables for holding temperature data
temp_c = tk.DoubleVar()
temp_f = tk.DoubleVar()

entry_celsius = tk.Entry(root, width=7, textvariable=temp_c)
label_unitc = tk.Label(root, text="°C")
label_equal = tk.Label(root, text="is equal to")
label_fahrenheit = tk.Label(root, textvariable=temp_f)
label_unitf = tk.Label(root, text="°F")
button_convert = tk.Button(root, text="Convert", command=convert)

# Lay out widgets
entry_celsius.grid(row=0, column=1)
label_unitc.grid(row=0, column=2)
label_equal.grid(row=1, column=0)
label_fahrenheit.grid(row=1, column=1)
label_unitf.grid(row=1, column=2)
button_convert.grid(row=2, column=1)

# Place cursor in entry box by default
entry_celsius.focus()

root.mainloop()
