
import pathlib, os
import tkinter as tk
from tkinter import PhotoImage

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

	email_label= tk.Label(win2,text='Username',font=("Times New Roman", 18))
	pass_label= tk.Label(win2,text='Password',font=("Times New Roman", 18))

	email_entry= tk.Entry(win2,textvariable=email_var,font=("Times New Roman", 18))
	pass_entry= tk.Entry(win2,textvariable=pass_var,font=("Times New Roman", 18))
	submit_button= tk.Button(win2,text='Submit',font=("Times New Roman", 18),activeforeground='Green')
	close_button = tk.Button(win2, text='X', font=("Times New Roman", 14), bg="red", fg="white", command=close_window,height=1,width=2)
	

	email_label.grid(row=0,column=0)
	email_entry.grid(row=0,column=1)
	pass_label.grid(row=1,column=0)
	pass_entry.grid(row=1,column=1)
	submit_button.grid(row=2,column=1)
	close_button.place(relx=0.93,rely=0.03)


	win2.mainloop()
	win3= tk.Tk()
	win3.geometry('1600x900')
	label= tk.Label(win3,text='Welcome to Cs project :)',font='Times New Roman',anchor='center',justify='center')
	label.pack(padx=20,pady=20)
	win3.mainloop()

def _signup():
	def close_window():
		win4.withdraw() 
		win1.deiconify() 
	
	win1.withdraw()	
	win4 = tk.Toplevel()
	win4.title("Sign up")
	win4.geometry("500x500")
	win4.configure(bg="lightblue")
	win4.title("Sign Up")
	
	age_var=tk.StringVar()
	email_var=tk.StringVar()
	pass_var=tk.StringVar()
	gender_var = tk.StringVar(value="") 
	
	age_label=tk.Label(win4,text="           Age          ",font=("Times New Roman",18))
	email_label=tk.Label(win4,text='       Email id       ',font=("Times New Roman",18))
	pass_label=tk.Label(win4,text='      Password      ',font=("Times New Roman",18))
	
	age_entry=tk.Entry(win4,textvariable=age_var,font=("Times New Roman",18))
	email_entry=tk.Entry(win4,textvariable=email_var,font=("Times New Roman",18))
	pass_entry=tk.Entry(win4,textvariable=pass_var,font=("Times New Roman",18))
	
	button1=tk.Radiobutton(win4,text='Male',variable=gender_var,height=1,width=10,font=("Times New Roman",18),activeforeground="Green",value="male")
	button2=tk.Radiobutton(win4,text='Female',variable=gender_var,height=1,width=10,font=("Times New Roman",18),activeforeground="Green",value="female")
	submit_button= tk.Button(win4,text='Submit',font=("Times New Roman",18),activeforeground='Green')
	close_button = tk.Button(win4, text='X', font=("Times New Roman", 14), 
                         bg="red", fg="white", command=close_window)
	
	email_label.grid(row=0,column=0)
	email_entry.grid(row=0,column=1)
	pass_label.grid(row=1,column=0)
	pass_entry.grid(row=1,column=1)
	age_label.grid(row=2,column=0)
	age_entry.grid(row=2,column=1)
	button1.grid(row=3,column=0)
	button2.grid(row=3,column=1)
	submit_button.place(relx=0.4,rely=0.6)
	close_button.place(relx=1, rely=0.01, anchor='ne')
	
	win4.protocol("WM_DELETE_WINDOW", close_window)
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
	label1 = tk.Label(win1, text= " Do you have an account?", font = ('Arial', 24))
	label1.pack(padx=100,pady=100)
	label2 = tk.Label(win1, text= " If not please sign up", font = ('Arial', 24))
	label2.pack(padx=140,pady=140)
	b1= tk.Button(win1,text='Login',bg='green',  command = _login, fg = 'white', width = 10, font = ("Times New Roman", 30),activeforeground='Green')
	b1.pack()
	b1.place(relx=0.5,rely=0.45, anchor='center')
	b2= tk.Button(win1,text='Sign up',bg='green',  command = _signup, fg = 'white', width = 10,  font = ("Times New Roman", 30),activeforeground='Green')
	b2.pack()
	b2.place(relx=0.5,rely=0.75,anchor = 'center')
	win1.mainloop()

_welcome()
