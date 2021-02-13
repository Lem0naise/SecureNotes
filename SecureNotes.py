import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


root = tk.Tk()
root.title("SecureNotes")
root.configure(bg= "pale turquoise")
root.resizable(0,0)
root.geometry('500x400')
global isempty
isempty = False
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

#password decryption table
decrypted = b"abcdefghijklmnop!qrstuvwxyz1234567_890ABCDEFGHIJKLMNOPQRSTUVWXYZ "
encrypted = b"zcxBVMNlkjhgFASDqewT RUyoIPZCXbvmnLKJHGfas!dQEWtruYOip0793682541_"
encrypt_table = bytes.maketrans(decrypted, encrypted)
decrypt_table = bytes.maketrans(encrypted, decrypted)

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



#Checking Login Details
def login(user, passwor):
    try:
        #checks if the username equals that user's password
        if logins[user] == passwor:
            global logged_user 
            logged_user = user
            with open("assets/Logged_user.scn", "w") as file:
                file.write(logged_user.translate(encrypt_table)) 
            global congrats
            congrats = Label(text="Congratulations, you have successfully logged in!", bg = "pale turquoise")
            congrats.place(x=250, y=290, anchor= "center")
            exec(open("assets/scnotelauncher.py").read())
            root.destroy()
        else:
            global sorry
            try:
                errorr.destroy()
            except:
                pass
            sorry = Label(text="Sorry, that login and password are not recognized. ", bg = "pale turquoise")
            sorry.place(x=250, y=290, anchor= "center")


    except:
            try:
                errorr.destroy()
            except:
                pass
            sorry = Label(text="Sorry, that login and password are not recognized. ", bg = "pale turquoise")
            sorry.place(x=250, y=290, anchor= "center")
            
#you need to keep the test here, it doesn't work without it but i don't know why
def startlogin(test):
    #reads logins from text file in assets
    global logins
    logins = {}
    with open("assets/logins.scn") as dicti:
        for line in dicti:
            try:
                (key, val) = line.split()
                key, val = key.translate(decrypt_table), val.translate(decrypt_table)
                logins[key] = val
            except:
                isempty = True
            
    #destroys the old "logged in" messages if they are there
    try:
        congrats.destroy()
        sorry.destroy()
    except:
        pass
    login(username.get(), password.get())

def startlogin2():
    startlogin(2)


def sign_up_first():
    sign_up()
#signup function

def sign_up2(test):
    sign_up()

def sign_up3():
    sign_up2(2)

def sign_up():
    if username.get() in logins:
        try:
            sorry.destroy()
            congrats.destroy()
        except:
            pass
        global errorr
        errorr = Label(text = "You already have an account, but your password does not match. ", anchor='center', bg = "pale turquoise")
        errorr.place(x= 250, y = 290, anchor = 'center')
    else:

        global mess
        global mess2
        root.bind('<Return>', sign_up2)

        signin.destroy()
        signup.destroy()
        global entersignup
        entersignup = Button(text = "Sign Up", command = sign_up3, anchor='center')
        entersignup.place(x= 250, y = 260, anchor = 'center')
        

        #here put the textvariables into the login file
        with open("assets/logins.scn", "a") as dicti:
            if isempty == False:
                dicti.write("\n")
            dicti.write(username.get().translate(encrypt_table))
            dicti.write(" ")
            dicti.write(password.get().translate(encrypt_table))
            dicti.write("\n")

        root.destroy()




#binding the enter key to the enter button 
root.bind('<Return>', startlogin)

#Input Bar
username = StringVar()
global mess
mess = Entry(textvariable = username, width = 60, borderwidth=0)
mess.place(x= 300, y = 180, anchor = 'center')

password = StringVar()
global mess2
mess2 = Entry(textvariable = password, width = 60, borderwidth=0, show = "○")
mess2.place(x= 300, y = 200, anchor = 'center')

#signin / signup buttons
global signin
signin = Button(text = "Sign In", command = startlogin2, anchor='center')
signin.place(x= 250, y = 230, anchor = 'center')

global signup
signup = Button(text = "Sign Up (Restart) ", command = sign_up_first, anchor='center')
signup.place(x= 250, y = 260, anchor = 'center')




root.mainloop()