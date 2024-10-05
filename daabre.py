

import tkinter as tk
win1=tk.Tk()
win1.geometry("1600x900")
label = tk.Label(win1, text= "vanakkam da maapla", font = ('Arial', 18))
label.pack()
b1= tk.Button(win1,text='Hello world',bg='green')
b1.pack()
win2= tk.Tk()
win2.geometry('500x500')
b2= tk.Button(win2,text='New window',bg='Red',fg='White')
b2.pack()
win1.mainloop()
win2.mainloop()