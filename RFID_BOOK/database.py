import sqlite3

def create_tables():
    conn = sqlite3.connect("perpustakaan.db")
    cursor = conn.cursor()

    # Tabel Buku
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS buku (
        uid TEXT PRIMARY KEY,
        judul TEXT NOT NULL,
        penulis TEXT NOT NULL,
        tahun TEXT NOT NULL
    )
    """)

    # Tabel Peminjaman
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS peminjaman (
        uid TEXT PRIMARY KEY,
        peminjam TEXT NOT NULL,
        tanggal_pinjam TEXT NOT NULL,
        tanggal_kembali TEXT
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database berhasil dibuat!")
