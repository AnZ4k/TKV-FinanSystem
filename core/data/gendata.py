import sqlite3 as sq

db = sq.connect('./data.db')

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS admin (
        login   TEXT NOT NULL,
        pass    TEXT NOT NULL
        
    );
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS data (
        saldo       TEXT,
        dividas     TEXT,
        nDividas    TEXT,
        datDiv      TEXT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        type            TEXT NOT NULL,
        action          TEXT NOT NULL,
        description     TEXT NOT NULL,
        ammount         TEXT NOT NULL
    )
""")