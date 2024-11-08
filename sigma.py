import pathlib, os
import mysql.connector
from customtkinter import *
from PIL import Image
msgno = 0
def _import_data():
	f = open('cache.txt','r')
	id = int(f.readline())
	room = f.readline()
	cursor.execute("use userinfo")
	sql_insert_query = "SELECT * from login_info where id = '%s'" 
	cursor.execute(sql_insert_query % id)
	result = cursor.fetchall()
	label = CTkLabel(app,text=result, font=('Arial',20),height=28,width=260)
	label.place(relx=0.5,rely=0.03,anchor='center')
	
	return id,result[0][1],room

def _message():
	cursor.execute('use %s'%room)
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
			displabel = CTkLabel(master=app, text = result[i],bg_color='transparent',text_color='white')
			displabel.place(relx=0.82,rely=0.8)
		msgno = len(result)
	def _close():
		sql_insert_query ='''delete from messages'''
		cursor.execute(sql_insert_query)
		conn.commit()
		cursor.close()

	frame_2 = CTkFrame(app, corner_radius=15,width=260,height=670, fg_color="transparent") 
	frame_2.place(relx=0.8, rely=0.02)
	message = StringVar()
	messagebox = CTkEntry(app,textvariable=message,font=("Times New Roman", 20),width = 235)
	
	submitbutton = CTkButton(app,text='Send',font=("Times New Roman", 18),command=_send,text_color='white',fg_color='green',width=100)
	checkbutton = CTkButton(app,text='check',font=("Times New Roman", 18),command=_check,text_color='white',fg_color='green',width=100)
	closebutton = CTkButton(app,text='close',font=("Times New Roman", 18),command=_close,text_color='white',fg_color='green')
	chatbox_label= CTkLabel(app,text='ChatBox',font=("Times New Roman", 18),width=250)

	chatbox_label.place(relx=0.8,rely=0.02)
	messagebox.place(relx = 0.81,rely=0.86)
	submitbutton.place(relx=0.82,rely=0.92)
	checkbutton.place(relx=0.9,rely=0.92)
	closebutton.place(relx=0.5,rely=0.95,anchor='center')

def _funtions_menu():
	timerbutton = CTkButton(app,text='Timer',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=50,height=50)
	calendarbutton = CTkButton(app,text='Calendar',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=50,height=50)
	musicbutton = CTkButton(app,text='Music',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=50,height=50)
	notesbutton = CTkButton(app,text='Notes',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=50,height=50)
	taskbutton = CTkButton(app,text='To-do',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=50,height=50)
	
	timerbutton.place(relx=0.02,rely=0.2)
	calendarbutton.place(relx=0.02,rely=0.3)
	taskbutton.place(relx=0.02,rely=0.4)
	notesbutton.place(relx=0.02,rely=0.5)
	musicbutton.place(relx=0.02,rely=0.6)


app = CTk()
app.geometry("1600x900")
conn = mysql.connector.connect(host='152.67.165.118', user = 'guest2', password='test')
cursor = conn.cursor()
image_file = "bg_image.png"
curr_dir = pathlib.Path(__file__).parent.resolve()
image_path = os.path.join(curr_dir, image_file)

imag = Image.open(image_path)
bg_image =CTkImage(dark_image=imag,size=(1600,900))
bg_label =CTkLabel(app, image=bg_image,text=' ')
bg_label.place(relwidth=1, relheight=1) 

data = _import_data()
id = data[0]
user = data[1]
room = data[2]
_message()
_funtions_menu()
app.mainloop()
