import pathlib, os
import mysql.connector
from customtkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import tkinter as tk
import random
import time
msgno = 0
def _import_data():
	f = open('cache.txt','r')
	id = int(f.readline())
	room = f.readline()
	cursor.execute("use userinfo")
	sql_insert_query = "SELECT * from login_info where id = '%s'" 
	cursor.execute(sql_insert_query % id)
	result = cursor.fetchall()
	label = CTkLabel(app,text='User_Id: '+str(result[0][0])+'\nUsername: '+str(result[0][1])+'\nAge: '+str(result[0][3])+'\nGender: '+str(result[0][4])+'\nPassword: '+str(result[0][2]), font=('Arial',20),width=200,height=130)
	label.place(relx=0.5,rely=0.1,anchor='center')
	f.close()
	return id,result[0][1],room

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

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
		for i in range(len(result)-1,msgno-1,-1):
			displabel = CTkLabel(master=frame_2, text = result[i][2]+' : '+result[i][3]+'\n',bg_color='transparent',text_color='white',wraplength=200,font=('Arial',15))
			displabel.pack(side='bottom')
		msgno = len(result)
		print('bye')
		app.after(5000,_check)
	
	def _close():
		sql_insert_query ='''delete from messages'''
		cursor.execute(sql_insert_query)
		conn.commit()
		cursor.close()

	frame_2 = CTkFrame(app, corner_radius=15,width=260,height=500, fg_color="transparent") 
	frame_2.place(relx=0.8, rely=0.1)
	scroll = CTkScrollbar(master=frame_2,orientation='vertical')
	scroll.pack(side='right')
	frame_2.pack_propagate(False)
	message = StringVar()
	messagebox = CTkEntry(app,textvariable=message,font=("Times New Roman", 20),width = 235)
	
	submitbutton = CTkButton(app,text='Send',font=("Times New Roman", 18),command=_send,text_color='white',fg_color='green',width=100)
	checkbutton = CTkButton(app,text='check',font=("Times New Roman", 18),command=_check,text_color='white',fg_color='green',width=100)
	closebutton = CTkButton(app,text='close',font=("Times New Roman", 18),command=_close,text_color='white',fg_color='green')
	chatbox_label= CTkLabel(app,text='ChatBox',font=("Times New Roman", 18),width=260)

	chatbox_label.place(relx=0.8,rely=0.02)
	messagebox.place(relx = 0.81,rely=0.86)
	submitbutton.place(relx=0.82,rely=0.92)
	checkbutton.place(relx=0.9,rely=0.92)
	closebutton.place(relx=0.5,rely=0.95,anchor='center')

def _bgchange():
		list_bg= ['pic1.png','pic2.png','pic3.png','pic4.png','pic5.png','pic6.png','pic7.png','pic8.png','pic9.png']
		def _openimage():
			text= random.randint(0,8)
			image_ = list_bg[text]
			c_dir = pathlib.Path(__file__).parent.resolve()
			image_path1 = os.path.join(c_dir, image_)
			image_open = Image.open(image_path1)
			bg_image1 =CTkImage(dark_image=image_open,size=(1600,900))
			bg_label1 =CTkLabel(app, image=bg_image1,text=' ')
			bg_label1.place(relwidth=1, relheight=1) 
		_openimage()
		_funtions_menu()
		_message()
		_import_data()
		

def _todolist():
	to_do_win=CTkToplevel()
	to_do_win.config(bg='#09112e')
	to_do_win.geometry("400x600")
	to_do_win.title("To do list")
	remove_var=StringVar()
	label1=CTkLabel(to_do_win, text="To do List",font=("Times New Roman", 18), width=10,height=40, text_color='white',bg_color='dark blue')
	remove_task=CTkButton(to_do_win,text='Remove Task',font=("Times New Roman",18),width=30,height=30,fg_color='Red',bg_color='transparent',hover_color='dark blue')
	add_task=CTkButton(to_do_win,text="Add Task",width=100,height=30,font=("Times New Roman",18),bg_color='transparent',fg_color='green',hover_color='dark blue')
	remove_entry=CTkEntry(to_do_win,textvariable=remove_var,font=("Times New Roman",18),width=300)
	tasks_list=tk.Listbox(to_do_win,width=35,height=15,font=("Times New Roman",18),bg='grey')
	
	label1.place(relx=0.4,rely=0.1)
	add_task.place(relx=0.15,rely=0.2)
	remove_task.place(relx=0.55,rely=0.2)
	remove_entry.place(relx=0.15,rely=0.3)
	tasks_list.place(relx=0.1,rely=0.4)
	
	
		

	to_do_win.mainloop()
		
def _notes():
	frame_3=tk.Frame(app, width=400, height=400, background = 'black')
	frame_3.place(x = 300, y = 300)
	
	frame_3.bind("<Button-1>",drag_start)
	frame_3.bind("<B1-Motion>",drag_motion)
	text_box=CTkTextbox(frame_3,width=400,height=300,font=("Times New Roman",18))
	text_box.insert("1.0", "Write your notes here...")
	close_button=CTkButton(frame_3,text='X',fg_color='red',width=50,height=10,font=("Times New Roman",15),command=frame_3.destroy)
	close_button.place(relx=0.95, rely=0.05, anchor="center")
	text_box.place(anchor='center',relx=0.6,rely=0.5)



def _funtions_menu():

	timerbutton = CTkButton(app,text='Timer',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=100,height=50)
	calendarbutton = CTkButton(app,text='Calendar',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=100,height=50)
	musicbutton = CTkButton(app,text='Music',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=100,height=50)
	notesbutton = CTkButton(app,text='Notes',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=100,height=50,command=_notes)
	taskbutton = CTkButton(app,text='To-do list',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=100,height=50,command=_todolist)
	logoutbutton = CTkButton(app,text='Logout',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=100,height=50)
	bgchangebutton= CTkButton(app,text='Change\nBackground',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=100,height=50,command=_bgchange)

	timerbutton.place(relx=0.02,rely=0.3)
	calendarbutton.place(relx=0.02,rely=0.4)
	taskbutton.place(relx=0.02,rely=0.5)
	notesbutton.place(relx=0.02,rely=0.6)
	musicbutton.place(relx=0.02,rely=0.7)
	logoutbutton.place(relx=0.02,rely=0.92)
	bgchangebutton.place(relx=0.02,rely=0.2)

app = CTk()
app.geometry("1600x900")
conn = mysql.connector.connect(host='150.230.143.62', user = 'guest2', password='test')
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
