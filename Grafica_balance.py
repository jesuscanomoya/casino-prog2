import matplotlib.pyplot as plt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import numpy as np
import sqlite3

class Grafica_balance(QMainWindow):
    def __init__(self,parent=None, *args):
        super(Grafica_balance, self).__init__(parent=parent)
        self.setWindowTitle('Casino')  # Título de página
        self.setWindowIcon(QIcon('Imagenes/icon.jpg'))  # Icono de ventana
        self.setFixedSize(900, 800)  # Tamaño
        conn = sqlite3.connect('hist_bal.db')
        cursor = conn.cursor()

        cursor.execute('SELECT dinero FROM hist_bal WHERE dni = 257 ',)
        user = cursor.fetchall()
        a= ([i[0] for i in user])
        print(a)
        conn.close()
        lista_aux=[]
        # Data for plotting
        for i in range(0,len(a)):
            lista_aux.append(i)

        fig, ax = plt.subplots()
        ax.plot(lista_aux, a)

        ax.set(xlabel='time (s)', ylabel='Dinero',
               title='Historial crediticio')
        ax.grid()

        plt.savefig('Imagenes/hist_bal.png')

        # Fondo
        self.fondo = QLabel(self)  # Creamos una etiqueta que va a ser el fondo de la ventana
        self.fondo.setGeometry(-30, -70, 1024, 1024)  # Su posición
        self.fondo.setPixmap(QPixmap('Imagenes/hist_bal.png'))  # Imagen de fondo










if __name__ == '__main__':
    app = QApplication([])
    grafico = Grafica_balance()


    grafico.show()
    app.exec_()

