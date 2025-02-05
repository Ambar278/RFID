import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sqlite3
import time

reader = SimpleMFRC522()

def borrow_book(book_id):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    
    # Cek ketersediaan buku
    c.execute("SELECT available FROM books WHERE id = ?", (book_id,))
    result = c.fetchone()
    
    if result and result[0]:  # Jika buku tersedia
        # Simpan peminjaman
        c.execute("INSERT INTO borrowings (book_id) VALUES (?)", (book_id,))
        c.execute("UPDATE books SET available = ? WHERE id = ?", (False, book_id))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False

def return_book(book_id):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    
    # Cek apakah buku dipinjam
    c.execute("SELECT id FROM borrowings WHERE book_id = ? AND returned_at IS NULL", (book_id,))
    result = c.fetchone()
    
    if result:  # Jika buku dipinjam
        # Update waktu pengembalian
        c.execute("UPDATE borrowings SET returned_at = CURRENT_TIMESTAMP WHERE book_id = ? AND returned_at IS NULL", (book_id,))
        c.execute("UPDATE books SET available = ? WHERE id = ?", (True, book_id))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False

try:
    while True:
        print("Arahkan tag RFID ke reader...")
        id, text = reader.read()
        print("ID Tag: ", id)
        
        # Memisahkan informasi buku
        title, author, year = text.split(';')
        print(f"Judul: {title}, Penulis: {author}, Tahun Terbit: {year}")
        
        # Tanyakan apakah pengguna ingin meminjam atau mengembalikan buku
        action = input("Apakah Anda ingin (1) meminjam atau (2) mengembalikan buku? (1/2): ")
        
        if action == '1':
            if borrow_book(id):
                print("Buku berhasil dipinjam!")
            else:
                print("Buku tidak tersedia!")
        elif action == '2':
            if return_book(id):
                print("Buku berhasil dikembalikan!")
            else:
                print("Buku tidak dipinjam!")
        else:
            print("Pilihan tidak valid!")
        
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()