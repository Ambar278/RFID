import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sqlite3

reader = SimpleMFRC522()

def kembalikan_buku():
    conn = sqlite3.connect("perpustakaan.db")
    cursor = conn.cursor()

    print("Tempelkan tag RFID untuk mengembalikan buku...")
    uid, _ = reader.read()
    uid_str = str(uid)

    cursor.execute("SELECT peminjam FROM peminjaman WHERE uid = ?", (uid_str,))
    peminjaman = cursor.fetchone()

    if peminjaman:
        cursor.execute("DELETE FROM peminjaman WHERE uid = ?", (uid_str,))
        conn.commit()
        print("\nBuku berhasil dikembalikan!")
    else:
        print("Buku ini belum pernah dipinjam.")

    conn.close()

try:
    kembalikan_buku()
except KeyboardInterrupt:
    print("\nProses dihentikan.")
    GPIO.cleanup()
