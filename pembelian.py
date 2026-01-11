from tkinter import *
from database import connect
from datetime import datetime

def pembelian():
    w=Tk();w.title("Pembelian")

    barang=connect().cursor().execute("SELECT * FROM barang").fetchall()
    lb=Listbox(w);[lb.insert(END,b) for b in barang];lb.pack()

    qty=Entry(w);qty.pack()

    def simpan():
        b=barang[lb.curselection()[0]]
        q=int(qty.get())
        total=q*b[2]
        conn=connect();c=conn.cursor()
        c.execute("INSERT INTO pembelian VALUES(NULL,?,?,?,?)",
                  (b[0],q,total,datetime.now()))
        c.execute("UPDATE barang SET stok=stok+? WHERE id=?",(q,b[0]))
        c.execute("INSERT INTO jurnal VALUES(NULL,?,?,?,?,?)",
                  (datetime.now(),"Persediaan",total,0))
        c.execute("INSERT INTO jurnal VALUES(NULL,?,?,?,?,?)",
                  (datetime.now(),"Kas",0,total))
        conn.commit();conn.close()

    Button(w,text="Simpan",command=simpan).pack()
    w.mainloop()
