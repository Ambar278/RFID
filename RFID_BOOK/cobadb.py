import sqlite3

def insert_book(title, author, year):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("INSERT INTO books (title, author, year, available) VALUES (?, ?, ?, ?)", (title, author, year, True))
    conn.commit()
    conn.close()

try:
    title = input("Masukkan judul buku: ")
    author = input("Masukkan penulis buku: ")
    year = input("Masukkan tahun terbit: ")
    
    # Simpan informasi buku ke database
    insert_book(title, author, year)
    print("Data buku berhasil disimpan ke database!")
except Exception as e:
    print("Terjadi kesalahan:", e)