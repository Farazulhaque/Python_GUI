# Python program to generate random password using Tkinter module
import random
from tkinter import *
from tkinter.ttk import *


# Data needed for generating password
def low():
    entry.delete(0, END)

    # Get the desired length of variable
    length = var1.get()

    easy = "abcdefghijklmnopqrstuvwxyz0123456789"
    medium = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    hard = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_!@#$%^&*()"
    password = ""

    # If strength selected is EASY
    if var.get() == 1:
        for i in range(0, length):
            password += random.choice(easy)
        return password

    # If strength selected is MEDIUM
    elif var.get() == 2:
        for i in range(0, length):
            password += random.choice(medium)
        return password

    # If strength selected is hARD
    elif var.get() == 3:
        for i in range(0, length):
            password += random.choice(hard)
        return password

    else:
        print("Please choose an option")


# Data needed for creation of password
def generate():
    password1 = low()
    entry.insert(10, password1)


# Function to copy password to clipboard
def copy():
    random_password = entry.get()
    root.clipboard_clear()
    root.clipboard_append(random_password)


# Main function
# Create GUI window
root = Tk()

# GUI window title
root.title("Randomized Password Generator")

# Create label and entry to show password generated
Random_password = Label(root, text="Password")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)

# Create label for password length
c_label = Label(root, text="Length")
c_label.grid(row=1)

# Button to copy password to clipboard
copy_button = Button(root, text="Copy", command=copy)
copy_button.grid(row=0, column=2)

# Button to generate password
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)

# Creating variable var for radio buttons
var = IntVar()
# Giving default strength to MEDIUM to radio button
var.set(2)
# Radio buttons to select strength of password
radio_low = Radiobutton(root, text="EASY", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky="E")
radio_middle = Radiobutton(root, text="MEDIUM", variable=var, value=2)
radio_middle.grid(row=1, column=3, sticky="E")
radio_strong = Radiobutton(root, text="HARD", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky="E")

# Creating variable var1 for passsword length
var1 = IntVar()
# Combo Box to select length of password
combo = Combobox(root, textvariable=var1)

combo['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                   18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, "How long?")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)

# Start the GUI
root.mainloop()
