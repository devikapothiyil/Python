
from tkinter import *

top = Tk()
top.title("Login page")
top.geometry("500x300")

def print_values():
    name=e1.get()
    reg=e2.get()
    print("Name: ",name)
    print("Register no:",reg)

name = Label(top, text="Name")
name.place(x=50, y=50)

reg = Label(top, text="Reg no:")
reg.place(x=50, y=100)  

e1 = Entry(top)
e1.place(x=100, y=50)
e2 = Entry(top)
e2.place(x=100, y=100)

b=Button(top,text="Enter",command=print_values)
b.place(x=200,y=150)

detail = Label(top, text="Details:")
detail.place(x=50, y=200)

#print_values()
top.mainloop()
