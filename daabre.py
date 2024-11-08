
import pathlib, os
import PIL
from PIL import Image
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox as msg
import mysql.connector
import customtkinter as ctk
import subprocess
import sys


def _successful_signin():
	current_dir = pathlib.Path(__file__).parent.resolve() # current directory

	subprocess.Popen(['python',os.path.join(current_dir,'befake.py')])
	sys.exit()
	

def _create_sql(n,a,p,g):
	conn = mysql.connector.connect(host='152.67.165.118', user = 'guest2', password='test', database = 'userinfo')
	cursor = conn.cursor()
	sql_insert_query = '''INSERT INTO login_info
                   (username,password,age,gender) VALUES (%s,%s,%s,%s)'''
	insert_tuple_1 = (n,p,a,g)
	cursor.execute(sql_insert_query,insert_tuple_1)
	conn.commit()
	sql_insert_query = "SELECT id from login_info where username = '%s'" 
	cursor.execute(sql_insert_query % n)
	result = cursor.fetchall()
	cursor.close()
	f = open('cache.txt','w')
	f.write(str(result[0][0]) + '\n')
	
def _search_sql(n,p):
	conn = mysql.connector.connect(host='152.67.165.118', user = 'guest2', password='test', database = 'userinfo')
	cursor = conn.cursor()
	sql_insert_query = "SELECT password from login_info where username = '%s'" 
	cursor.execute(sql_insert_query % n)
	result = cursor.fetchall()
	if len(result) == 0:
		cursor.close()
		return -1
	elif result[0][0] == p:
		sql_insert_query = "SELECT id from login_info where username = '%s'" 
		cursor.execute(sql_insert_query % n)
		result = cursor.fetchall()
		cursor.close()
		f = open('cache.txt','w')
		f.write(str(result[0][0]) + '\n')
		cursor.close()
		return 1
	else:
		cursor.close()
		return 0
	
	

