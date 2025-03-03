import sqlite3

def connect_db(db_file="vehicles.db"):
    return sqlite3.connect(db_file)

def execute_query(query, params=(), commit=False, fetch_one=False, fetch_all=False):
    with connect_db() as conn:
        cursor = conn.execute(query, params)
        result = None
        if fetch_one:
            result = cursor.fetchone()
        elif fetch_all:
            result = cursor.fetchall()
        if commit:
            conn.commit()
            result = cursor.lastrowid if cursor.lastrowid is not None else cursor.rowcount
        return result
    
def create_table():
    query = ("""--sql
        CREATE TABLE IF NOT EXISTS vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            rental_price_per_day REAL NOT NULL,
            seating_capacity INTEGER,
            engine_capacity INTEGER,
            UNIQUE (brand, model, year)
        )
    """)
    execute_query(query, commit=True)

create_table()