from tkinter import *

color = "#4287f5"

m = Tk()
m.configure(bg=color)
entry = StringVar()

m.geometry("255x404")
m.resizable(0,0)

f1 = Frame(m, highlightthickness=1, bg = "white", highlightbackground="white", highlightcolor="black")
f1.pack(side = TOP)

Entry(f1, textvariable=entry, width = 20, bg = "white", bd = 0, font=("Times New Roman", 17)).grid(row=0,column=1, pady=30, padx = 20)


f2 = Frame(m, highlightthickness=1, bg = "white", highlightbackground="black", highlightcolor="white", height=404, width=255)
f2.pack()

Button(f2, text="Clear", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 0, column=0, ipadx=90, ipady=25, columnspan=300)


Button(f2, text="Sin", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 1, column=0)
Button(f2, text="Cos", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 1, column=1)
Button(f2, text="Tan", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 1, column=2)

Button(f2, text="Sec", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 2, column=1)
Button(f2, text="Cos", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 2, column=0)
Button(f2, text="Cot", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 2, column=2)

Button(f2, text="Sine Inverse", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 3, column=0)
Button(f2, text="Cos Inverse", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 3, column=1)
Button(f2, text="Tan Inverse", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 3, column=2)

Button(f2, text="Cosec Inverse", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 4, column=0)
Button(f2, text="Sec Inverse", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 4, column=1)
Button(f2, text="Cot Inverse", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 4, column=2)

Button(f2, text="Factorial", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 5, column=0)
Button(f2, text="Ln", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 5, column=1)
Button(f2, text="Log Inverse", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 5, column=2)



f3 = Frame(m, highlightthickness=1, bg = "Grey", highlightbackground="Grey", highlightcolor="Grey", height=404, width=255)
f3.pack()


Button(f3, text="9", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 6, column=0)
Button(f3, text="8", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 6, column=1)
Button(f3, text="7", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 6, column=2)

Button(f3, text="6", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 7, column=0)
Button(f3, text="5", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 7, column=1)
Button(f3, text="4", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 7, column=2)

Button(f3, text="3", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 8, column=0)
Button(f3, text="2", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 8, column=1)
Button(f3, text="1", bd=1, bg = "white", width= 11, cursor="hand2", activebackground=color).grid(row = 8, column=2)

m.mainloop()