
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

#Called in both Login and Sign_up functions
def _successful_signin():
	current_dir = pathlib.Path(__file__).parent.resolve() # current directory

	subprocess.Popen(['python',os.path.join(current_dir,'befake.py')])
	sys.exit()
	
#This function is called in sign_up function
def _create_sql(n,a,p,g): #Name,Age,Password,Gender
	conn = mysql.connector.connect(host='150.230.143.62', user = 'guest2', password='test', database = 'userinfo')
	cursor = conn.cursor()
	cursor.execute('''select * from login_info where username = %s''',(n,))
	result = cursor.fetchall()
	if len(result) == 0: #Checking if the username already exists
		sql_insert_query = '''INSERT INTO login_info
                   (username,password,age,gender) VALUES (%s,%s,%s,%s)'''
		insert_tuple_1 = (n,p,a,g)
		cursor.execute(sql_insert_query,insert_tuple_1)
		conn.commit()  #Ensures that the changes are done in the database
		sql_insert_query = "SELECT id from login_info where username = '%s'" 
		cursor.execute(sql_insert_query % n)
		result = cursor.fetchall()
		cursor.close()
		f = open('cache.txt','w') 
		f.write(str(result[0][0]) + '\n') #Text file is created to store the user id in the users device
	else:
		msg.showerror("Error","Username already exists")
		return -1
		
#This function is called in Login function	
def _search_sql(n,p):
	conn = mysql.connector.connect(host='150.230.143.62', user = 'guest2', password='test', database = 'userinfo')
	cursor = conn.cursor()
	sql_insert_query = "SELECT password from login_info where username = '%s'" 
	cursor.execute(sql_insert_query % n)
	result = cursor.fetchall()
	if len(result) == 0:  #If the condition is true then username doesn't exist
		cursor.close()
		return -1
	elif result[0][0] == p: #If the condition is true then the password matches 
		sql_insert_query = "SELECT id from login_info where username = '%s'" 
		cursor.execute(sql_insert_query % n)
		result = cursor.fetchall()
		cursor.close()
		f = open('cache.txt','w')
		f.write(str(result[0][0]) + '\n') #result[0][0] gives user id
		cursor.close()
		return 1
	else:
		cursor.close()
		return 0
	
	
def _login():
	
	def close_window():
		win2.withdraw() # Hides the login window, win2
		win1.deiconify()  #Shows the hidden main window,win1 again
	win1.withdraw() #Hides the main window.win1
	win2= ctk.CTkToplevel() #Creates a Sub-window
	win2.geometry('500x500')
	win2.configure(fg_color='lightblue')
	win2.title("Login")
	email_var= ctk.StringVar()
	pass_var= ctk.StringVar()
	show_password = ctk.BooleanVar()
	
	img_file_name = "login1.png"
	current_dir = pathlib.Path(__file__).parent.resolve() # current directory
	img_path = os.path.join(current_dir, img_file_name)

	#Load the image using function Image from PIL
	image = Image.open(img_path)
	background_image =ctk.CTkImage(dark_image=image,size=(500,500))
	background_label = ctk.CTkLabel(win2, text = '', image=background_image)
	background_label.place(relwidth=1, relheight=1)  # Stretch the image to cover the window
	
	def _submit():
			if email_var.get() and pass_var.get(): #Checking if all attributes are entered
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
	login_label = ctk.CTkLabel(win2,text='Login',font=('Berlin Sans FB Demi',28),text_color='black',fg_color='lightblue')
	email_label= ctk.CTkLabel(win2,text='Username',font=("Berlin Sans FB Demi", 18),width=10,text_color='Black',fg_color='transparent')
	pass_label= ctk.CTkLabel(win2,text='Password',font=("Berlin Sans FB Demi", 18),width=10,text_color='Black',fg_color='transparent')

	email_entry= ctk.CTkEntry(win2,textvariable=email_var,font=("Berlin Sans FB Demi", 18),width = 150)
	pass_entry= ctk.CTkEntry(win2,textvariable=pass_var,font=("Berlin Sans FB Demi", 18),width = 150,show='*')
	
	submit_button= ctk.CTkButton(win2,text='Submit',font=("Berlin Sans FB Demi", 18),command=_submit,text_color='blue',fg_color='lightblue',hover_color='pink')
	close_button = ctk.CTkButton(win2, text='Back', font=("Berlin Sans FB Demi",14),text_color='blue',fg_color='lightblue', command=close_window,hover_color='pink')
	show_password_check = ctk.CTkCheckBox(win2, text='Show Password', variable=show_password, onvalue=True, offvalue=False, command=password_seen,text_color='Black')
	enter_value = ctk.CTkLabel(win2,text='',font=('arial',15),text_color='red',fg_color='white')
	
	win2.grid_rowconfigure(0, weight=1)  
	win2.grid_rowconfigure(1, weight=1)  
	login_label.grid(row=0, column=0, columnspan=2, sticky='ew', pady=10)
	login_label.grid(row=2, column=0,sticky='n')
	email_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
	email_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')
	pass_label.grid(row=4, column=0, padx=5, pady=5, sticky='e')
	pass_entry.grid(row=4, column=1, padx=5, pady=5, sticky='w')
	show_password_check.grid(row=5, column=1, sticky='w', padx=5, pady=5)
	submit_button.grid(row=6, column=0, pady=20)
	close_button.grid(row=6, column=1, pady=10)
	win2.grid_columnconfigure((0, 1), weight=1)
	

	win2.mainloop()

