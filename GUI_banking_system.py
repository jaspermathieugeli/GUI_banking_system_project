from tkinter import *
import os
from PIL import Image, ImageTk

master = Tk()
master.title("Banking System")

def complete_creation():

    creation_name = name.get()
    creation_passcode = passcode.get()

    account_list = os.listdir()

    if creation_name == "" or creation_passcode == "":
        notify.config(fg="black", text="Please fill all fields")
        return
    notify.config(fg="black", text="Yes.")

    for check in account_list:
        if creation_name == check:
            notify.config(fg="black", text="Already exists.")
            return
        else:
            new = open(creation_name, "w")
            new.write(creation_name + "\n")
            new.write(creation_passcode + "\n")

def create():

    global name
    global passcode
    global notify

    name = StringVar()
    passcode = StringVar()
    
    creation_screen = Toplevel(master)
    creation_screen.title("Create")

    Label(creation_screen, text="Name", font=("Calibri", 10)).grid(row=1, sticky=W)
    Label(creation_screen, text="Passcode", font=("Calibri", 10)).grid(row=2, sticky=W)

    notify = Label(creation_screen, font=("Calibri", 10))
    notify.grid(row=4, sticky=W)

    Entry(creation_screen, textvariable=name).grid(row=1, column=1)
    Entry(creation_screen, textvariable=passcode, show="*").grid(row=2, column=1)

    Button(creation_screen, text="Create", command=complete_creation, font=("Calibri", 10)).grid(row=3, sticky=N, pady=10)

def log_in():

    log_in_name = StringVar()
    log_in_passcode = StringVar()

    log_in_screen = Toplevel(master)
    log_in_screen.title("Log In")

    Label(log_in_screen, text="Name", font=("Calibri", 10)).grid(row=1, sticky=W)
    Label(log_in_screen, text="Passcode", font=("Calibri", 10)).grid(row=2, sticky=W)

    Entry(log_in_screen, textvariable=log_in_name).grid(row=1, column=1)
    Entry(log_in_screen, textvariable=log_in_passcode, show="*").grid(row=2, column=1)

    Button(log_in_screen, text="Log In", font=("Calibri", 10)).grid(row=3, sticky=N, pady=10)

image = Image.open("Images/bank.png")
image = image.resize((200, 200))
image = ImageTk.PhotoImage(image)

Label(master, text = "Banking System", font=("Calibri", 10)).grid(row=0, sticky=N, pady=10)
Label(master, image=image).grid(row=2, sticky=N, pady=20)

Button(master, text="Create", font=("Calibri", 10), width=20, command=create).grid(row=3, sticky=N, pady=5)
Button(master, text="Log In", font=("Calibri", 10), width=20, command=log_in).grid(row=4, sticky=N, pady=5)

master.mainloop()