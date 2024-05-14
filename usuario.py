import sqlite3
from hashlib import sha256
# from ventana import *


class Usuario:
    def __init__(self, dni, nombre, apellidos, contrasena):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.contrasena = self.hash_password(contrasena)

    @staticmethod
    def hash_password(contrasena):
        return sha256(contrasena.encode('utf-8')).hexdigest()

    def guardar_en_bd(self):
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
        except sqlite3.OperationalError as e:
            print("Error operacional:", e)
        finally:
            conn.close()

    @staticmethod
    def login(dni, contrasena):
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        hashed_password = sha256(contrasena.encode('utf-8')).hexdigest()
        cursor.execute('SELECT * FROM usuarios WHERE dni = ? AND contraseña = ?', (dni, hashed_password))
        user = cursor.fetchone()
        print(user)
        if user:
            cursor.execute('SELECT dinero FROM usuarios WHERE dni = ?', (user[0],))
            dinero = cursor.fetchone()[0]
            conn.close()
            print("Usuario registrado exitosamente!")
            return user[0], dinero
        else:
            conn.close()
            return False

    @staticmethod
    def cambiar_contrasena(dni, nueva_contrasena):
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

    @staticmethod
    def actualizar_dinero(dni, dinero):
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