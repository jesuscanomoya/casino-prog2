import matplotlib.pyplot as plt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import numpy as np
import sqlite3
import time

class Grafica_balance():
    @staticmethod
    def graficar_balance(dni):
        conn = sqlite3.connect('hist_bal.db')
        cursor = conn.cursor()
        cursor.execute('SELECT dinero FROM hist_bal WHERE dni = ?', (str(dni),))
        user = cursor.fetchall()
        a = ([i[0] for i in user])
        print(a)
        conn.close()
        lista_aux = []
        # Data for plotting
        for i in range(0, len(a)):
            lista_aux.append(i)

        fig, ax = plt.subplots()
        ax.plot(lista_aux, a)

        ax.set(xlabel='time (s)', ylabel='Dinero',
               title='Historial crediticio')
        ax.grid()

        plt.savefig('Imagenes/hist_bal.png')
        plt.show()


    @staticmethod
    def meter_datos_bd(DNI, dinero):
        conn = sqlite3.connect('hist_bal.db')
        cursor = conn.cursor()

        try:
            cursor.execute('INSERT INTO hist_bal (dni, dinero, tiempo) VALUES (?, ?, ?)',
                           (DNI, dinero, time.time()))
            conn.commit()
            print("Todo sucedió bien")
        except sqlite3.IntegrityError:
            print("Esto no debería pasar")
        except sqlite3.OperationalError as e:
            print("Error operacional:", e)
        finally:
            conn.close()

    @staticmethod
    def eliminar_usuario(DNI):
        conn = sqlite3.connect('hist_bal.db')
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM hist_bal WHERE dni = ?', (DNI,))
            conn.commit()
            print("Usuario dado de baja correctamente.")
        except Exception as e:
            print("Error al dar de baja:", e)
        finally:
            conn.close()

if __name__ == '__main__':
    Grafica_balance.eliminar_usuario(1)
