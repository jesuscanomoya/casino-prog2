import sqlite3


def bd_crear():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            dni VARCHAR(9) PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            contraseña VARCHAR NOT NULL,
            dinero INTEGER DEFAULT 10
        );
    ''')
    conn.commit()
    conn.close()


bd_crear()
