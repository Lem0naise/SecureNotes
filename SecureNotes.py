from os import unlink
import tkinter as tk
from tkinter import *
from typing import get_type_hints
from PIL import Image, ImageTk
import traceback
import tkinter.font as font

root = tk.Tk()
root.title("SecureNotes Login ")
root.configure(bg= "gray10")
root.resizable(0,0)
root.geometry('500x400')
global isempty
isempty = False
password = StringVar()
username = StringVar()
logins = {}

#creating font
deffont = font.Font(family = "arial", size="1")


#Importing Images
load = Image.open("assets\input_bar.png")
load = load.resize((400, 19), Image.ANTIALIAS)
ib = ImageTk.PhotoImage(load)

load = Image.open("assets\lock.png")
load = load.resize((64, 64), Image.ANTIALIAS)
lock = ImageTk.PhotoImage(load)

signinbutton = Image.open("assets\sign_in.png")
signinbutton = signinbutton.resize((131, 25), Image.ANTIALIAS)
sibutton = ImageTk.PhotoImage(signinbutton)

signupbutton = Image.open("assets\sign_up.png")
signupbutton = signupbutton.resize((131, 25), Image.ANTIALIAS)
subutton = ImageTk.PhotoImage(signupbutton)

#password decryption table
decrypted = b"abcdefghijklmnop!qrstuvwxyz1234567_890ABCDEFGHIJKLMNOPQRSTUVWXYZ "
encrypted = b"zcxBVMNlkjhgFASDqEwT+RUyoIPZCXbvmnLKJHGfas!dQ_WtruYOip0793682541e"
encrypt_table = bytes.maketrans(decrypted, encrypted)
decrypt_table = bytes.maketrans(encrypted, decrypted)




#reading notes
def noteprocess():
    with open("assets/Logged_User.scn") as logg:
        global loggeduser
        loggs = logg.read()
        loggeduser = loggs.strip()
        global loggeduserpath
        loggeduserpath = ("assets/" + loggeduser + ".scn")

    def startnotes():
        global root
        try:
            with open(loggeduserpath) as notesfile:
                print(loggeduserpath)
                global note
                notes = (notesfile.readlines())
                for i in range(0, len(notes)-1):
                    #decrypts notes (all danil no credit to me :))
                    notes[i] = notes[i].translate(decrypt_table)

            root.destroy()    
            print("destroying old window works")   
            root = tk.Tk()
            root.title(loggeduser.translate(decrypt_table) + "'s notes")
            print("title works")
            root.configure(bg= "gray10")
            root.geometry('600x450')
            root.geometry()
            print("new root works")
            noteframe = Frame(root, bg = "gray10")
            noteframe.pack()

            #saving and exiting
            def gettext():
                noteinputvar = noteinput.get("1.0", END)
                with open(loggeduserpath, "w") as txtfile:
                    txtfile.write(noteinputvar.translate(encrypt_table))
            savebutton = Button(text="Save", bg = "gray10", command = gettext, fg = "snow", activebackground = "gray10", borderwidth = 0)
            savebutton.pack()
            #prints all notes (all danil's work)
            for each_note in notes:

                noteinput = Text(noteframe, bg = "gray10", font = ("arial", 10), borderwidth=0, fg = "snow", insertbackground = "snow")
                noteinput.grid(row=0, column=0, padx=10, pady=2)
                with open(loggeduserpath) as txtfile:
                     txtimported = (txtfile.read()).translate(decrypt_table)
                if txtimported == " ":
                    pass
                else:    
                    noteinput.insert(INSERT, txtimported)
                global signup
                
                
                #saving text (updating text box) every 0.5 seconds
                #encrypting to text file
                #future (seperate indiidual notes by special character)
                

            print("notes works")



            

        except: 
            traceback.print_exc() 
            open(loggeduserpath, "x")

            #Writes a space to the text file
            with open(loggeduserpath, "w") as txtfile:
                    txtfile.write(" ")

            print("create")
            startnotes()
            print("creating new text file works")
            startnotes()
    startnotes()


