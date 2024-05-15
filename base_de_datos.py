"""
Creación Base de Datos

Este archivo se encarga de crear una base de datos para la gestión de usuarios del casino.
Se creará una tabla ('usuarios') en la que guardar los datos de todos los usuarios. Estos
datos podrán ser modificados por el programa de gestión de usuarios 'usuario.py'.

Atributos
---------
dni: str
    DNI/NIE del usuario. Identificador del usuario en el programa.
nombre: str
    Nombre del usuario.
apellidos: str
    Apellido/s del usuario.
contraseña: str
    Contraseña del usuario. Necesaria para iniciar sesión.
    Codificada mediante la función sha256 de la librería hashlib.
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
    conn.close()


bd_crear()
