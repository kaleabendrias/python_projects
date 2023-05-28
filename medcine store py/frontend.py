from tkinter import *
import backend


def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),numberOfDoses_text.get()):
        list1.insert(END,row)


def add_command():
    backend.insert(title_text.get(), numberOfDoses_text.get())
    list1.delete(0, END)
    list1.insert(END,(title_text.get(), numberOfDoses_text.get()))


def update_command():
    try:
        backend.update(selected_tuple[0], title_text.get(), numberOfDoses_text.get())
        list1.delete(0, END)
        list1.insert(END, 'successfully updated'+ " "+ str(selected_tuple))
    except:
        list1.delete(0, END)
        list1.insert(END, 'please select a value tobe updated')

def delete_command():
    try:
        backend.delete(selected_tuple[0])
        list1.delete(0, END)
        list1.insert(0, 'successfully deleted'+' '+str(selected_tuple))
    except:
        list1.delete(0, END)
        list1.insert(END, 'please select a value to be deleted')

def delete_all_command():
    backend.delete_all()

def close_command():
    window.destroy()


window = Tk()

# set the apps title
window.title('Medicine store')

# show the title and number of doses
l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = Label(window, text='numberOfDoses')
l2.grid(row=0, column=2)

#  show the boxes of title and number of doses
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

numberOfDoses_text = StringVar()
e2 = Entry(window, textvariable=numberOfDoses_text)
e2.grid(row=0, column=3)

# Draw the list box
list1 = Listbox(window, height=8, width=35)
list1.grid(row=2, column=0, rowspan=7, columnspan=2)

# draw the scroll bar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=7)

# may yview helps us to scroll
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
# checks if we have selected and item from list box
list1.bind('<<ListboxSelect>>',get_selected_row)

# Draw the buttons
b1 = Button(window, text='View All', width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text='Search', width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text='Add', width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update selected', width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete selected', width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text='close', width=12, command=close_command)
b6.grid(row=7, column=3)

b7=Button(window, text='Delete All', width=12, command=delete_all_command)
b7.grid(row=8, column=3)

window.mainloop()
