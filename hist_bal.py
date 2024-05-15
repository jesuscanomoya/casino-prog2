import sqlite3


def bd_crear():
    conn = sqlite3.connect('hist_bal.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            dni VARCHAR(9),
            dinero INTEGER DEFAULT 10,
            tiempo FLOAT
        );
    ''')
    conn.commit()
    conn.close()


bd_crear()
