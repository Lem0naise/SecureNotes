from os import unlink
import tkinter as tk
from tkinter import *
from typing import get_type_hints
from PIL import Image, ImageTk
import traceback
import tkinter.font as font

#reading settings files before start (to apply darkmode)
try:
	with open("assets/settings.scn") as settingsfile:
		notes = (settingsfile.readlines())
		autosavetemp = str(notes[0])
		darkmodetemp = str(notes[1])

	#setting dark mode colour
	if darkmodetemp.strip().lower() == "true":
		darkmodecolour = "gray10"
		lightmodecolour = "snow"
	else:
		darkmodecolour = "snow"
		lightmodecolour = "gray10"

except:
	traceback.print_exc()
	with open("assets/settings.scn", "x") as temp:
		pass
	with open("assets/settings.scn", "w") as idekanymore:
		idekanymore.write("False")
		idekanymore.write("\n")
		idekanymore.write("True")
		
	with open("assets/settings.scn") as settingsfile:
		notes = (settingsfile.readlines())
		autosavetemp = str(notes[0])
		darkmodetemp = str(notes[1])

	#setting dark mode colour
	if darkmodetemp.strip().lower() == "true":
		darkmodecolour = "gray10"
		lightmodecolour = "snow"
	else:
		darkmodecolour = "snow"
		lightmodecolour = "gray10"

root = tk.Tk()
root.title("SecureNotes Login ")
try:
	root.configure(bg= darkmodecolour)
except:
	root.configure(bg = "gray10")
root.resizable(0,0)
root.geometry('500x400')
global isempty
isempty = False
password = StringVar()
username = StringVar()
logins = {}
global autosave
global darkmode
darkmode = "True"
global PaschaHuevo
PaschaHuevo = ''

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

backimage = Image.open("assets\\settings_icon.png")
backimage = backimage.resize((25,25), Image.ANTIALIAS)
settings_icon = ImageTk.PhotoImage(backimage)

backimage = Image.open("assets\\box_checked.png")
backimage = backimage.resize((36,33), Image.ANTIALIAS)
boxchecked = ImageTk.PhotoImage(backimage)

backimage = Image.open("assets\\box_unchecked.png")
backimage = backimage.resize((36,33), Image.ANTIALIAS)
boxunchecked = ImageTk.PhotoImage(backimage)

#password decryption table
decrypted = b"abcdefghijklmnop!qrstuvwxyz1234567_890ABCDEFGHIJKLMNOPQRSTUVWXYZ "
encrypted = b"zcxBVMNlkjhgFASDqEwT+RUyoIPZCXbvmnLKJHGfas!dQ_WtruYOip0793682541e"
encrypt_table = bytes.maketrans(decrypted, encrypted)
decrypt_table = bytes.maketrans(encrypted, decrypted)


#Creating Settings File

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
			root.configure(bg= darkmodecolour)
			root.geometry('600x450')
			root.geometry()
			print("new root works")
			noteframe = Frame(root, bg = darkmodecolour)
			noteframe.pack()

			#saving and exiting
			def gettext():
				noteinputvar = noteinput.get("1.0", END)
				with open(loggeduserpath, "w") as txtfile:
					txtfile.write(noteinputvar.translate(encrypt_table))
			savebutton = Button(text="Save", bg = darkmodecolour, command = gettext, fg = lightmodecolour, activebackground = darkmodecolour, borderwidth = 0)
			savebutton.pack()
			#prints all notes (all danil's work)
			for each_note in notes:

				noteinput = Text(noteframe, bg = darkmodecolour, font = ("arial", 10), borderwidth=0, fg = lightmodecolour, insertbackground = lightmodecolour)
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
			congrats = Label(text="Welcome Back!", bg = darkmodecolour, fg = "dodger blue")
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

			sorry = Label(text="Incorrect username or password.", bg = darkmodecolour, fg = "red")
			sorry.place(x=250, y=290, anchor= "center")


	except:
			try:
				errorr.destroy()
			except:
				pass
			sorry = Label(text="Incorrect username or password.", bg = darkmodecolour, fg = "red")
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
		errorr = Label(text = "Username not available. ", anchor='center', bg = darkmodecolour, fg = "red")
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
		errorr = Label(text = "Account created. ", anchor='center', bg = darkmodecolour, fg = "dodger blue")
		errorr.place(x= 250, y = 290, anchor = 'center')

def autosave1():
	global autosave


	#applying autosave settings
	with open("assets/settings.scn") as settingsfile:
		alllines = (settingsfile.readlines())
		autosave = str(alllines[0].strip())
	if autosave == "True":
		autosavebutton.configure(image = boxunchecked)
		autosave = "False"
	elif autosave == "False":
		autosavebutton.configure(image = boxchecked)
		autosave = "True"
	else:
		print("urmum")

	createsettingsfile()

def darkmode1():
	global darkmode
	with open("assets/settings.scn") as settingsfile:
		alllines1 = (settingsfile.readlines())
		darkmode = str(alllines1[1].strip())
	#applying darkmode settings 
	if darkmode == "True":
		darkmodebutton.configure(image = boxunchecked)
		darkmode = "False"
	elif darkmode == "False":
		darkmodebutton.configure(image = boxchecked)
		darkmode = "True"

	createsettingsfile()


