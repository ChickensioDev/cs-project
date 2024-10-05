

import tkinter as tk
def _login():
	win2= tk.Tk()
	win2.geometry('500x500')
	b2= tk.Button(win2,text='New window',bg='Red',fg='White')
	b2.pack()
	win2.mainloop
	
def _welcome():
	win1=tk.Tk()
	win1.geometry("1600x900")
	label = tk.Label(win1, text= "vanakkam da maapla", font = ('Arial', 18))
	label.pack()
	b1= tk.Button(win1,text='Hello world',bg='green',  command = _login)
	b1.pack()

	a= tk.StringVar()
	b= tk.StringVar()
	cb= tk.Checkbutton(win1,text='male',variable=a)
	cb1= tk.Checkbutton(win1,text='female',variable=b)
	cb.pack()
	cb1.pack()
	win1.mainloop()

_welcome()
