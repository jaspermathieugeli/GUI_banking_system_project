from tkinter import *
import os
from PIL import Image, ImageTk

master = Tk()
master.title("Banking System")

image = Image.open("Images/bank.png")
image = image.resize((200, 200))
image = ImageTk.PhotoImage(image)

Label(master, text = "Banking System", font=("Calibri", 10)).grid(row=0, sticky=N, pady=10)
Label(master, image=image).grid(row=2, sticky=N, pady=20)