def createsettingsfile():

	try:
		with open("assets/settings.scn", "w") as sosage:
			try:
				sosage.write(autosave)
				sosage.write("\n")
			except:
				sosage.write("False")
				sosage.write("\n")
			try:
				sosage.write(darkmode)
			except:
				sosage.write("True")
	except:
		traceback.print_exc()
		with open("assets/settings.scn", "x") as temp:
			pass
		with open("assets/settings.scn", "w") as idekanymore:
			idekanymore.write("False")
			idekanymore.write("\n")
			idekanymore.write("True")


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

	global PaschaHuevo
	global PaschaHuevoDark
	global backbutton
	backbutton = Button(text="Back", command = mainmenu, anchor='center', bg = darkmodecolour, activebackground= darkmodecolour, borderwidth=0, fg = lightmodecolour)
	backbutton.place(x= 20, y = 385, anchor = 'center')
	def checksautosavesetting():
		global PaschaHuevo
		global PaschaHuevoDark
		try:

			#opening settings file
			with open("assets/settings.scn") as settingsfile:
				notes = (settingsfile.readlines())
				lineautosave = str(notes[0])
				linedarkmode = str(notes[1])
				print("Auto save is "+ lineautosave)
				print("Dark mode is " + linedarkmode)
			
			#checking autosave setting
			if lineautosave.strip() == "True":
				print("print this if ur bad")
				PaschaHuevo = boxchecked
			elif lineautosave.strip() == "False":
				print("danil is best")
				PaschaHuevo = boxunchecked
			else:
				print("Autosave is " + lineautosave.strip())

			#checking darkmode settings
			if linedarkmode.strip() == "True":
				print("print this if ur bad")
				PaschaHuevoDark = boxchecked
			elif linedarkmode.strip() == "False":
				print("danil is best")
				PaschaHuevoDark = boxunchecked

		except:
			open("assets/settings.scn", "x")
			with open("assets/settings.scn", "w") as idekanymore:
				idekanymore.write("False")
				idekanymore.write("\n")
				idekanymore.write("True")
			checksautosavesetting()
	checksautosavesetting()
	print(PaschaHuevo)
	
	global autosavebutton
	autosavebutton = Button(image = PaschaHuevo, command = autosave1, anchor='center', bg = darkmodecolour, activebackground= darkmodecolour, borderwidth=0, fg = lightmodecolour)
	autosavebutton.place(x= 100, y = 115, anchor = 'center')

	global autosavelabel
	autosavelabel = Label(text = "- Autosave", bg = darkmodecolour, fg = lightmodecolour, anchor = 'center', font = ("Ariel", 15))
	autosavelabel.place(x = 120, y = 100)

	global darkmodebutton
	darkmodebutton = Button(image = PaschaHuevoDark, command = darkmode1, anchor='center', bg = darkmodecolour, activebackground= darkmodecolour, borderwidth=0, fg = lightmodecolour)
	darkmodebutton.place(x= 100, y = 155, anchor = 'center')

	global darkmodelabel
	darkmodelabel = Label(text = "- Darkmode (Requires Restart)", bg = darkmodecolour, fg = lightmodecolour, anchor = 'center', font = ("Ariel", 15))
	darkmodelabel.place(x = 120, y = 140)

	#10.4 width, 10y


def mainmenu():

	try:
		autosavelabel.destroy()
		autosavebutton.destroy()
		darkmodebutton.destroy()
		darkmodelabel.destroy()
		backbutton.destroy()
		settings.destroy()
	except:
		pass
	#reads logins from text file in assets
	global logins
	
	with open("assets/logins.scn") as dicti:
		for line in dicti:
			try:
				(key, val) = line.split()
				key, val = key.translate(decrypt_table), val.translate(decrypt_table)
				logins[key] = val
			except:
				pass
			

	global inputbar
	global inputbar2
	global logolock
	global ul
	global ul2
	#binding the enter key to the enter button 
	root.bind('<Return>', startlogin)



	#Placing Images + Text
	inputbar = Label(image = ib, bg = darkmodecolour)
	inputbar.place(x = 290, y = 200, anchor = 'center')

	inputbar2 = Label(image = ib, bg = darkmodecolour)
	inputbar2.place(x = 290, y = 180, anchor = 'center')

	logolock = Label(image = lock, bg = darkmodecolour)
	logolock.place(x = 250, y = 130, anchor = 'center')

	ul = Label(text = "Username:", bg = darkmodecolour, fg = lightmodecolour)
	ul.place(x = 40, y = 180, anchor = 'center')

	ul2 = Label(text = "Password:", bg = darkmodecolour, fg = lightmodecolour)
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
	signin = Button(image = sibutton, command = startlogin2, anchor='center', bg = darkmodecolour, activebackground= darkmodecolour, borderwidth=0, fg = lightmodecolour)
	signin.place(x= 250, y = 230, anchor = 'center')

	global signup
	signup = Button(image = subutton, command = sign_up_first, anchor='center', bg = darkmodecolour, activebackground= darkmodecolour, borderwidth=0, fg = lightmodecolour)
	signup.place(x= 250, y = 258, anchor = 'center')

	#settings button
	global settingsbutton
	settingsbutton = Button(image = settings_icon, command = opensettings, anchor='center', bg = darkmodecolour, activebackground= darkmodecolour, borderwidth=0, fg = lightmodecolour)
	settingsbutton.place(x= 485, y = 385, anchor = 'center')

mainmenu()

root.mainloop()
