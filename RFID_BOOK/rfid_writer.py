import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sqlite3

reader = SimpleMFRC522()

def insert_book(title, author, year):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("INSERT INTO books (title, author, year, available) VALUES (?, ?, ?, ?)", (title, author, year, True))
    conn.commit()
    conn.close()

try:
    print("Arahkan tag RFID ke reader untuk menulis data...")
    title = input("Masukkan judul buku: ")
    author = input("Masukkan penulis buku: ")
    year = input("Masukkan tahun terbit: ")
    
    # Format data yang akan disimpan
    book_info = f"{title};{author};{year}"
    
    reader.write(book_info)
    print("Data berhasil ditulis ke tag RFID!")
    
    # Simpan informasi buku ke database
    insert_book(title, author, year)
    print("Data buku berhasil disimpan ke database!")
except Exception as e:
    print("Terjadi kesalahan:", e)
finally:
    GPIO.cleanup()