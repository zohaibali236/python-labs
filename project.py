"""importing modules"""
from tkinter import messagebox
import mysql.connector as db
from tkinter import *
from datetime import datetime
from ctypes import windll
"""End of importing modules"""

user32 = windll.user32
sizeX = user32.GetSystemMetrics(0)
sizeY = user32.GetSystemMetrics(1)

def ConnectDB():
    try:
        dbHandle = db.connect (
            user = f"{str(UserNameEntry.get())}",
            password = f"{str(pwEntry.get())}",
            host = "localhost",
            database = "test"
        )
    except db.Error as error:
        messagebox.showerror("Error!", "Invalid Credentials")
        print(error, "at", datetime.now())
    else:
        global mysql_query
        mysql_query = dbHandle.cursor()


loginPage = Tk()

loginPage.title("Patients Record")


loginPage.geometry(f"{sizeX}x{sizeY}")


UserName = Label(loginPage, text="User Name")
UserName.place(relx=0.456, rely=0.35, anchor="center")


UserNameEntry = Entry(loginPage)
UserNameEntry.place(relx=0.48, rely=0.37, anchor="center")

pw = Label(loginPage, text="Password")
pw.place(relx=0.454, rely=0.4, anchor="center")


pwEntry = Entry(loginPage, show="*")
pwEntry.place(relx=0.48, rely=0.425, anchor="center")


loginButton = Button(loginPage, text="Login", command=ConnectDB)
loginButton.place(relx=0.48, rely=0.456, anchor="center")



loginPage.mainloop()
