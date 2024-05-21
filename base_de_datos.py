"""
Creación Base de Datos

Este archivo se encarga de crear una base de datos para la gestión de usuarios del casino.
Se creará una tabla ('usuarios') en la que guardar los datos de todos los usuarios. Estos
datos podrán ser modificados por el programa de gestión de usuarios 'usuario.py'.
Por otro lado, se creará una tabla 'hist_bal' que guardará las modificaciones de capital de
todos los usuarios. De esta tabla obtendremos el historial de cada usuario en el archivo
'Grafica_balance.py'.
"""

import sqlite3


def bd_crear():
    """
    Crea tanto la base de datos ('usuarios.db') como la tabla 'usuarios'.

    Atributos de la tabla 'usuarios'
    --------------------------------
    dni: varchar, longitud 9, clave primaria
        DNI/NIE del usuario. Identificador del usuario en el programa.
    nombre: text, valor no nulo
        Nombre del usuario.
    apellidos: text, valor no nulo
        Apellidos del usuario.
    contraseña: varchar, valor no nulo
        Contraseña del usuario.
    dinero: integer, por defecto 10
        Dinero del que dispone el usuario.
    prohibido: boolean, por defecto False
        Indica si el usuario tiene la entrada prohibida.

    Atributos de la tabla 'hist_bal'
    --------------------------------
    id: integer, valor en autoincremento, clave primaria
        Id de la modificación. Añade valor automático.
    tiempo: float, valor no nulo
        Momento en el que se realiza la modificación. Recibido de time.time().
    dni: varchar, longitud 9, valor no nulo
        DNI/NIE del usuario. Clave ajena procedente de 'usuarios'.
    dinero: integer, por defecto 10
        Dinero del que dispone el usuario (modificación). Clave ajena procedente de 'usuarios'.
    """
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            dni VARCHAR(9) PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            contraseña VARCHAR NOT NULL,
            dinero INTEGER DEFAULT 10,
            prohibido BOOLEAN DEFAULT False
        );
    ''')
    conn.commit()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hist_bal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tiempo FLOAT NOT NULL,
            dni VARCHAR(9) NOT NULL,
            dinero INTEGER DEFAULT 10,
            FOREIGN KEY (dni, dinero) REFERENCES usuarios(dni, dinero)
        );
    ''')
    conn.commit()
    conn.close()


bd_crear()
