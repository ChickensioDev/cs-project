import pathlib, os
import mysql.connector
from customtkinter import *
import subprocess
def _import_data():
	f = open('cache.txt','r')
	id = int(f.readline())
	
	cursor.execute("use userinfo")
	sql_insert_query = "SELECT * from login_info where id = '%s'" 
	cursor.execute(sql_insert_query % id)
	result = cursor.fetchall()

	f.close()
	return id,result[0][1]
def create_pressed(n,p):
	cursor.execute('''create database %s'''%n)
	cursor.execute('''use %s'''%n)
	cursor.execute('''create table messages (mid int primary key auto_increment, id int, username varchar(20),message varchar(3000))''')
	
	cursor.execute('''use userinfo''')
	cursor.execute('''insert into room_info(id,room,password) values (%s, %s, %s)''',(id,n,p))
	conn.commit()
	f = open("cache.txt","w")
	f.write(str(id) + '\n')
	f.write(n + '\n')
	f.close()
	current_dir = pathlib.Path(__file__).parent.resolve() # current directory
	subprocess.Popen(['python',os.path.join(current_dir,'sigma.py')])
	sys.exit()

def join_pressed(n,p):
	cursor.execute('''use userinfo''')
	cursor.execute('select * from room_info where room = %s', (n,))
	result = cursor.fetchall()
	if len(result) != 0:
		if result[0][3] == p:
			f = open("cache.txt",'w')
			f.write(str(id) + '\n')
			f.write(n + '\n')
			f.close()
			current_dir = pathlib.Path(__file__).parent.resolve() # current directory
			subprocess.Popen(['python',os.path.join(current_dir,'sigma.py')])
			sys.exit()
		else:
			pass ###remove this line and add text that says password incorrect
	else:
		pass ###remove this line and add text that says acc not found
	
def room1():
	win3=CTk()
	win3.geometry("1600x900")
	win3.title("Be fake")

	frame=CTkFrame(win3,corner_radius=15,width=600,height=600,fg_color='black')
	frame.place(relx=0.5,rely=0.5,anchor='center')
	
	label1=CTkLabel(win3,text='welcome to befake',font=('Arial',28))
	label1.place(relx=0.5,rely=0.5,anchor='center')

	button1=CTkButton(win3,text='Create Room',font=("Arial",28),command=create_room)
	button2=CTkButton(win3,text='Join Room',font=("Arial",28),command=join_room)

	button1.place(relx=0.4,rely=0.6,anchor='center')
	button2.place(relx=0.6,rely=0.6,anchor='center')
	win3.mainloop()

def create_room():
	win4=CTkToplevel()
	win4.geometry("1600x900")
	win4.title("Room")

	label_name=CTkLabel(win4,text="Name",font=("Arial",28))
	label_name.place(relx=0.5,rely=0.5,anchor='center')
	label_pass=CTkLabel(win4,text="Password",font=("Arial",28))
	label_pass.place(relx=0.48,rely=0.6,anchor="center")
	show_password = BooleanVar()

	name_var=StringVar()
	pass_var=StringVar()
	def password_seen():
		if show_password.get():
				pass_entry.configure(show='')
		else:
				pass_entry.configure(show='*')  # Hide the password with *)
	name_entry=CTkEntry(win4,textvariable=name_var,font=("Times New Roman",28),width=200)
	name_entry.place(relx=0.6,rely=0.5,anchor='center')
	pass_entry=CTkEntry(win4,textvariable=pass_var,font=("Times New Roman",28),width=200, show = "*")
	pass_entry.place(relx=0.6,rely=0.6,anchor='center')
	show_password_check = CTkCheckBox(win4, text='Show Password', variable=show_password, onvalue=True, offvalue=False, command=password_seen,text_color='white')
	show_password_check.place(relx=0.58,rely=0.65,anchor='center')
	def pressed():
		print(pass_var.get(),name_var.get())
		if pass_var.get() and name_var.get():
			create_pressed(name_var.get(),pass_var.get())
	create_button=CTkButton(win4,text='Create Room',font=("Times New Roman",28), command = pressed)
	create_button.place(relx=0.55,rely=0.7,anchor='center')

	win4.mainloop()

def join_room():
	win5=CTkToplevel()
	win5.geometry("1600x900")
	label_name=CTkLabel(win5,text="Name",font=("Arial",28))
	label_name.place(relx=0.5,rely=0.5,anchor='center')
	label_pass=CTkLabel(win5,text="Password",font=("Arial",28))
	label_pass.place(relx=0.48,rely=0.6,anchor="center")
	show_password = BooleanVar()
	name_var=StringVar()
	pass_var=StringVar()
	def password_seen():
		if show_password.get():
				pass_entry.configure(show='')
		else:
				pass_entry.configure(show='*')  # Hide the password with *)
	def pressed():
		if pass_var.get() and name_var.get():
			join_pressed(name_var.get(),pass_var.get())
	name_entry=CTkEntry(win5,textvariable=name_var,font=("Times New Roman",28),width=200)
	name_entry.place(relx=0.6,rely=0.5,anchor='center')
	pass_entry=CTkEntry(win5,textvariable=pass_var,font=("Times New Roman",28),width=200, show = "*")
	pass_entry.place(relx=0.6,rely=0.6,anchor='center')
	show_password_check = CTkCheckBox(win5, text='Show Password', variable=show_password, onvalue=True, offvalue=False, command=password_seen,text_color='white')
	show_password_check.place(relx=0.58,rely=0.65,anchor='center')
	join_button=CTkButton(win5,text='Join Room',font=("Times New Roman",28), command = pressed)
	join_button.place(relx=0.55,rely=0.7,anchor='center')

	win5.mainloop()
conn = mysql.connector.connect(host='152.67.165.118', user = 'guest2', password='test')
cursor = conn.cursor()
data = _import_data()
id = data[0]
user = data[1]

room1()
