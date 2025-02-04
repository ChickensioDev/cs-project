import pathlib, os
import mysql.connector
from customtkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import tkinter as tk
import random
import time
import tkcalendar
from tkcalendar import DateEntry
import csv,os

msgno = 0
flag = False
editing = False
note = False
def _import_data():	# data is imported from the text file from the user's system
	f = open('cache.txt','r') #1st line of the file is user id and second line of the file is name of the room
	id = int(f.readline())
	room = f.readline()
	cursor.execute("use userinfo")
	sql_insert_query = "SELECT * from login_info where id = '%s'" 
	cursor.execute(sql_insert_query % id)
	result = cursor.fetchall()
	label = CTkLabel(app,text='\nUser_Id: '+str(result[0][0])+'\nUsername: '+str(result[0][1])+'\nAge: '+str(result[0][3])+'\nGender: '+str(result[0][4])+'\nPassword: '+str(result[0][2]+'\nRoom: '+room), font=('Arial',20),width=200,height=130)
	label.place(relx=0.5,rely=0.15,anchor='center')
	f.close()
	return id,result[0][1],room #result[0][1] fetches the username

def drag_start(event):	
	global editing
	widget = event.widget
	widget.startX = event.x
	widget.startY = event.y
	editing = True
def drag_motion(event):		# function helps in moving the widgets
	global editing
	widget = event.widget
	x = widget.winfo_x() - widget.startX + event.x
	y = widget.winfo_y() - widget.startY + event.y
	
	widget.place(x=x,y=y)
	
	editing = True
'''
def  _create_csv():
		f= open('to-do-list.csv','w',newline='')
def _open_csv(mode,task):
		f=open('to-do-list.csv',mode,newline='')
		if mode=='a':
				obj=csv.writer(f)
				store=[task]
				obj.writerow(store)
		elif mode=='w':
				g= open('temp.csv','w',newline='')
				gobj=csv.writer(g)
				data=task
				d= csv.reader(f,delimiter=',')
				for x in d:
						if x!=data: gobj.writerow(x)
				g.close(); f.close()
				os.remove('to-do-list.csv')
				os.rename('temp,csv','to-do-list.csv')
		elif mode=='r':
				data=csv.reader(f,delimiter=',')
				return f
		f.close()
'''
def _message(): 	
		cursor.execute('use %s'%room)	
		def _send():	# messages are inserted into the sql table
			sql_insert_query ='''INSERT INTO messages(id,username,message) VALUES (%s, %s ,%s)'''
			sql_insert_tuple = (id,user,message.get())
			cursor.execute(sql_insert_query, sql_insert_tuple)
			conn.commit()
			messagebox.delete(0,tk.END)		# clears the entr box after sending message

		def _check():	# fetches the messages from the sql table
			global msgno
			conn.commit()
			cursor.execute('select * from messages')
			result = cursor.fetchall()
			for i in range(msgno, len(result)):
				displabel = CTkLabel(master=frame_2, text = result[i][2]+' : '+result[i][3]+'\n',bg_color='transparent',text_color='white',wraplength=200,font=('Arial',15))
				displabel.pack(side='top')		
			msgno = len(result)
		
		def _update():
			global flag
			if not flag:
				flag = True
			else:
				_check()
			app.after(1000,_update)		# the check function is executed ever 1000 milli second
		
		def _close():	  # deletes all the messages from the table
			sql_insert_query ='''delete from messages'''
			cursor.execute(sql_insert_query)
			conn.commit()
			cursor.close()

		frame_2 = CTkScrollableFrame(app, corner_radius=15,width=250,height=500, fg_color="transparent") 
		frame_2.place(relx=0.79, rely=0.1)

	
		message = StringVar()	# entry box for the message
		messagebox = CTkEntry(app,textvariable=message,font=("Times New Roman", 20),width = 235)
	
		submitbutton = CTkButton(app,text='Send',font=("Times New Roman", 18),command=_send,text_color='white',fg_color='green',width=200)
		checkbutton = CTkButton(app,text='check',font=("Times New Roman", 18),command=_check,text_color='white',fg_color='green',width=100)
		closebutton = CTkButton(app,text='close',font=("Times New Roman", 18),command=_close,text_color='white',fg_color='green')
		chatbox_label= CTkLabel(app,text='ChatBox',font=("Times New Roman", 18),width=260)

		chatbox_label.place(relx=0.8,rely=0.02)
		messagebox.place(relx = 0.81,rely=0.86)
		submitbutton.place(relx=0.83,rely=0.92)
		_update()
	
def _bgchange(): 	# changes the background
		list_bg= ['pic1.png','pic2.png','pic3.png','pic4.png','pic5.png','pic6.png','pic7.png','pic8.png','pic9.png']
		def _openimage():		# loads the image 
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


