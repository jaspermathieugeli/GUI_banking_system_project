from tkinter import *
import os
from PIL import Image, ImageTk

master = Tk()
master.title("Banking System")

image = Image.open("Images/bank.png")
image = image.resize((200, 200))
image = ImageTk.PhotoImage(image)