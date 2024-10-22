import pathlib, os
import mysql.connector
from customtkinter import *
import daabre

app = CTk()
app.geometry("300x300")

label = CTkLabel(master=app,text = daabre.name, font=('Arial',30))
label.place(relx=0.5,rely=0.5,anchor='center')
app.mainloop()
conn = mysql.connector.connect(host='152.67.165.118', user = 'guest2', password='test', database = 'userinfo')
cursor = conn.cursor()
