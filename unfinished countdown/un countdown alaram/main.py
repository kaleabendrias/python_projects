import time, subprocess,threading
from tkinter import *


def calculate():
    x = int(e1.get())
    alarm(x)


def alarm(x):
    listbox.delete(0, END)
    for i in range(x):
        y = x - i
        thread = threading.Thread(target=listbox.insert, args=[END, str(y)]).start()
        time.sleep(1)
    alarm1 = subprocess.Popen(['start', 'Alarm01.wav'], shell=True)


window= Tk()

window.title('Count Down')

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=2)

b1=Button(window,text='start', width=15, command=calculate)
b1.grid(row=1,column=2)

listbox=Listbox(window)
listbox.grid(row=2, column=2, columnspan=5)

window.mainloop()