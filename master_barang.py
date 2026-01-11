from tkinter import *
from database import connect

def master_barang():
    w=Tk();w.title("Barang")

    def simpan():
        conn=connect();c=conn.cursor()
        c.execute("INSERT INTO barang VALUES(NULL,?,?,?)",
                  (n.get(),h.get(),s.get()))
        conn.commit();conn.close();tampil()

    def tampil():
        lb.delete(0,END)
        for r in connect().cursor().execute("SELECT * FROM barang"):
            lb.insert(END,r)

    n=Entry(w);h=Entry(w);s=Entry(w)
    Label(w,text="Nama").pack();n.pack()
    Label(w,text="Harga").pack();h.pack()
    Label(w,text="Stok").pack();s.pack()
    Button(w,text="Simpan",command=simpan).pack()
    lb=Listbox(w,width=50);lb.pack()
    tampil();w.mainloop()