def _login():
	
	def close_window():
		win2.iconify() # Hides the login window, win2
		win1.deiconify()  #Shows the hidden main window,win1 again
	win1.withdraw() #Hides the main window.win1
	win2= ctk.CTkToplevel()
	win2.geometry('500x500')
	win2.configure(fg_color='lightblue')
	win2.title("Login")
	email_var= ctk.StringVar()
	pass_var= ctk.StringVar()
	show_password = ctk.BooleanVar()
	enter_value = ctk.CTkLabel(win2,text='',font=('arial',15),text_color='red',fg_color='white')
	
	def _submit():
			if email_var.get() and pass_var.get():
				if _search_sql(email_var.get(), pass_var.get()) == 1:
					_successful_signin()
				elif _search_sql(email_var.get(), pass_var.get()) == 0:
				 enter_value.configure(text="incorrect password")
				elif _search_sql(email_var.get(), pass_var.get()) == -1:
					enter_value.configure(text="username does not exist")
			else:
				enter_value.configure(text="Please enter the username and password")
			enter_value.place(relx=0.5,rely=0.5,anchor='center')
	def password_seen():
		if show_password.get():
			pass_entry.configure(show='')
		else:
			pass_entry.configure(show='*')  # Hide the password with *)
	login_label = ctk.CTkLabel(win2,text='Login',font=('Times New Roman',28),text_color='black',fg_color='transparent')
	email_label= ctk.CTkLabel(win2,text='Username',font=("Times New Roman", 18),width=10,text_color='Black',fg_color='transparent')
	pass_label= ctk.CTkLabel(win2,text='Password',font=("Times New Roman", 18),width=10,text_color='Black',fg_color='transparent')

	email_entry= ctk.CTkEntry(win2,textvariable=email_var,font=("Times New Roman", 18),width = 150)
	pass_entry= ctk.CTkEntry(win2,textvariable=pass_var,font=("Times New Roman", 18),width = 150,show='*')
	
	submit_button= ctk.CTkButton(win2,text='Submit',font=("Times New Roman", 18),command=_submit,text_color='white',fg_color='green')
	close_button = ctk.CTkButton(win2, text='Back', font=("Times New Roman",14),text_color='white',fg_color='green', command=close_window)
	show_password_check = ctk.CTkCheckBox(win2, text='Show Password', variable=show_password, onvalue=True, offvalue=False, command=password_seen,text_color='Black')
	
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
	win4 = ctk.CTkToplevel()
	win4.title("Sign up")
	win4.geometry("500x500")
	win4.configure(fg_color="lightblue")
	
	age_var=ctk.StringVar()
	email_var=ctk.StringVar()
	pass_var=ctk.StringVar()		
	gender_var = ctk.StringVar(value="o") 
	show_password = ctk.BooleanVar()
	
	def _submit():
		if age_var.get() and email_var.get() and pass_var.get() and gender_var.get() != 'o':
			_create_sql(email_var.get(),age_var.get(), pass_var.get(),gender_var.get())
			_successful_signin()
		else:
			enter_value= ctk.CTkLabel(win4,text='Please enter values for all the fields',font=('arial',15),text_color='red',fg_color='white')
			enter_value.place(relx=0.5,rely=0.5, anchor="center")
	def password_seen():
		if show_password.get():
			pass_entry.configure(show='')
		else:
			pass_entry.configure(show='*')  # Hide the password with *)
	
	age_label=ctk.CTkLabel(win4,text="Age",font=("Times New Roman",18),width=10,text_color='black')
	email_label=ctk.CTkLabel(win4,text='Username',font=("Times New Roman",18),width=10,text_color='black')
	pass_label=ctk.CTkLabel(win4,text='Password',font=("Times New Roman",18),width=10,text_color='black')
	
	age_entry=ctk.CTkEntry(win4,textvariable=age_var,font=("Times New Roman",18),width = 200)
	email_entry=ctk.CTkEntry(win4,textvariable=email_var,font=("Times New Roman",18), width = 200)
	pass_entry=ctk.CTkEntry(win4,textvariable=pass_var,font=("Times New Roman",18),width = 200, show='*')
	
	button1=ctk.CTkRadioButton(win4,text='Male',variable=gender_var,font=("Times New Roman",18),fg_color="Green",text_color='black',value="male",width = 7)
	button2=ctk.CTkRadioButton(win4,text='Female',variable=gender_var,font=("Times New Roman",18),fg_color="Green",text_color='black',value="female",width=7)
	submit_button= ctk.CTkButton(win4,text='Submit',font=("Times New Roman",18), command=_submit,fg_color='Green')
	close_button = ctk.CTkButton(win4, text='Back', font=("Times New Roman", 14), text_color="white", fg_color="green", command=close_window)
	show_password_check = ctk.CTkCheckBox(win4, text='Show Password', variable=show_password, onvalue=True, offvalue=False, command=password_seen,text_color='black')
	
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
	win1=ctk.CTk() #Creates a CTk window
	win1.title("Welcome")
	img_file_name = "bg.png"
	current_dir = pathlib.Path(__file__).parent.resolve() # current directory
	img_path = os.path.join(current_dir, img_file_name)

	#Load the image using Pillow
	image = Image.open(img_path)
	background_image =ctk.CTkImage(dark_image=image,size=(1600,900))
	background_label = ctk.CTkLabel(win1, image=background_image)
	background_label.place(relwidth=1, relheight=1)  # Stretch the image to cover the window

	frame = ctk.CTkFrame(win1, corner_radius=15,width=600,height=600, fg_color="transparent") 
	frame.place(relx=0.5, rely=0.5, anchor='center')

	win1.geometry("1600x900")
	title_label = ctk.CTkLabel(win1, text= "welcome!", font = ('Arial', 28),bg_color='transparent')
	title_label.place(relx=0.5,rely=0.2,anchor='center')
	
	label1 = ctk.CTkLabel(win1, text= "Already have an account?", font = ('Arial', 24))
	label1.place(relx=0.5,rely=0.3,anchor='center')
	
	label2 = ctk.CTkLabel(win1, text= "New to the page?", font = ('Arial', 24))
	label2.place(relx=0.5,rely=0.6,anchor='center')
	
	b1= ctk.CTkButton(win1,text='Login',command = _login,fg_color='green', text_color= 'white', width = 7, height=1, font = ("Times New Roman", 30))
	b1.place(relx=0.5,rely=0.4, anchor='center')
	
	b2= ctk.CTkButton(win1, command = _signup,text='Sign up',fg_color='green',  text_color = 'white', width = 7, height=1,  font = ("Times New Roman", 30))
	b2.place(relx=0.5,rely=0.7,anchor = 'center')
	win1.mainloop()

_welcome()


	
