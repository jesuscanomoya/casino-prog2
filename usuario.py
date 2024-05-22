import sqlite3
from hashlib import sha256
# from ventana import *
from Grafica_balance import *


class Usuario:
    """
    Clase que lleva a cabo la gestión total del usuario.

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

    Métodos
    -------
    hash_password(contrasena)
        Codifica la contraseña del usuario (función hashlib.sha256).
    guardar_en_bd()
        Guarda el usuario registrado en la base de datos 'usuarios.db'.
    login(dni, contrasena)
        Busca si el usuario está registrado en la base de datos.
    cambiar_contrasena(dni, nueva_contrasena)
        Cambia la contraseña del usuario correspondiente.
    eliminar_usuario(dni)
        Elimina el usuario correspondiente de la base de datos 'usuarios.db'.
    actualizar_dinero(dni, dinero)
        Modifica el valor del dinero del usuario en la base de datos.
    prohibir_entrada(dni)
        Marca un usuario como prohibido en la base de datos.

    Modificaciones en base de datos:  sqlite3.

    Todos métodos estáticos (a excepción de guardar_en_bd()).
    Comodidad para actuar como diversos usuarios y para iniciar/cerrar sesión.
    """
    def __init__(self, dni, nombre, apellidos, contrasena):
        """
        Parámetros
        ---------
        dni: str
            DNI/NIE del usuario. Identificador del usuario en el programa.
        nombre: str
            Nombre del usuario.
        apellidos: str
            Apellido/s del usuario.
        contrasena: str
            Contraseña del usuario. Necesaria para iniciar sesión.
            Codificada mediante la función sha256 de la librería hashlib.
        """
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.contrasena = self.hash_password(contrasena)

    @staticmethod
    def hash_password(contrasena):
        """
        Método estático
        Codifica la contraseña recibida (función hashlib.sha256).

        Parámetros
        ---------
        contrasena: str
            Contraseña a codificar.
        """
        return sha256(contrasena.encode('utf-8')).hexdigest()

    def guardar_en_bd(self):
        """
        Guarda el usuario registrado en la base de datos 'usuarios.db'

        Raises
        ------
        sqlite3.IntegrityError
            Ya existe un usuario con ese DNI/NIE (clave primaria).
        sqlite3.OperationalError
            Se produce un error operacional al intentar guardar el usuario.
        """
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        print(self.dni, self.nombre, self.apellidos, self.contrasena)

        try:
            cursor.execute('INSERT INTO usuarios (dni, nombre, apellidos, contraseña) VALUES (?, ?, ?, ?)',
                           (self.dni, self.nombre, self.apellidos, self.contrasena))
            conn.commit()
            print("Usuario registrado exitosamente!")
        except sqlite3.IntegrityError:
            print("El DNI ya existe en la base de datos.")
            conn.close()
            print("joal")
            return False
        except sqlite3.OperationalError as e:
            print("Error operacional:", e)
        finally:
            conn.close()
        Grafica_balance.meter_datos_bd(self.dni, 10)

    @staticmethod
    def login(dni, contrasena):
        """
        Método estático
        Busca si el usuario con dni y contraseña dados está registrado en la base de datos.
        Si lo encuentra, devuelve su dni y su dinero (que usará en los juegos del casino).

        Parámetros
        ---------
        dni: str
            DNI/NIE del usuario.
        contrasena: str
            Contraseña del usuario.
        """
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        hashed_password = sha256(contrasena.encode('utf-8')).hexdigest()
        cursor.execute('SELECT * FROM usuarios WHERE dni = ? AND contraseña = ?', (dni, hashed_password))
        user = cursor.fetchone()
        conn.close()
        if user:
            if user[-1]:
                print("Usuario con acceso prohibido")
                return False
            else:
                return user[0], user[-2]
        else:
            return False

    @staticmethod
    def cambiar_contrasena(dni, nueva_contrasena):
        """
        Método estático
        Cambia la contraseña del usuario con DNI/NIE dado.

        Parámetros
        ---------
        dni: str
            DNI/NIE del usuario.
        nueva_contrasena: str
            Nueva contraseña del usuario.
        """
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        try:
            new_password_hashed = Usuario.hash_password(nueva_contrasena)
            cursor.execute('UPDATE usuarios SET contraseña = ? WHERE dni = ?', (new_password_hashed, dni))
            conn.commit()
            print("Contraseña actualizada correctamente.")
        except Exception as e:
            print("Error al actualizar la contraseña:", e)
        finally:
            conn.close()

    @staticmethod
    def eliminar_usuario(dni):
        """
        Método estático
        Elimina de la base de datos al usuario con DNI/NIE dado.

        Parámetros
        ---------
        dni: str
            DNI/NIE del usuario a eliminar.
        """
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM usuarios WHERE dni = ?', (dni,))
            conn.commit()
            print("Usuario dado de baja correctamente.")
        except Exception as e:
            print("Error al dar de baja:", e)
        finally:
            conn.close()
        Grafica_balance.eliminar_usuario(dni)

    @staticmethod
    def actualizar_dinero(dni, dinero):
        """
        Método estático
        Modifica el valor del dinero del usuario en la base de datos.
        Usuario especificado por DNI/NIE dado.

        Parámetros
        ---------
        dni: str
            DNI/NIE del usuario.
        dinero: int
            Nueva cantidad de dinero a establecer en el perfil del usuario dentro de la base de datos.
        """
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        try:
            cursor.execute('UPDATE usuarios SET dinero = ? WHERE dni = ?', (dinero, dni))
            conn.commit()
            print("Capital actualizado correctamente.")
        except Exception as e:
            print("Error al actualizar el capital:", e)
        finally:
            conn.close()
        Grafica_balance.meter_datos_bd(dni, dinero)

    @staticmethod
    def prohibir_entrada(dni):
        """
        Método estático
        Establece la prohibición de entrada de un usuario con DNI/NIE dado.
        Marca al usuario como prohibido en la base de datos.

        Parámetros
        ---------
        dni: str
            DNI/NIE del usuario vetado de entrada.
        """
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        try:
            cursor.execute('UPDATE usuarios SET prohibido = ? WHERE dni = ?', (True, dni))
            conn.commit()
            print("Usuario restringido a partir de este momento.")
        except Exception as e:
            print("Error al restringir usuario:", e)
        finally:
            conn.close()
