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
            type TEXT CHECK(type IN ('Car', 'Motorcycle')),
            brand TEXT,
            model TEXT,
            year INTEGER,
            rental_price_per_day REAL,
            seating_capacity INTEGER, 
            engine_capacity INTEGER
        )
    """)
    execute_query(query)

create_table()