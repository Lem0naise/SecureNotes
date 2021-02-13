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
frame = Frame(root)
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

#reads logins from text file in assets
logins = {}
with open("assets/logins.txt") as dicti:
    for line in dicti:
        (key, val) = line.split()
        logins[key] = val

#Checking Login Details
def login(user, passwor):
    try:
        #checks if the username equals that user's password
        if logins[user] == passwor:
            global logged_user 
            logged_user = logins[user]
            global congrats
            congrats = Label(text="Congratulations, you have successfully logged in!", bg = "pale turquoise")
            congrats.place(x=250, y=290, anchor= "center")
        else:
            global sorry
            sorry = Label(text="Sorry, that login and password are not recognized. ", bg = "pale turquoise")
            sorry.place(x=250, y=290, anchor= "center")


    except:
            sorry = Label(text="Sorry, that login and password are not recognized. ", bg = "pale turquoise")
            sorry.place(x=250, y=290, anchor= "center")
            
#you need to keep the test here, it doesn't work without it but i don't know why
def startlogin(test):
    #destroys the old "logged in" messages if they are there
    try:
        congrats.destroy()
        sorry.destroy()
    except:
        pass
    login(username.get(), password.get())

def startlogin2():
    startlogin(2)
#signup function
def sign_up():
    print("signing up")

#binding the enter key to the enter button 
root.bind('<Return>', startlogin)

#Input Bar
username = StringVar()
mess = Entry(textvariable = username, width = 60, borderwidth=0)
mess.place(x= 300, y = 180, anchor = 'center')

password = StringVar()
mess2 = Entry(textvariable = password, width = 60, borderwidth=0)
mess2.place(x= 300, y = 200, anchor = 'center')

#signin / signup buttons
signin = Button(text = "Sign In", command = startlogin2, anchor='center')
signin.place(x= 250, y = 230, anchor = 'center')

signup = Button(text = "Sign Up", command = sign_up, anchor='center')
signup.place(x= 250, y = 260, anchor = 'center')




root.mainloop()