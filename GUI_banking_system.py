from tkinter import *
import os
from PIL import Image, ImageTk

master = Tk()
master.title("Banking System")

def create():
    pass
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