def _calendar():	# displays the calendar
	frame_5 = tk.Frame(app,width=350, height=350, background='#09112e')
	frame_5.place(x=350,y=500,anchor='center')
	frame_5.bind("<Button-1>",drag_start)
	frame_5.bind("<B1-Motion>",drag_motion)

	label1=CTkLabel(frame_5,text='Calendar',width=30,font=("Times New Roman",18))
	label1.place(x=1,y=1)
	close_button=CTkButton(frame_5,text='X',fg_color='red',width=30,height=10,font=("Times New Roman",15),command=frame_5.destroy)
	close_button.place(relx=0.95, rely=0.05, anchor="center")
	cal=DateEntry(frame_5,selectmode='day',width=20,font=("Times New Roman",15))
	cal.place(anchor='center',relx=0.35,rely=0.2)

	
def _timer():	# timer widget
	frame_4 = tk.Frame(app,width=200, height=300, background='#09112e')
	frame_4.place(x= 400, y= 300,anchor='center')
	frame_4.bind("<Button-1>",drag_start)
	frame_4.bind("<B1-Motion>",drag_motion)
	flag=False
	def _countdown():
			nonlocal flag
			global frame_time
			if flag==True:
				frame_time.destroy()
			
			frame_time=tk.Frame(frame_4,width=100,height=100,bg='#09112e')
			flag=True
			frame_time.place(relx=0.5,rely=0.6,anchor='center')
			label = tk.Label(frame_time, font=("Helvetica", 24), fg="red",bg='#09112e')
			label.pack()
			def _count(time):
					label.config(text=str(time))
					if time > 0:
						frame_time.after(1000, lambda: _count(time-1))
					else:
						label.config(text="Time's up!",fg="green")		
			try:
				a=int(minutes.get()) if minutes.get() else 0
				b=int(seconds.get()) if seconds.get() else 0
			except ValueError:
				messagebox.showerror("Error","Enter a valid time")
				frame_time.destroy()
				return
			time=a*60 +b
			if time>900:
				_count(time)
			else:
				frame_time.destroy()
				messagebox.showerror("Error","Enter time thats more than 15minutes")
			
	seconds= StringVar()	# enter the time
	minutes= StringVar() 
	
	sec_entry= CTkEntry(frame_4,textvariable=seconds,width=70,text_color='black',fg_color='violet',height=25)
	entry_label= CTkLabel(frame_4,text='Enter Time\n\nMinutes        Seconds  ',font=("Times New Roman", 18))
	entry_label.place(relx=0.06,rely=0.2)
	min_entry= CTkEntry(frame_4,textvariable=minutes,width=70,text_color='black',fg_color='violet',height=25)

	set_button = CTkButton(frame_4, text='Set Timer',text_color='white',width=80, fg_color='violet',hover_color='cyan',command=_countdown)
	sec_entry.place(relx=0.5,rely=0.44)
	min_entry.place(relx=0.1,rely=0.44)

	set_button.place(relx=0.3, rely= 0.7)
	close_button=CTkButton(frame_4,text='X',fg_color='red',width=30,height=10,font=("Times New Roman",15),command=frame_4.destroy)
	close_button.place(relx=0.95, rely=0.05, anchor="center")
		
def _todolist():	# to do list widget
	try: print("hi")
	except: a=5
	else:
		frame_6=tk.Frame(app,width=450,height=450,background='#09112e')
		frame_6.place(x=300,y=200)
		label1=CTkLabel(frame_6,text='To-do list',width=30,font=("Times New Roman",18))
		label1.place(x=1,y=1)		
		task_var=StringVar()	# entry box for task
		task_entry = CTkEntry(frame_6, textvariable=task_var, placeholder_text="Enter your task", width=200, height=30)
		task_entry.place(anchor='center',relx=0.5,rely=0.28)
		task_listbox = tk.Listbox(frame_6, width=30, height=10, font=("Times New Roman", 18), bg="black", fg="white")
		task_listbox.place(anchor="center", relx=0.5, rely=0.65)

		def add_task():		# adds the task to the list
			task=task_var.get()
			if task:
				task_listbox.insert(tk.END,task)
				task_var.set("")
			else:
				messagebox.showerror("Error",'Please enter a task to add')
		def remove_task():		# removes the task from the list
			selected_task=task_listbox.curselection() #Returns the selected task
			if selected_task:
				task_listbox.delete(selected_task)
			else:
				messagebox.showerror("Error",'Please select a task to remove')
		def task_done():	# marks the task as done (changes the colour basically)
			selected_task=task_listbox.curselection()
			if selected_task:
				task_listbox.itemconfig(selected_task,foreground='gray')
			else:
				messagebox.showerror("Error",'Please select a task to mark as done')
		def clear_selection(event):		
			if event.widget!=task_listbox: #clears selection only if left click is done outside the listbox
				task_listbox.selection_clear(0,END)
		def frame_click(event):
			clear_selection(event)
			drag_start(event)	
		
		add_task_button=CTkButton(frame_6,text='Add Task',fg_color='green',hover_color='#8A2BE2',width=100,height=30,command=add_task,font=("Times New Roman",18))
		add_task_button.place(anchor='center',relx=0.15,rely=0.15)
		
		remove_task_button=CTkButton(frame_6,text='Remove Task',fg_color='Red',hover_color='#8A2BE2',width=100,height=30,command=remove_task,font=("Times New Roman",18))
		remove_task_button.place(anchor='center',relx=0.46,rely=0.15)
		
		task_done_button=CTkButton(frame_6,text='Mark as done',fg_color='#03A9F4',hover_color='#8A2BE2',width=100,height=30,command=task_done,font=("Times New Roman",18))
		task_done_button.place(anchor='center',relx=0.78,rely=0.15)
		
		close_button=CTkButton(frame_6,text='X',fg_color='red',width=30,height=10,font=("Times New Roman",15),command=frame_6.destroy)
		close_button.place(relx=0.95, rely=0.05, anchor="center")
		frame_6.bind("<Button-1>",frame_click)
		frame_6.bind("<B1-Motion>",drag_motion)

