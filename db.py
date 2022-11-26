from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as db

con = db.connect(
    host = "localhost",
    user = "root",
    database = "student"
)

m=Tk()


var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()


def display():
    for i in stable.get_children():
        stable.delete(i)
    cur1 = con.cursor()
    cur1.execute('select * from students')
    data = cur1.fetchall()
    if (len(data) != 0):
        for i in data:
            stable.insert("", END, values = i)
    cur1.close()

def insert():
    cur1=con.cursor()
    cur1.execute(f"INSERT INTO students(`NAME`, `CLASS`, `SECTION`) values('{var2.get()}','{var3.get()}','{var4.get()}')")
    con.commit()
    messagebox.showinfo("Insert", "One record has been added")
    display()
    cur1.close()
def delete():
    cur1=con.cursor()
    cur1.execute(f"DELETE FROM students WHERE ID={var1.get()}")
    con.commit()
    messagebox.showinfo("Delete","One record has been deleted")
    display()
    cur1.close()



l1=Label(m,bg="white",fg="black",text="Student Management System",font=("Times New Roman",45),bd=1)
l1.pack(side=TOP,fill=X)
f1=Frame(m,bg="white")
f1.place(x=10,y=100,width=450,height=650)
Label(f1,bg="white",fg="black",text="ID",font=("bold"),width=15,bd=15).grid(row=1,column=0,padx=50,pady=10)
Label(f1,bg="white",fg="black",text="NAME",font=("bold"),width=15,bd=15).grid(row=2,column=0,padx=50,pady=10)
Label(f1,bg="white",fg="black",text="CLASS",font=("bold"),width=15,bd=15).grid(row=3,column=0,padx=50,pady=10)
Label(f1,bg="white",fg="black",text="SECTION",font=("bold"),width=15,bd=15).grid(row=4,column=0,padx=50,pady=10)
Entry(f1,bg="white",fg="black",textvariable=var1,width=15,bd=1).grid(row=1,column=1)
Entry(f1,bg="white",fg="black",textvariable=var2,width=15,bd=1).grid(row=2,column=1)
Entry(f1,bg="white",fg="black",textvariable=var3,width=15,bd=1).grid(row=3,column=1)
Entry(f1,bg="white",fg="black",textvariable=var4,width=15,bd=1).grid(row=4,column=1)
Button(f1,text="Display",bg="white",fg="black",font=("bold"),width=15,bd=1,command=display).grid(row=5,column=0)
Button(f1,text="Insert",bg="white",fg="black",font=("bold"),width=15,bd=1,command=insert).grid(row=6,column=0)
Button(f1,text="Delete",bg="white",fg="black",font=("bold"),width=15,bd=1,command=delete).grid(row=7,column=0)

f2=Frame(m,bg="white")
f2.place(x=450,y=100,width=900,height=700)
stable=ttk.Treeview(f2,height=900,columns=("ID","NAME","CLASS","SECTION"))

stable.column("#0", width=0, minwidth=0)
stable.column("ID", width=100, minwidth=100, anchor=CENTER)
stable.column("NAME", width=100, minwidth=100, anchor=CENTER)
stable.column("CLASS", width=100, minwidth=100, anchor=CENTER)
stable.column("SECTION", width=100, anchor=CENTER)

stable.heading("ID", text="ID", anchor=CENTER)
stable.heading("NAME", text="Name", anchor=CENTER)
stable.heading("CLASS", text="Class", anchor=CENTER)
stable.heading("SECTION", text="Section", anchor=CENTER)
stable.pack()


m.mainloop()

con.close()