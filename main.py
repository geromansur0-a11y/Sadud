from tkinter import 
from database import create_tables
from auth import login
from master_barang import master_barang
from pembelian import pembelian
from penjualan import penjualan
from laporan import laporan

def dashboard(role):
    w=Tk();w.title("SADUD")
    Label(w,text="SADUD",font=("Arial",18)).pack()

    Button(w,text="Barang",command=master_barang).pack()
    Button(w,text="Pembelian",command=pembelian).pack()
    Button(w,text="Penjualan",command=penjualan).pack()
    Button(w,text="Laporan",command=laporan).pack()

    w.mainloop()

if __name__=="__main__":
    create_tables()
    r=Tk()
    login(r,dashboard)
    r.mainloop()
