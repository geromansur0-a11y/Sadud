import tkinter as tk
from database import create_tables
from auth import login
from master_barang import master_barang
from pembelian import pembelian
from penjualan import penjualan
from laporan import laporan

def dashboard(role):
    win = tk.Tk()
    win.title("SADUD - Sistem Akuntansi Digital Usaha Dagang")
    win.geometry("400x350")

    tk.Label(
        win,
        text="SADUD",
        font=("Arial", 18, "bold")
    ).pack(pady=15)

    tk.Button(win, text="Data Barang", width=25, command=master_barang).pack(pady=5)
    tk.Button(win, text="Pembelian", width=25, command=pembelian).pack(pady=5)
    tk.Button(win, text="Penjualan", width=25, command=penjualan).pack(pady=5)
    tk.Button(win, text="Laporan", width=25, command=laporan).pack(pady=5)

    win.mainloop()

if __name__ == "__main__":
    create_tables()
    root = tk.Tk()
    login(root, dashboard)
    root.mainloop()
