import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()
root.title("SecureNotes")
root.configure(bg= "pale turquoise")
root.resizable(0,0)
root.geometry('500x400')

username = ''
password = ''

#Importing Images
load = Image.open("assets\input_bar.png")
load = load.resize((400, 19), Image.ANTIALIAS)
ib = ImageTk.PhotoImage(load)

load = Image.open("assets\lock.png")
load = load.resize((64, 64), Image.ANTIALIAS)
lock = ImageTk.PhotoImage(load)

#Placing Images + Text
inputbar = Label(image = ib, bg = "pale turquoise")
inputbar.place(x = 300, y = 200, anchor = 'center')

inputbar = Label(image = ib, bg = "pale turquoise")
inputbar.place(x = 300, y = 180, anchor = 'center')

logolock = Label(image = lock, bg = "pale turquoise")
logolock.place(x = 250, y = 130, anchor = 'center')

ul = Label(text = "Username:", bg = "pale turquoise", fg = "SteelBlue4")
ul.place(x = 50, y = 180, anchor = 'center')

ul = Label(text = "Password:", bg = "pale turquoise", fg = "SteelBlue4")
ul.place(x = 50, y = 200, anchor = 'center')

#Input Bar
message = StringVar()
mess = Entry(textvariable = username, width = 60, borderwidth=0)
mess.place(x= 300, y = 180, anchor = 'center')

message = StringVar()
mess = Entry(textvariable = password, width = 60, borderwidth=0)
mess.place(x= 300, y = 200, anchor = 'center')

#Checking Login Details


root.mainloop()