from tkinter import *
from database import connect

def login(root, success):
    def cek():
        conn = connect()
        c = conn.cursor()
        c.execute("SELECT role FROM users WHERE username=? AND password=?",
                  (u.get(), p.get()))
        r = c.fetchone()
        conn.close()
        if r:
            root.destroy()
            success(r[0])
        else:
            msg.config(text="Login gagal")

    Label(root,text="SADUD Login").pack()
    u=Entry(root);u.pack()
    p=Entry(root,show="*");p.pack()
    Button(root,text="Login",command=cek).pack()
    msg=Label(root,fg="red");msg.pack()