#Checking Login Details
def login(user, passwor):
    global sorry
    try:
        #checks if the username equals that user's password
        if logins[user] == passwor:
            global logged_user 
            logged_user = user
            with open("assets/Logged_user.scn", "w") as file:
                file.write(logged_user.translate(encrypt_table)) 
            global congrats
            congrats = Label(text="Welcome Back!", bg = "gray10", fg = "dodger blue")
            congrats.place(x=250, y=290, anchor= "center")
            noteprocess()


        else:
            
            try:
                errorr.destroy()
            except:
                pass
            try:
                sorry.destroy()
            except:
                pass

            sorry = Label(text="Incorrect username or password.", bg = "gray10", fg = "red")
            sorry.place(x=250, y=290, anchor= "center")


    except:
            try:
                errorr.destroy()
            except:
                pass
            sorry = Label(text="Incorrect username or password.", bg = "gray10", fg = "red")
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
        errorr = Label(text = "Username not available. ", anchor='center', bg = "gray10", fg = "red")
        errorr.place(x= 250, y = 290, anchor = 'center')
    else:
        global mess
        global mess2
        root.bind('<Return>', sign_up2)
        try:
            sorry.destroy()
        except:
            pass    
        #here put the textvariables into the login file
        with open("assets/logins.scn", "a") as dicti:
            if isempty == False:
                dicti.write("\n")
            dicti.write(username.get().translate(encrypt_table))
            dicti.write(" ")
            dicti.write(password.get().translate(encrypt_table))
            dicti.write("\n")
        errorr = Label(text = "Account created. ", anchor='center', bg = "gray10", fg = "dodger blue")
        errorr.place(x= 250, y = 290, anchor = 'center')

def opensettings():

    inputbar.destroy()
    inputbar2.destroy()
    logolock.destroy()
    ul.destroy()
    ul2.destroy()
    mess.destroy()
    mess2.destroy()
    signin.destroy()
    signup.destroy()
    settingsbutton.destroy()

    global backbutton
    backbutton = Button(text = "Back", command = mainmenu, anchor='center', bg = "gray10", activebackground= "gray10", borderwidth=0, fg = "snow")
    backbutton.place(x= 20, y = 10, anchor = 'center')


def mainmenu():
    #reads logins from text file in assets
    global logins
    
    with open("assets/logins.scn") as dicti:
        for line in dicti:
            try:
                (key, val) = line.split()
                key, val = key.translate(decrypt_table), val.translate(decrypt_table)
                logins[key] = val
            except:
                isempty = True
            
            
    global inputbar
    global inputbar2
    global logolock
    global ul
    global ul2
    #binding the enter key to the enter button 
    root.bind('<Return>', startlogin)



    #Placing Images + Text
    inputbar = Label(image = ib, bg = "gray10")
    inputbar.place(x = 290, y = 200, anchor = 'center')

    inputbar2 = Label(image = ib, bg = "gray10")
    inputbar2.place(x = 290, y = 180, anchor = 'center')

    logolock = Label(image = lock, bg = "gray10")
    logolock.place(x = 250, y = 130, anchor = 'center')

    ul = Label(text = "Username:", bg = "gray10", fg = "snow")
    ul.place(x = 40, y = 180, anchor = 'center')

    ul2 = Label(text = "Password:", bg = "gray10", fg = "snow")
    ul2.place(x = 40, y = 200, anchor = 'center')


    #Input Bar

    global mess
    mess = Entry(textvariable = username, width = 60, borderwidth=0)
    mess.place(x= 300, y = 180, anchor = 'center')


    global mess2
    mess2 = Entry(textvariable = password, width = 60, borderwidth=0, show = "●")
    mess2.place(x= 300, y = 200, anchor = 'center')

    #signin / signup buttons
    global signin
    signin = Button(image = sibutton, command = startlogin2, anchor='center', bg = "gray10", activebackground= "gray10", borderwidth=0, fg = "snow")
    signin.place(x= 250, y = 230, anchor = 'center')

    global signup
    signup = Button(image = subutton, command = sign_up_first, anchor='center', bg = "gray10", activebackground= "gray10", borderwidth=0, fg = "snow")
    signup.place(x= 250, y = 258, anchor = 'center')

    #settings button
    global settingsbutton
    settingsbutton = Button(text = "Settings", command = opensettings, anchor='center', bg = "gray10", activebackground= "gray10", borderwidth=0, fg = "snow")
    settingsbutton.place(x= 475, y = 385, anchor = 'center')

mainmenu()

root.mainloop()
