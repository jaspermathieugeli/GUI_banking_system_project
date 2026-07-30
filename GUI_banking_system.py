from tkinter import *
import os
from PIL import Image, ImageTk

master = Tk()
master.title("Banking System")

def create():

    name = StringVar()
    passcode = StringVar()
    
    creation_screen = Toplevel(master)
    creation_screen.title("Create")

    Label(creation_screen, text="Name", font=("Calibri", 10)).grid(row=1, sticky=W)
    Label(creation_screen, text="Passcode", font=("Calibri", 10)).grid(row=2, sticky=W)

    Entry(creation_screen, textvariable=name).grid(row=1, column=1)
    Entry(creation_screen, textvariable=passcode, show="*").grid(row=2, column=1)

def log_in():
    pass

image = Image.open("Images/bank.png")
image = image.resize((200, 200))
image = ImageTk.PhotoImage(image)

Label(master, text = "Banking System", font=("Calibri", 10)).grid(row=0, sticky=N, pady=10)
Label(master, image=image).grid(row=2, sticky=N, pady=20)

Button(master, text="Create", font=("Calibri", 10), width=20, command=create).grid(row=3, sticky=N, pady=5)
Button(master, text="Log In", font=("Calibri", 10), width=20, command=log_in).grid(row=4, sticky=N, pady=5)

master.mainloop()