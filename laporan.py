from tkinter import *
from database import connect

def laporan():
    w=Tk();w.title("Laporan")
    lb=Listbox(w,width=70);lb.pack()

    lb.insert(END,"=== PENJUALAN ===")
    for r in connect().cursor().execute("SELECT * FROM penjualan"):
        lb.insert(END,r)

    lb.insert(END,"=== LABA RUGI ===")
    c=connect().cursor()
    penjualan=c.execute("SELECT SUM(total) FROM penjualan").fetchone()[0] or 0
    pembelian=c.execute("SELECT SUM(total) FROM pembelian").fetchone()[0] or 0
    lb.insert(END,f"Laba Bersih : {penjualan-pembelian}")

    w.mainloop()
