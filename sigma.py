import pathlib, os
import mysql.connector
from customtkinter import *

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
		print(sql_insert_tuple)
		cursor.execute(sql_insert_query, sql_insert_tuple)
		conn.commit()
		
	def _check():
		sql_query = cursor.execute('select * from messages')
		result = cursor.fetchall()
		for i in range(0,len(result)):
			displabel = CTkLabel(master=app, text = result[i])
			displabel.pack()
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
print(id,user)
_message()
app.mainloop()
