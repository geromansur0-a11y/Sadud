import sqlite3

def connect():
    return sqlite3.connect("sadud.db")

def create_tables():
    conn = connect()
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        role TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS barang(
        id INTEGER PRIMARY KEY,
        nama TEXT,
        harga REAL,
        stok INTEGER
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS supplier(
        id INTEGER PRIMARY KEY,
        nama TEXT,
        telp TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS pelanggan(
        id INTEGER PRIMARY KEY,
        nama TEXT,
        telp TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS pembelian(
        id INTEGER PRIMARY KEY,
        barang_id INTEGER,
        qty INTEGER,
        total REAL,
        tanggal TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS penjualan(
        id INTEGER PRIMARY KEY,
        barang_id INTEGER,
        qty INTEGER,
        total REAL,
        tanggal TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS jurnal(
        id INTEGER PRIMARY KEY,
        tanggal TEXT,
        akun TEXT,
        debit REAL,
        kredit REAL
    )""")

    c.execute("INSERT OR IGNORE INTO users VALUES (1,'admin','admin','admin')")
    conn.commit()
    conn.close()
