from csv import writer
from tkinter import *

root = Tk()

# width x Height
root.geometry("300x300")
root.minsize(500, 350)
root.maxsize(500, 350)


def proceed():
    def calculate_si():
        p = int(principalvalue.get())
        r = float(ratevalue.get())/100
        t = int(timevalue.get())
        A = p * (1 + r*t)
        print(A)
        principal_amt = Label(root, text=f"Principal Amount {p}", fg="green", font=(
            "Times New Roman", 12, "bold")).grid(row=6, column=2, columnspan=3)
        interest_amt = Label(root, text=f"Interest Amount {A-p}", fg="green", font=(
            "Times New Roman", 12, "bold")).grid(row=7, column=2, columnspan=3)
        total_amt = Label(root, text=f"Total Amount {A+p}", fg="green", font=(
            "Times New Roman", 12, "bold")).grid(row=8, column=2, columnspan=3)

    def calculate_ci():
        p = int(principalvalue.get())
        r = float(ratevalue.get())/100
        t = int(timevalue.get())
        A = p * (1 + r)**(t)
        print(A)
        principal_amt = Label(root, text=f"Principal Amount {p}", fg="green", font=(
            "Times New Roman", 12, "bold")).grid(row=6, column=2, columnspan=3)
        interest_amt = Label(root, text=f"Interest Amount {A-p}", fg="green", font=(
            "Times New Roman", 12, "bold")).grid(row=7, column=2, columnspan=3)
        total_amt = Label(root, text=f"Total Amount {A+p}", fg="green", font=(
            "Times New Roman", 12, "bold")).grid(row=8, column=2, columnspan=3)

    if var.get() == "si":
        for widget in root.winfo_children():
            widget.destroy()

        Label(root, text="Simple Interest Calculator", font="comicsansms 20 bold",
              pady=15).grid(row=0, column=0, columnspan=5)

        # Text for our form
        principal = Label(root, text="Principal (P): Rs. ", padx=70, font=1)
        rate = Label(root, text="Rate (R) % ", font=1)
        time = Label(root, text="Time (in yrs)", font=1)

        # Pack text for our form
        principal.grid(row=1, column=2)
        rate.grid(row=2, column=2)
        time.grid(row=3, column=2)

        # Tkinter variable for storing variables
        principalvalue = StringVar()
        ratevalue = StringVar()
        timevalue = StringVar()

        # Entries for our form
        principalentry = Entry(root, textvariable=principalvalue, fg="#000154",
                               highlightthickness=1, relief="flat", font=10)
        rateentry = Entry(root, textvariable=ratevalue, fg="#000154",
                          highlightthickness=1, relief="flat", font=10)
        timeentry = Entry(root, textvariable=timevalue, fg="#000154",
                          highlightthickness=1, relief="flat", font=10)

        # Setting border of entry widget
        principalentry.config(highlightbackground="#a2a3a2",
                              highlightcolor="#314f29")
        rateentry.config(highlightbackground="#a2a3a2",
                         highlightcolor="#314f29")
        timeentry.config(highlightbackground="#a2a3a2",
                         highlightcolor="#314f29")

        # Packing the entries for our form
        principalentry.grid(row=1, column=3, pady="3")
        rateentry.grid(row=2, column=3, pady="3")
        timeentry.grid(row=3, column=3, pady="3")

        blankspace = Label(root, text="").grid(row=7, column=2)
        # button & packing it and assigning it a command
        Button(text="Calculate", command=calculate_ci, relief="ridge", cursor="hand2",
               font=("Comic Sans MS", "12")).grid(row=5, column=2, columnspan=2)

    else:
        for widget in root.winfo_children():
            widget.destroy()
        Label(root, text="Compound Interest Calculator", font="comicsansms 20 bold",
              pady=15).grid(row=0, column=0, columnspan=5)

        # Text for our form
        principal = Label(root, text="Principal (P): Rs. ", padx=70, font=1)
        rate = Label(root, text="Rate (R) % ", font=1)
        time = Label(root, text="Time (in yrs)", font=1)

        # Pack text for our form
        principal.grid(row=1, column=2)
        rate.grid(row=2, column=2)
        time.grid(row=3, column=2)

        # Tkinter variable for storing variables
        principalvalue = StringVar()
        ratevalue = StringVar()
        timevalue = StringVar()

        # Entries for our form
        principalentry = Entry(root, textvariable=principalvalue, fg="#000154",
                               highlightthickness=1, relief="flat", font=10)
        rateentry = Entry(root, textvariable=ratevalue, fg="#000154",
                          highlightthickness=1, relief="flat", font=10)
        timeentry = Entry(root, textvariable=timevalue, fg="#000154",
                          highlightthickness=1, relief="flat", font=10)

        # Setting border of entry widget
        principalentry.config(highlightbackground="#a2a3a2",
                              highlightcolor="#314f29")
        rateentry.config(highlightbackground="#a2a3a2",
                         highlightcolor="#314f29")
        timeentry.config(highlightbackground="#a2a3a2",
                         highlightcolor="#314f29")

        # Packing the entries for our form
        principalentry.grid(row=1, column=3, pady="3")
        rateentry.grid(row=2, column=3, pady="3")
        timeentry.grid(row=3, column=3, pady="3")

        blankspace = Label(root, text="").grid(row=7, column=2)
        # button & packing it and assigning it a command
        Button(text="Calculate", command=calculate_si, relief="ridge", cursor="hand2",
               font=("Comic Sans MS", "12")).grid(row=5, column=2, columnspan=2)


var = StringVar()
var.set("si")
Label(root, text="Select your choice:",
      font="lucida 19 bold", justify=LEFT, padx=14).grid(row=1, column=1, columnspan=2)
radio = Radiobutton(root, text="Simple Interest", padx=14,
                    variable=var, value="si").grid(row=2, column=1)
radio = Radiobutton(root, text="Compound Interest", padx=14,
                    variable=var, value="ci").grid(row=2, column=2)

Button(text="proceed", command=proceed).grid(row=3, column=2)


root.mainloop()
