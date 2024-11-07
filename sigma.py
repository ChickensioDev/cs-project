import pathlib, os
import mysql.connector
from customtkinter import *
msgno = 0
def _import_data():
	f = open('cache.txt','r')
	id = int(f.read())
	sql_insert_query = "SELECT * from login_info where id = '%s'" 
	cursor.execute(sql_insert_query % id)
	result = cursor.fetchall()
	
	label = CTkLabel(master=app,text = result, font=('Arial',30))
	label.place(relx=0.5,rely=0.5,anchor='center')
	return id,result[0][1]

def _message():
	def _send():
		sql_insert_query ='''INSERT INTO messages(id,username,message) VALUES (%s, %s ,%s)'''
		sql_insert_tuple = (id,user,message.get())
		cursor.execute(sql_insert_query, sql_insert_tuple)
		conn.commit()
		
	def _check():
		global msgno
		conn.commit()
		cursor.execute('select * from messages')
		result = cursor.fetchall()
		
		for i in range(msgno,len(result)):
			displabel = CTkLabel(master=app, text = result[i])
			displabel.pack()
		msgno = len(result)
	def _close():
		sql_insert_query ='''delete from messages'''
		cursor.execute(sql_insert_query)
		conn.commit()
		cursor.close()
	message = StringVar()
	messagebox = CTkEntry(app,textvariable=message,font=("Times New Roman", 18),width = 150)
	
	submitbutton = CTkButton(app,text='submit',font=("Times New Roman", 18),command=_send,text_color='white',fg_color='green')
	checkbutton = CTkButton(app,text='check',font=("Times New Roman", 18),command=_check,text_color='white',fg_color='green')
	closebutton = CTkButton(app,text='close',font=("Times New Roman", 18),command=_close,text_color='white',fg_color='green')
	messagebox.place(relx = 0.8,rely=0.8)
	submitbutton.place(relx=0.8,rely=0.9)
	checkbutton.place(relx=0.8,rely=0.95)
	closebutton.place(relx=0.5,rely=0.95)
app = CTk()
app.geometry("900x900")
conn = mysql.connector.connect(host='152.67.165.118', user = 'guest2', password='test', database = 'userinfo')
cursor = conn.cursor()
data = _import_data()
id = data[0]
user = data[1]
_message()
app.mainloop()

'''def room1():
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
    win4=CTk()
    win4.geometry=("1600x900")
    win4.title("Room")

    label_name=CTkLabel(win4,text="Name",font=("Arial",28))
    label_name.place(relx=0.5,rely=0.5,anchor='center')
    label_pass=CTkLabel(win4,text="Password",font=("Arial",28))
    label_pass.place(relx=0.48,rely=0.6,anchor="center")

    name_var=StringVar()
    pass_var=StringVar()

    name_entry=CTkEntry(win4,textvariable=name_var,font=("Times New Roman",28),width=200)
    name_entry.place(relx=0.6,rely=0.5,anchor='center')
    pass_entry=CTkEntry(win4,textvariable=pass_var,font=("Times New Roman",28),width=200)
    pass_entry.place(relx=0.6,rely=0.6,anchor='center')

    create_button=CTkButton(win4,text='Create Room',font=("Times New Roman",28))
    create_button.place(relx=0.55,rely=0.7,anchor='center')

    win4.mainloop()

def join_room():
    win5=CTk()
    win5.geometry=("1600x900")

    label_name=CTkLabel(win5,text="Name",font=("Arial",28))
    label_name.place(relx=0.5,rely=0.5,anchor='center')
    label_pass=CTkLabel(win5,text="Password",font=("Arial",28))
    label_pass.place(relx=0.48,rely=0.6,anchor="center")

    name_var=StringVar()
    pass_var=StringVar()

    name_entry=CTkEntry(win5,textvariable=name_var,font=("Times New Roman",28),width=200)
    name_entry.place(relx=0.6,rely=0.5,anchor='center')
    pass_entry=CTkEntry(win5,textvariable=pass_var,font=("Times New Roman",28),width=200)
    pass_entry.place(relx=0.6,rely=0.6,anchor='center')

    join_button=CTkButton(win5,text='Join Room',font=("Times New Roman",28))
    join_button.place(relx=0.55,rely=0.7,anchor='center')

    win5.mainloop()
    
room1()'''
