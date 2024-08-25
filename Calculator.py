import tkinter as tk
from tkinter import *

root=tk.Tk()
#root.geometry("600x600")
root.title("Simple Calculator")
e=Entry(root,width=30,borderwidth=5)
e.grid(row=0,column=1,columnspan=3 ,padx=10,pady=20,)

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global fnum
    global math
    math="addition"
    fnum=int(first_number)
    e.delete(0, END)


def button_answer():
    second_number=e.get()
    e.delete(0,END)
    
    if math== "addition":
      e.insert(0, fnum + int(second_number))

    if math== "subtraction":
      e.insert(0, fnum - int(second_number))

    if math== "multiplication":
      e.insert(0, fnum * int(second_number))

    if math== "division":
      e.insert(0, fnum / int(second_number))

def button_subtract():     
    first_number=e.get()
    global fnum
    global math
    math="subtraction"
    fnum=int(first_number)
    e.delete(0, END)           

def button_multiply():
    first_number=e.get()
    global fnum
    global math
    math="multiplication"
    fnum=int(first_number)
    e.delete(0, END)

def button_divide():
    first_number=e.get()
    global fnum
    global math
    math="division"
    fnum=int(first_number)
    e.delete(0, END)


b1=Button(root,text="1",padx=40 ,pady=20 ,command=lambda:button_click(1))
b2=Button(root,text="2",padx=40 ,pady=20 ,command=lambda:button_click(2))
b3=Button(root,text="3",padx=40 ,pady=20 ,command=lambda:button_click(3))
b4=Button(root,text="4",padx= 40,pady=20 ,command=lambda:button_click(4))
b5=Button(root,text="5",padx=40 ,pady=20 ,command=lambda:button_click(5))
b6=Button(root,text="6",padx=40 ,pady=20 ,command=lambda:button_click(6))
b7=Button(root,text="7",padx=40 ,pady=20 ,command=lambda:button_click(7))
b8=Button(root,text="8",padx=40 ,pady=20 ,command=lambda:button_click(8))
b9=Button(root,text="9",padx=40 ,pady=20 ,command=lambda:button_click(9))
b0=Button(root,text="0",padx=40 ,pady=20 ,command=lambda:button_click(0))

clear=Button(root,text="A/C",padx=40,pady=20,command=button_clear)
answer=Button(root,text="=",padx=50,pady=20,command=button_answer)
add=Button(root,text="+",padx=40,pady=20,bg='Blue',command=button_add)
subtract=Button(root,text="-",padx=40,pady=20, command=button_subtract)
multiply=Button (root,text="x",padx=40,pady=20, command=button_multiply)
divide=Button(root,text="/",padx=40,pady=20, command=button_divide)

b1.grid(row= 4,column= 1 )
b2.grid(row= 4,column= 2 )
b3.grid(row= 4,column= 3 )

b4.grid(row= 3,column= 1 )
b5.grid(row= 3,column= 2 )
b6.grid(row= 3,column=  3)

b7.grid(row=2,column=1  )
b8.grid(row=2,column= 2 )
b9.grid(row=2,column=  3)

b0.grid(row= 5,column= 2 )

clear.grid(row=1,column=1)
answer.grid(row=1,column=4)
add.grid(row=2,column=4)
subtract.grid(row=5,column=4)
multiply.grid(row=3,column=4)
divide.grid(row=4,column=4)
root.mainloop()
