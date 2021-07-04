from tkinter import *
from random import randint


root = Tk()

# width x Height
root.geometry("300x300")
root.minsize(400, 220)
root.maxsize(400, 220)
root.title("Guess Number Game")

secret_num = randint(1, 100)
num_guesses = 0


def check():
    global num_guesses

    # To erase the previous output
    output = Label(root, text="                                           ", fg="red", font=(
        "Times New Roman", 12, "bold")).grid(row=4, column=2, columnspan=3)
    guess = int(userGuessvalue.get())
    num_guesses += 1
    if 5 - num_guesses == 1:
        x = "guess"
    else:
        x = "guesses"
    if num_guesses <= 4:
        if guess < secret_num:
            output = Label(root, text=f"HIGHER {5-num_guesses} {x} left", fg="red", font=(
                "Times New Roman", 12, "bold")).grid(row=4, column=2, columnspan=3)
        elif guess > secret_num:
            output = Label(root, text=f"LOWER {5-num_guesses} {x} left", fg="red", font=(
                "Times New Roman", 12, "bold")).grid(row=4, column=2, columnspan=3)
        else:
            output = Label(root, text="You got it!!", fg="green", font=(
                "Times New Roman", 12, "bold")).grid(row=4, column=2, columnspan=3)
    else:
        output = Label(root, text=f"You lose. The correct number is {secret_num}.", fg="red", font=(
            "Times New Roman", 12, "bold")).grid(row=4, column=2, columnspan=3)


# For heading
Label(root, text="Guess Number Game", font="comicsansms 20 bold",
      pady=15).grid(row=0, column=2, columnspan=2)

# Text for userGuess
userGuess = Label(root, text="Enter your Guess", padx=20, font=1)

# Pack text for userGuess
userGuess.grid(row=1, column=2)

# Tkinter variable for storing variables
userGuessvalue = StringVar()

# Entries for our userGuess
userGuessentry = Entry(root, textvariable=userGuessvalue, fg="#000154",
                       highlightthickness=1, relief="flat", font=10)

# Setting border of entry widget
userGuessentry.config(highlightbackground="#a2a3a2", highlightcolor="#314f29")

# Packing the entries for our userGuess
userGuessentry.grid(row=1, column=3, pady="3")

# For spacing between user input and check button
blankspace = Label(root, text="").grid(row=2, column=2)

# button & packing it and assigning it a command
Button(text="Check", command=check, relief="ridge", cursor="hand2",
       font=("Comic Sans MS", "12")).grid(row=3, column=2, columnspan=2)


root.mainloop()
