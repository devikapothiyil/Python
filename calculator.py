from tkinter import *

top = Tk()
top.title("Calculator")
top.geometry("500x300")

def print_values():
    no1=int(e1.get())
    no2=int(e2.get())
    print("Number_1:",no1)
    print("Number_2:",no2)
    
    
def add():
     t.delete(0,END)
     no1=int(e1.get())
     no2=int(e2.get())
     r=no1+no2
     print("Result=",r)
     t.insert(0,r)

def sub():
     t.delete(0,END)
     no1=int(e1.get())
     no2=int(e2.get())
     r=no1-no2
     print("Result=",r)
     t.insert(0,r)

def multi():
     t.delete(0,END)
     no1=int(e1.get())
     no2=int(e2.get())
     r=no1*no2
     print("Result=",r)
     t.insert(0,r)

def divide():
     t.delete(0,END)
     no1=int(e1.get())
     no2=int(e2.get())
     r=no1/no2
     print("Result=",r)
     t.insert(0,r)

def clear_entry():
     e1.delete(0,END)
     e2.delete(0,END)
     t.delete(0,END)
     
no1 = Label(top, text="Number 1:")
no1.place(x=50, y=50)

no2 = Label(top, text="Number 2:")
no2.place(x=50, y=100)  

e1 = Entry(top)
e1.place(x=120, y=50)
e2 = Entry(top)
e2.place(x=120, y=100)

t=Entry(top)
t.place(x=100,y=200)

b=Button(top,text="+",command=add)
b.place(x=300,y=50)

b=Button(top,text="-",command=sub)
b.place(x=300,y=100)

b=Button(top,text="/",command=divide)
b.place(x=300,y=150)

b=Button(top,text="*",command=multi)
b.place(x=300,y=200)

b=Button(top,text="Clear",command=clear_entry)
b.place(x=300,y=250)

detail = Label(top, text="Result:")
detail.place(x=50, y=200)

top.mainloop()

top.mainloop()
