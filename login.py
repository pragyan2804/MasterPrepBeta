#teacher login not integreated


from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import importlib
import mysql.connector as mysql

def loginaction():
	root = Tk()
	root.title("PrepMasterBETA")
	root.geometry("1280x720")
	root.resizable(False, False)
	bg = PhotoImage(file = "login.png")
	label1 = Label( root, image = bg)
	label1.place(x = 0, y = 0)

	user = StringVar()
	passwd = StringVar()
	usernametxt = Entry(root,
					textvariable=user,
					bg="#0c5dc0",
					justify="center",
					borderwidth=0,
					font="calibri 20",).place(x=443, y=350, width=435, height=55)

	passwordtxt = Entry(bg="#0c5dc0",
					textvariable=passwd,
					justify="center",
					font="calibri 20",
					borderwidth=0,
					show="*").place(x=443, y=470, width=435, height=55)

	def login1(e):
		mycon = mysql.connect(host='localhost', user='root', passwd='dhruv_789_$1', database='prepmaster')
		mycursor = mycon.cursor()
		mycursor.execute('select * from account_student;')
		account_teach = mycursor.fetchall()
		if user.get() == account_teach[0][0] and passwd.get() == account_teach[0][1]:
			messagebox.showinfo('showinfo','LOGIN SUCCESSFUL!')
			root.destroy()
			from homepage import homepageaction
			homepageaction()			
		else:
			messagebox.showinfo('showinfo','INVALID USERNAME OR PASSWORD')

	def login2():
		mycon = mysql.connect(host='localhost', user='root', passwd='dhruv_789_$1', database='prepmaster')
		mycursor = mycon.cursor()
		mycursor.execute('select * from account_student;')
		account_teach = mycursor.fetchall()
		if user.get() == account_teach[0][0] and passwd.get() == account_teach[0][1]:
			messagebox.showinfo('showinfo','LOGIN SUCCESSFUL!')
			root.destroy()
			from homepage import homepageaction
			homepageaction()
		else:
			messagebox.showinfo('showinfo','INVALID USERNAME OR PASSWORD')

	def signuppage():
		root.destroy()
		from signup import signupwindowaction
		signupwindowaction()

	Display = Button(root, 
					text ="START LEARNING!",
					font ="BurbankBigCondensed-Bold 25",
					bg="#57595c",
					command = lambda:login2()).place(x=535, y=552, width=250, height=50)
	root.bind('<Return>',login1)


	Display = Button(root,
					text="(OR CLICK HERE TO SIGN UP, IT'S FREE!)",
					font="BurbankBigCondensed-Bold 17",
					fg="white",
					bg="#0072ff",
					borderwidth=0,
					command = lambda:signuppage()).place(x=513, y=650, width=300, height=50)



	root.mainloop()

loginaction()