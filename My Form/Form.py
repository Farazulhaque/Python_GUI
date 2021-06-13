from csv import writer
from tkinter import *

root = Tk()

# width x Height
root.geometry("300x300")
root.minsize(450, 350)
root.maxsize(450, 350)

# # Add image file
# bg = PhotoImage(file = "bg.png")

# # Show image using label
# label1 = Label( root, image = bg)
# label1.place(x = 0, y = 0)

# ========================================================
# Form
# Heading of CSV file
# This is only for the first time
heading = ["Name", "Phone No", "Gender",
           "Emergency Contact No", "Payment Mode", "Food Service"]

# Add Heading to CSV file
with open("records.csv", 'a') as h:
    csv = writer(h)
    csv.writerow(heading)
    h.close()


# Add data to CSV file
def addData():
    blankspace = Label(root, text="0", fg="green", font=(
        "Times New Roman", 12, "bold")).grid(row=9, column=2, columnspan=3)
    data = [namevalue.get(), phonevalue.get(), gendervalue.get(
    ), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()]
    # print("Submitting Form")
    if (namevalue.get() != "" and phonevalue.get() != "" and gendervalue.get != "" and emergencyvalue.get() != "" and paymentmodevalue.get() != ""):
        with open("records.csv", 'a') as f:
            csv = writer(f)
            csv.writerow(data)
            f.close()
        blankspace = Label(root, text="Data Added Successfully", fg="green", font=(
            "Times New Roman", 12, "bold")).grid(row=9, column=2, columnspan=3)
    else:
        blankspace = Label(root, text=" Please fill all the fields ", fg="red", font=(
            "Times New Roman", 12, "bold")).grid(row=9, column=2, columnspan=3)


Label(root, text="My Form", font="comicsansms 20 bold",
      pady=15).grid(row=0, column=0, columnspan=5)

# Text for our form
name = Label(root, text="Name", padx=70, font=1)
phone = Label(root, text="Phone", font=1)
gender = Label(root, text="Gender", font=1)
emergency = Label(root, text="Emergency Contact", font=1, padx=0)
paymentmode = Label(root, text="Payment Mode", font=1, padx=0)

# Pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# Tkinter variable for storing variables
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

# Entries for our form
nameentry = Entry(root, textvariable=namevalue, fg="#000154",
                  highlightthickness=1, relief="flat", font=10)
phoneentry = Entry(root, textvariable=phonevalue, fg="#000154",
                   highlightthickness=1, relief="flat", font=10)
genderentry = Entry(root, textvariable=gendervalue, fg="#000154",
                    highlightthickness=1, relief="flat", font=10)
emergencyentry = Entry(root, textvariable=emergencyvalue, fg="#000154",
                       highlightthickness=1, relief="flat", font=10)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue, fg="#000154",
                         highlightthickness=1, relief="flat", font=10)

# Setting border of entry widget
nameentry.config(highlightbackground="#a2a3a2", highlightcolor="#314f29")
phoneentry.config(highlightbackground="#a2a3a2", highlightcolor="#314f29")
genderentry.config(highlightbackground="#a2a3a2", highlightcolor="#314f29")
emergencyentry.config(highlightbackground="#a2a3a2", highlightcolor="#314f29")
paymentmodeentry.config(highlightbackground="#a2a3a2",
                        highlightcolor="#314f29")

# Packing the entries for our form
nameentry.grid(row=1, column=3, pady="3")
phoneentry.grid(row=2, column=3, pady="3")
genderentry.grid(row=3, column=3, pady="3")
emergencyentry.grid(row=4, column=3, pady="3")
paymentmodeentry.grid(row=5, column=3, pady="3")

# Checkbox and packing
foodservice = Checkbutton(
    text="Want to precheck your meals", variable=foodservicevalue, font=1)
foodservice.grid(row=6, column=3)

blankspace = Label(root, text="").grid(row=7, column=2)
# button & packing it and assigning it a command
Button(text="Submit", command=addData, relief="ridge", cursor="hand2",
       font=("Comic Sans MS", "12")).grid(row=8, column=2, columnspan=2)


root.mainloop()
