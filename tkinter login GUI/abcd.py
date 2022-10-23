import tkinter
from tkinter import ttk
from tkinter import *
# window creation
window = Tk()
window.geometry("600x500+300+100")
window.config(bg="blue")
# frame creation
name=StringVar()
passwd=StringVar()
f1=Frame(window,bg="blue")
f1.pack(side=TOP,fill=X)
# heading creation
l1=Label(f1,text="INSERT IN TO AZHAGAR",fg="black",bg="blue",font=("sans",30,"bold")).grid(row=1,columnspan=2,column=0)
# name entry creation
l2=Label(f1,text="NAME :",bg="blue",fg="black",pady=60,font=("sans",20)).grid(row=2,column=0,)
def abc():
	print(f'hello {name.get()},welcome to our tkinter programe!')
e1=Entry(f1,textvariable=name,bg="gray").grid(row=2,column=1)
# password entry creation
l3=Label(f1,text="PASSWORD :",bg="blue",fg="black",pady=10,font=("sans",20)).grid(row=3,column=0,)
e1=Entry(f1,textvariable=passwd,bg="gray").grid(row=3,column=1,pady=70)
# submit button creation
b1=Button(f1,text="submit",command=abc,bg="green",padx=30,pady=10).grid(row=4,column=0,columnspan=2)
window.mainloop()
