import tkinter as tk

def countdown(count):
    if running:
        label['text'] = f'Time Left: {count}'
        if count > 0:
            root.after(1000, countdown, count-1)

def start_timer():
    global running
    running = True
    countdown(10)

def stop_timer():
    global running
    running = False

root = tk.Tk()
running = False
label = tk.Label(root, text="Time Left: 10")
label.pack()
start_button = tk.Button(root, text='Start', command=start_timer)
start_button.pack()
stop_button = tk.Button(root, text='Stop', command=stop_timer)
stop_button.pack()
root.mainloop()
