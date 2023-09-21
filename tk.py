from tkinter import *

import sqlite3
rt = Tk()
Label(rt,text="Registration Form",fg="white",font="DubaiMedium 12 bold",bg="black").grid(row = 0,column = 2,padx = 20,pady = 10)
Label(rt,text="Name").grid(row = 1,column = 1,padx = 10,pady = 10)
nameval=StringVar()
Entry(rt,textvariable=nameval).grid(row = 1,column = 2,padx = 10,pady = 10)

Label(rt,text="Email").grid(row = 2,column = 1,padx = 10,pady = 10)
email=StringVar()
Entry(rt,textvariable=email).grid(row = 2,column = 2,padx = 10,pady = 10)

Label(rt,text="Contact_no").grid(row = 3,column = 1,padx = 10,pady = 10)
phoneval=IntVar()
Entry(rt,textvariable=phoneval).grid(row = 3,column = 2,padx = 10,pady = 10)

Label(rt,text="Address").grid(row = 4,column = 1,padx = 10,pady = 10)
address=StringVar()
Entry(rt,textvariable=address).grid(row = 4,column = 2,padx = 10,pady = 10)

def create():
    conn = sqlite3.connect('C:/Users/dell/user.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users(id integer primary key autoincrement,Name TEXT,Email TEXT,Contact_no INT,Address TEXT,sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)")
    conn.commit()
    conn.close()
create()

def savedata():
    conn = sqlite3.connect('C:/Users/dell/user.db',timeout = 10)
    c = conn.cursor()
    c.execute('INSERT INTO users(Name,Email,Contact_no,Address) Values(?,?,?,?)',(nameval.get(),email.get(),phoneval.get(),address.get()))
    conn.commit()
    print("SAVED")


Button(rt,text="submit details",command=savedata).grid(padx=10,pady=10,row=5,column=1)



mainloop()
