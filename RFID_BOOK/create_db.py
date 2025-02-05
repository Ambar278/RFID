import sqlite3

# Membuat koneksi ke database SQLite
conn = sqlite3.connect('library.db')

# Membuat cursor
c = conn.cursor()

# Membuat tabel untuk buku
c.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    year INTEGER,
    available BOOLEAN
)
''')

# Membuat tabel untuk peminjaman
c.execute('''
CREATE TABLE IF NOT EXISTS borrowings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    borrowed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (book_id) REFERENCES books (id)
)
''')

# Menyimpan perubahan dan menutup koneksi
conn.commit()
conn.close()

print("Database dan tabel berhasil dibuat!")