def _notes():	
	global note
	delete = False
	create = True
	note = True
	cursor.execute("create table if not exists notewidget (wid int, message varchar(1000), posx int, posy int)")
	cursor.execute("select * from widgets")
	result = cursor.fetchall()
	for i in result:
		if i[1] == "note":
			create = False
	if create:
		cursor.execute("insert into widgets(wname) values ('note')")
	conn.commit()
	cursor.execute('select * from notewidget')
	result = cursor.fetchall()
	frame_3=tk.Frame(app, width=400, height=400, background = 'black')
	if result != []:
		frame_3.place(x = result[0][2], y = result[0][3])
	else:
		frame_3.place(x = 500, y = 500)
	text_box=CTkTextbox(frame_3,width=300,height=300,font=("Times New Roman",18))
	def _test(event):
		global editing
		editing = True
	def _save_notes(event):
		global editing, note
		nonlocal delete
		data = text_box.get('0.0',END)
		cursor.execute("update notewidget set message= %s, posx = %s, posy = %s",(data,frame_3.winfo_x(),frame_3.winfo_y()))
		if cursor.rowcount == 0:
			cursor.execute("insert into notewidget(message, posx, posy) values(%s,%s,%s)",(data, frame_3.winfo_x(), frame_3.winfo_y()))
		editing = False
		conn.commit()
		if delete:
			note = False
			frame_3.destroy()
	def _delete_set():
		nonlocal delete
		delete = True
		_save_notes(0)
	def _check():
		global editing
		cursor.execute('select * from notewidget')
		result = cursor.fetchall()
		
		if result != [] and editing == False:
			frame_3.place(x = result[0][2], y = result[0][3])
			text_box.delete(0.0,'end')
			text_box.insert(0.0, result[0][1])
		elif result != [] and editing == True:
			_save_notes(0)
	text_box.bind("<Key>", _test)	
	
	
		
	def _update():
		global flag
		nonlocal delete
		if not flag:
			flag = True
		elif delete != True:
			_check()
		app.after(1000,_update)
	frame_3.bind("<Button-1>",drag_start)
	frame_3.bind("<B1-Motion>",drag_motion)
	frame_3.bind('<ButtonRelease-1>', _save_notes)
	
	if result != []:
		text_box.insert('0.0',result[0][1])
	else:
		text_box.insert('0.0', 'type notes here....')
	close_button=CTkButton(frame_3,text='X',fg_color='red',width=50,height=10,font=("Times New Roman",15),command=_delete_set)
	close_button.place(relx=0.95, rely=0.05, anchor="center")
	text_box.place(anchor='center',relx=0.5,rely=0.5)
	data = text_box.get('1.0',END)
	_update()
	text_box.bind('<Return>', _save_notes)
	
def _notes_check():
	global note
	if note == False:
		_notes()
def _funtions_menu():
	cursor.execute("create table if not exists widgets (wid int primary key auto_increment, wname varchar(20))")
	timerbutton = CTkButton(app,text='Timer',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=100,height=50,command=_timer)
	calendarbutton = CTkButton(app,text='Calendar',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=100,height=50,command=_calendar)
	notesbutton = CTkButton(app,text='Notes',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=100,height=50,command=_notes_check)
	taskbutton = CTkButton(app,text='To-do list',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=100,height=50,command=_todolist)
	#logoutbutton = CTkButton(app,text='Logout',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=100,height=50)
	bgchangebutton= CTkButton(app,text='Change\nBackground',font=('Times New Roman',18),fg_color='purple',hover_color='violet',text_color='white',width=100,height=50,command=_bgchange)

	timerbutton.place(relx=0.02,rely=0.3)
	calendarbutton.place(relx=0.02,rely=0.4)
	taskbutton.place(relx=0.02,rely=0.5)
	notesbutton.place(relx=0.02,rely=0.6)
	#logoutbutton.place(relx=0.02,rely=0.92)
	bgchangebutton.place(relx=0.02,rely=0.2)
	

	   
	   

app = CTk()
app.geometry("1600x900")
app.title("App")
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
id = data[0] #user id
user = data[1] #username
room = data[2] #room name

_message()
_funtions_menu()

app.mainloop()
