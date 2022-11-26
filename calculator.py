import tkinter

def addition():

    l1.config(text="result = %d"%(int(e1.get()) + int(e2.get())))

def subtract():
    l1.config(text="result = %d"%(int(e1.get()) - int(e2.get())))

def multiply():
    l1.config(text="result = %d"%(int(e1.get()) * int(e2.get())))

def divide():
    l1.config(text="result = %d"%(int(e1.get()) / int(e2.get())))


masterWindow = tkinter.Tk()

masterWindow.geometry("324x324")


e1 = tkinter.Entry(masterWindow)
e1.grid(row = 0, column = 1)

e2 = tkinter.Entry(masterWindow)
e2.grid(row = 0, column = 4)

l1 = tkinter.Label(masterWindow, text = "result = ?")
l1.grid(row=2, column = 2, pady = 20)

b1 = tkinter.Button(masterWindow, text = "Add", command = addition, width = 10)
b1.grid(row = 3, column=1)

b2 = tkinter.Button(masterWindow, text = "Subtract", command = subtract, width = 10)
b2.grid(row = 3, column=2)

b3 = tkinter.Button(masterWindow, text = "Multiply", command = multiply, width = 10)
b3.grid(row = 3, column=4)

b4 = tkinter.Button(masterWindow, text = "Divide", command = divide, width = 10)
b4.grid(row = 3, column=4)

masterWindow.mainloop()