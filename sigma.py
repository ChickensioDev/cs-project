import pathlib, os
import mysql.connector
from customtkinter import *

app = CTk()
app.geometry("300x300")
f = open('cache.txt','r')
id = int(f.read())
conn = mysql.connector.connect(host='152.67.165.118', user = 'guest2', password='test', database = 'userinfo')
cursor = conn.cursor()
sql_insert_query = "SELECT * from login_info where id = '%s'" 
cursor.execute(sql_insert_query % id)
result = cursor.fetchall()
cursor.close()

label = CTkLabel(master=app,text = result, font=('Arial',30))
label.place(relx=0.5,rely=0.5,anchor='center')
app.mainloop()

