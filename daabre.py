

import tkinter as tk
from tkinter import PhotoImage

def _login():
	win2= tk.Tk()
	win2.geometry('500x500')
	
	email_var= tk.StringVar()
	pass_var= tk.StringVar()

	email_label= tk.Label(win2,text='Username')
	pass_label= tk.Label(win2,text='Password')

	email_entry= tk.Entry(win2,textvariable=email_var)
	pass_entry= tk.Entry(win2,textvariable=pass_var)
	submit_button= tk.Button(win2,text='Submit')

	email_label.grid(row=0,column=0)
	email_entry.grid(row=0,column=1)
	pass_label.grid(row=1,column=0)
	pass_entry.grid(row=1,column=1)
	submit_button.grid(row=2,column=1)

	win2.mainloop()
	win3= tk.tk()
	win3.geometry('1600x900')
	label= tk.Label(win3,text='Welcome to Cs project :)',font='Times New Roman',anchor='center',justify='center')
	label.pack(padx=20,pady=20)
	win3.mainloop()


def _welcome():
	win1=tk.Tk()
	win1.geometry("1600x900")
	label = tk.Label(win1, text= "vanakkam da maapla!", font = ('Arial', 28))
	label.pack(padx=20,pady=20)
	label1 = tk.Label(win1, text= " Do you have an account?", font = ('Arial', 24))
	label1.pack(padx=100,pady=100)
	label2 = tk.Label(win1, text= " If not please sign up", font = ('Arial', 24))
	label2.pack(padx=140,pady=140)
	b1= tk.Button(win1,text='Login',bg='green',  command = _login, fg = 'white', width = 10, font = ("Times New Roman", 30))
	b1.pack()
	b1.place(relx=0.5,rely=0.45, anchor='center')
	b2= tk.Button(win1,text='Sign up',bg='green',  command = _login, fg = 'white', width = 10,  font = ("Times New Roman", 30))
	b2.pack()
	b2.place(relx=0.5,rely=0.75,anchor = 'center')
	win1.mainloop()

_welcome()
