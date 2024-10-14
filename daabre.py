
import pathlib, os
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox as msg
import mysql.connector

def add_user():
	pass

def _create_sql(n,a,p,g):
	conn = mysql.connector.connect(host='152.67.165.118', user = 'guest2', password='test', database = 'userinfo')
	cursor = conn.cursor()
	sql_insert_query = """ INSERT INTO login_info
                   (username,password,age,gender) VALUES (%s,%s,%s,%s)"""
	insert_tuple_1 = (n,p,a,g)
	cursor.execute(sql_insert_query,insert_tuple_1)
	conn.commit()
	cursor.close()
def _login():
	
	def close_window():
		win2.withdraw() # Hides the login window, win2
		win1.deiconify()  #Shows the hidden main window,win1 again
	win1.withdraw() #Hides the main window.win1
	win2= tk.Toplevel()
	win2.geometry('500x500')
	win2.configure(bg="lightblue")
	win2.title("Login")
	email_var= tk.StringVar()
	pass_var= tk.StringVar()
	show_password = tk.BooleanVar()

	def _submit():
		if email_var.get() and pass_var.get():
			win3= tk.Tk()
			win3.title("Be fake")
			win3.geometry('1600x900')
			label1= tk.Label(win3,text='Welcome to Cs project :)',font=('Times New Roman',20),anchor='center',justify='center')
			label1.pack(padx=20,pady=20)
			win3.mainloop()
		else:
			enter_value= tk.Label(win2,text='Please enter the username and password',font=('arial',15),fg='red',bg='white')
			enter_value.place(relx=0.5,rely=0.5, anchor="center")
	def password_seen():
		if show_password.get():
			pass_entry.config(show='')
		else:
			pass_entry.config(show='*')  # Hide the password with *)
	login_label = tk.Label(win2,text='Login',font=('Times New Roman',28))
	email_label= tk.Label(win2,text='Username',font=("Times New Roman", 18),width=10,)
	pass_label= tk.Label(win2,text='Password',font=("Times New Roman", 18),width=10)

	email_entry= tk.Entry(win2,textvariable=email_var,font=("Times New Roman", 18),width = 30)
	pass_entry= tk.Entry(win2,textvariable=pass_var,font=("Times New Roman", 18),width = 30,show='*')
	submit_button= tk.Button(win2,text='Submit',font=("Times New Roman", 18),activeforeground='Green',command=_submit)
	close_button = tk.Button(win2, text='Back', font=("Times New Roman", 14), activeforeground='Green', command=close_window,height=1,width=4)
	show_password_check = tk.Checkbutton(win2, text='Show Password', variable=show_password, onvalue=True, offvalue=False, command=password_seen)
	
	login_label.grid(row=0,column=0,columnspan=3,sticky='')
	email_label.grid(row=1,column=0)
	email_entry.grid(row=1,column=1)
	pass_label.grid(row=2,column=0)
	pass_entry.grid(row=2,column=1)
	show_password_check.grid(row=3, column=1, sticky='w')  # Place the checkbox below the password field
	submit_button.place(relx=0.5,rely=0.4,anchor="center",)
	close_button.place(relx=0.5,rely=0.9, anchor = "center")


	win2.mainloop()

