import sqlite3

def get_connect():
    return sqlite3.connect("database.db")

def create_table():
    tables = [
        """
        CREATE TABLE IF NOT EXISTS users ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            fullname TEXT NOT NULL, 
            phone TEXT UNIQUE NOT NULL,
            adress TEXT NOT NULL,
            chat_id INTEGER UNIQUE NOT NULL,
            gender TEXT NOT NULL,
            is_admin BOOLEAN DEFAULT 0,
            is_block BOOLEAN DEFAULT 0
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS category ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            is_active BOOLEAN DEFAULT 1
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            image TEXT NOT NULL, 
            price INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            size TEXT,
            season TEXT,
            gerider_type TEXT,
            brand TEXT, 
            category_id INTEGER,
            FOREIGN KEY(category_id) REFERENCES category(id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            price INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            status TEXT DEFAULT 'new',
            FOREIGN KEY(chat_id) REFERENCES users(chat_id),
            FOREIGN KEY(product_id) REFERENCES product(id)
        );
        """
    ]

    with get_connect() as db:
        dbc = db.cursor()
        for i in tables:
            dbc.execute(i)
        db.commit()

create_table()
