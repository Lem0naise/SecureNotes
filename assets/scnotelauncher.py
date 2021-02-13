import tkinter as tk
from tkinter import *
from typing import Counter
from PIL import Image, ImageTk
import time

#note encryption / decryption table
decrypted = b"abcdefghijklmnop!qrstuvwxyz1234567_890ABCDEFGHIJKLMNOPQRSTUVWXYZ "
encrypted = b"zcxBVMNlkjhgFASDqewT RUyoIPZCXbvmnLKJHGfas!dQEWtruYOip0793682541_"
encrypt_table = bytes.maketrans(decrypted, encrypted)
decrypt_table = bytes.maketrans(encrypted, decrypted)


root = tk.Tk()
root.title("SecureNotes")
root.configure(bg= "pale turquoise")

frame = Frame(root)

with open("Logged_User.scn") as logg:
    global loggeduser
    loggs = logg.read()
    loggeduser = loggs.strip()
    global loggeduserpath
    loggeduserpath = (loggeduser + ".scn")

def startnotes():
    try:
        with open(loggeduserpath) as notes:
            global note
            note = (notes.read().translate(decrypt_table))
        first_note = Label(frame, text=note)
        first_note.pack()
        print(note)
        

    except:    
        open(loggeduserpath, "x")
        print("create")
        startnotes()

startnotes()