def _signup():
	def close_window():
		win4.withdraw() 
		win1.deiconify() 
	
	win1.withdraw()	
	win4 = tk.Toplevel()
	win4.title("Sign up")
	win4.geometry("500x500")
	win4.configure(bg="lightblue")
	
	age_var=tk.StringVar()
	email_var=tk.StringVar()
	pass_var=tk.StringVar()		
	gender_var = tk.StringVar(value="o") 
	show_password = tk.BooleanVar()
	
	def _submit():
		if age_var.get() and email_var.get() and pass_var.get() and gender_var.get() != 'o':
			_create_sql(email_var.get(),age_var.get(), pass_var.get(),gender_var.get())
			win3= tk.Tk()
			win3.title("Befake")
			win3.geometry('1600x900')
			label1= tk.Label(win3,text='Welcome to Cs project :)',font=('Times New Roman',20),anchor='center',justify='center')
			label1.pack(padx=20,pady=20)
			win3.mainloop()
			
		else:
			enter_value= tk.Label(win4,text='Please enter values for all the fields',font=('arial',15),fg='red',bg='white')
			enter_value.place(relx=0.5,rely=0.5, anchor="center")
	def password_seen():
		if show_password.get():
			pass_entry.config(show='')
		else:
			pass_entry.config(show='*')  # Hide the password with *)
	
	age_label=tk.Label(win4,text="Age",font=("Times New Roman",18),width=10)
	email_label=tk.Label(win4,text='Username',font=("Times New Roman",18),width=10)
	pass_label=tk.Label(win4,text='Password',font=("Times New Roman",18),width=10)
	
	age_entry=tk.Entry(win4,textvariable=age_var,font=("Times New Roman",18),width = 20)
	email_entry=tk.Entry(win4,textvariable=email_var,font=("Times New Roman",18), width = 20)
	pass_entry=tk.Entry(win4,textvariable=pass_var,font=("Times New Roman",18),width = 20, show='*')
	
	button1=tk.Radiobutton(win4,text='Male',variable=gender_var,font=("Times New Roman",18),activeforeground="Green",value="male",width = 7)
	button2=tk.Radiobutton(win4,text='Female',variable=gender_var,font=("Times New Roman",18),activeforeground="Green",value="female",width=7)
	submit_button= tk.Button(win4,text='Submit',font=("Times New Roman",18),activeforeground='white', command=_submit)
	close_button = tk.Button(win4, text='Back', font=("Times New Roman", 14), bg="white", fg="black", command=close_window)
	show_password_check = tk.Checkbutton(win4, text='Show Password', variable=show_password, onvalue=True, offvalue=False, command=password_seen)
	
	email_label.grid(row=0,column=0)
	email_entry.grid(row=0,column=1)
	pass_label.grid(row=2,column=0)
	pass_entry.grid(row=2,column=1)
	show_password_check.grid(row=3, column=1, sticky='w') 
	age_label.grid(row=1,column=0)
	age_entry.grid(row=1,column=1)
	button1.grid(row=4,column=0,sticky='W')
	button2.grid(row=4,column=1,sticky='W')
	submit_button.place(relx=0.5,rely=0.4,anchor = 'center')
	close_button.place(relx=0.5, rely=0.9, anchor='center')
	win4.mainloop()


def _welcome():
	
	global win1
	win1=tk.Tk()
	img_file_name = "bg.png"
	current_dir = pathlib.Path(__file__).parent.resolve() # current directory
	img_path = os.path.join(current_dir, img_file_name)
	background_image = PhotoImage(file=img_path)
	background_label = tk.Label(win1, image=background_image)
	background_label.place(relwidth = 1, relheight = 1)  # Stretch the image to cover the window
	win1.geometry("1600x900")
	label = tk.Label(win1, text= "vanakkam da maapla!", font = ('Arial', 28))
	label.pack(padx=20,pady=20)
	label1 = tk.Label(win1, text= "Already have an account?", font = ('Arial', 24))
	label1.pack()
	label1.place(relx=0.5,rely=0.3,anchor='center')
	label2 = tk.Label(win1, text= "New to the page?", font = ('Arial', 24))
	label2.pack()
	label2.place(relx=0.5,rely=0.6,anchor='center')
	b1= tk.Button(win1,text='Login',bg='green',  command = _login, fg = 'white', width = 7, height=1, font = ("Times New Roman", 30),activeforeground='Green')
	b1.pack()
	b1.place(relx=0.5,rely=0.4, anchor='center')
	b2= tk.Button(win1,text='Sign up',bg='green',  command = _signup, fg = 'white', width = 7, height=1,  font = ("Times New Roman", 30),activeforeground='Green')
	b2.pack()
	b2.place(relx=0.5,rely=0.7,anchor = 'center')
	win1.mainloop()

_welcome()


	