def _signup():
	def close_window():
		win4.withdraw() #Hides the window
		win1.deiconify() #Re-draws the window Welcome page is shown again
	
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
	img_file_name = "login1.png"
	current_dir = pathlib.Path(__file__).parent.resolve() # current directory
	img_path = os.path.join(current_dir, img_file_name)

	#Imagage.open is a function of PIL
	image = Image.open(img_path)
	background_image =ctk.CTkImage(dark_image=image,size=(500,500))
	background_label = ctk.CTkLabel(win4, image=background_image)
	background_label.place(relwidth=1, relheight=1)  # Stretch the image to cover the window
	
	def _submit():
		if age_var.get() and email_var.get() and pass_var.get() and gender_var.get() != 'o': #If all attributes are entered by the user
			if _create_sql(email_var.get(),age_var.get(), pass_var.get(),gender_var.get()) != -1: #Checking if username exists else creating new record
				_successful_signin()
		else:
			enter_value= ctk.CTkLabel(win4,text='Please enter values for all the fields',font=('arial',15),text_color='red',fg_color='white')
			enter_value.place(relx=0.5,rely=0.95, anchor="center")
	def password_seen():
		if show_password.get():
			pass_entry.configure(show='')
		else:
			pass_entry.configure(show='*')  # Hide the password with *)
	
	age_label = ctk.CTkLabel(win4, text="Age", font=("Times New Roman", 18), width=10, text_color='black')
	email_label = ctk.CTkLabel(win4, text='Username', font=("Times New Roman", 18), width=12, text_color='black')
	pass_label = ctk.CTkLabel(win4, text='Password', font=("Times New Roman", 18), width=12, text_color='black')

	age_entry = ctk.CTkEntry(win4, textvariable=age_var, font=("Times New Roman", 18), width=200)
	email_entry = ctk.CTkEntry(win4, textvariable=email_var, font=("Times New Roman", 18), width=200)
	pass_entry = ctk.CTkEntry(win4, textvariable=pass_var, font=("Times New Roman", 18), width=200, show='*')

	button1 = ctk.CTkRadioButton(win4, text='Male', variable=gender_var, font=("Times New Roman", 18), fg_color="Green", text_color='black', value="male", width=7)
	button2 = ctk.CTkRadioButton(win4, text='Female', variable=gender_var, font=("Times New Roman", 18), fg_color="Green", text_color='black', value="female", width=7)
	submit_button = ctk.CTkButton(win4, text='Submit', font=("Times New Roman", 18), command=_submit, fg_color='lightblue',text_color="blue",hover_color='pink')
	close_button = ctk.CTkButton(win4, text='Back', font=("Times New Roman", 14), text_color="blue", fg_color="lightblue", command=close_window,hover_color='pink')
	show_password_check = ctk.CTkCheckBox(win4, text='Show Password', variable=show_password, onvalue=True, offvalue=False, font=('Timer New Roman',12),command=password_seen, text_color='black',height=5)

	# Layout
	email_label.place(relx=0.2,rely=0.4)
	pass_label.place(relx=0.2,rely=0.5)
	age_label.place(relx=0.2,rely=0.6)
	email_entry.place(relx=0.4,rely=0.4)
	pass_entry.place(relx=0.4,rely=0.5)
	age_entry.place(relx=0.4,rely=0.6)
	button1.place(relx=0.2,rely=0.7)
	button2.place(relx=0.45,rely=0.7)
	submit_button.place(relx=0.2,rely=0.8)
	close_button.place(relx=0.5,rely=0.8)
	show_password_check.place(relx=0.4,rely=0.55)
	
	win4.mainloop()


def _welcome():
	
	global win1
	win1=ctk.CTk() #Creates a CTk window
	win1.title("Welcome")
	img_file_name = "welcome.png"
	current_dir = pathlib.Path(__file__).parent.resolve() # current directory
	img_path = os.path.join(current_dir, img_file_name)

	
	image = Image.open(img_path)  #Image is a function in PIL
	background_image =ctk.CTkImage(dark_image=image,size=(1000,900)) #Given image is opened in dark mode
	background_label = ctk.CTkLabel(win1, image=background_image)
	background_label.place(relwidth=1, relheight=1)  # Stretch the image to cover the window

	frame = ctk.CTkFrame(win1, corner_radius=15,width=600,height=400, fg_color="violet") 
	frame.place(relx=0.5, rely=0.55, anchor='center')

	win1.geometry("1000x900")
	title_label = ctk.CTkLabel(win1, text= "welcome!", font = ('broadway', 40),bg_color='purple')
	title_label.place(relx=0.5,rely=0.25,anchor='center')
	
	label1 = ctk.CTkLabel(win1, text= "Already have an account?", font = ('Berlin Sans FB Demi', 28),fg_color='purple',text_color= 'lightpink')
	label1.place(relx=0.5,rely=0.4,anchor='center')
	
	label2 = ctk.CTkLabel(win1, text= "New to the page?", font = ('Berlin Sans FB Demi', 28),fg_color='purple',text_color= 'lightpink')
	label2.place(relx=0.5,rely=0.6,anchor='center')
	
	b1= ctk.CTkButton(win1,text='Login',command = _login,fg_color='purple', text_color= 'white', width = 7, height=1, font = ("Berlin Sans FB Demi", 23))
	b1.place(relx=0.5,rely=0.5, anchor='center')
	
	b2= ctk.CTkButton(win1, command = _signup,text='Sign up',fg_color='purple',  text_color = 'white', width = 7, height=1,  font = ("Berlin Sans FB Demi", 23))
	b2.place(relx=0.5,rely=0.7,anchor = 'center')
	win1.mainloop()

_welcome()


	
