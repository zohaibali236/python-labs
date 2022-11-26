from tkinter import *
from math import *


color = "#4287f5"
# color = "#FFCCFF"

m = Tk()
m.title("Scientific Calculator")
m.configure(bg="white")
entry = StringVar()

m.geometry("343x345")
m.resizable(0,0)

f1 = Frame(m, highlightthickness=1,bg = "white", highlightbackground="black", highlightcolor="black")
f1.pack(side = TOP)

e = Entry(f1, textvariable=entry, bd=1, width = 15, bg = "white", justify=RIGHT, font=("Times New Roman", 24))
e.grid(row=0,column=1, ipady=19, ipadx = 45, padx = 1)


f2 = Frame(m, highlightthickness=1, bg = "black", highlightbackground="white", highlightcolor="white", height=404, width=343)
f2.pack()

Button(f2, text="Clear", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set("")).grid(row = 0, column=0, ipadx=130, ipady=25, pady=0, columnspan=300)


Button(f2, text="Sin", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(sin(float(entry.get())))).grid(row = 1, column=0, padx=1, pady=1)
Button(f2, text="Cos", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(cos(float(entry.get())))).grid(row = 1, column=1, padx=1, pady=1)
Button(f2, text="Tan", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(tan(float(entry.get())))).grid(row = 1, column=2, padx=1, pady=1)

Button(f2, text="Sin¯¹", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(asin(float(entry.get())))).grid(row = 2, column=0, padx=1, pady=1)
Button(f2, text="Cos¯¹", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(acos(float(entry.get())))).grid(row = 2, column=1, padx=1, pady=1)
Button(f2, text="Tan¯¹", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(atan(float(entry.get())))).grid(row = 2, column=2, padx=1, pady=1)

Button(f2, text="Factorial", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(factorial(int(entry.get())))).grid(row = 3, column=0, padx=1, pady=1)
Button(f2, text="Ln", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(log(float(entry.get())))).grid(row = 3, column=1, padx=1, pady=1)
Button(f2, text="Log", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(log10(float(entry.get())))).grid(row = 3, column=2, padx=1, pady=1)


Button(f2, text="𝑥²", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(pow(float(entry.get()), 2))).grid(row = 1, column=3, padx=1, pady=1)
Button(f2, text="√x", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(sqrt(float(entry.get())))).grid(row = 2, column=3, padx=1, pady=1)
Button(f2, text="𝑥³", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(pow(float(entry.get()), 3))).grid(row = 3, column=3, padx=1, pady=1)


Button(f2, text="7", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(entry.get()+"7")).grid(row = 4, column=0, padx=1, pady=1)
Button(f2, text="8", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(entry.get()+"8")).grid(row = 4, column=1, padx=1, pady=1)
Button(f2, text="9", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(entry.get()+"9")).grid(row = 4, column=2, padx=1, pady=1)

Button(f2, text="4", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(entry.get()+"4")).grid(row = 5, column=0, padx=1, pady=1)
Button(f2, text="5", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(entry.get()+"5")).grid(row = 5, column=1, padx=1, pady=1)
Button(f2, text="6", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(entry.get()+"6")).grid(row = 5, column=2, padx=1, pady=1)

Button(f2, text="1", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(entry.get()+"1")).grid(row = 6, column=0, padx=1, pady=1)
Button(f2, text="2", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(entry.get()+"2")).grid(row = 6, column=1, padx=1, pady=1)
Button(f2, text="3", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(entry.get()+"3")).grid(row = 6, column=2, padx=1, pady=1)

Button(f2, text="0", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(entry.get()+"0")).grid(row = 7, column=0, padx=1, pady=1)
Button(f2, text=".", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(entry.get()+".")).grid(row = 7, column=1, padx=1, pady=1)
Button(f2, text="π", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(entry.get()+f"{pi}")).grid(row = 7, column=2, padx=1, pady=1)

Button(f2, text="+", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(entry.get()+"+")).grid(row = 4, column=3, padx=0, pady=1)
Button(f2, text="-", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(entry.get()+"-")).grid(row = 5, column=3, padx=0, pady=1)
Button(f2, text="x", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(entry.get()+"*")).grid(row = 6, column=3, padx=0, pady=1)
Button(f2, text="÷", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(entry.get()+"/")).grid(row = 7, column=3, padx=0, pady=1)

Button(f2, text="Ceil", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(ceil(float(entry.get())))).grid(row = 9, column=0, padx=1, pady=1)
Button(f2, text="Floor", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(floor(float(entry.get())))).grid(row = 9, column=1, padx=1, pady=1)
Button(f2, text="Round", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(round(float(entry.get())))).grid(row = 9, column=2, padx=1, pady=1)
Button(f2, text="Evaluate", bd=0,bg = "pink", width= 11, cursor="hand2", activebackground=color, command = lambda: entry.set(eval(entry.get()))).grid(row = 9, column=3, padx=1, pady=1)

m.mainloop()