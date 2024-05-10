import matplotlib.pyplot as plt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import numpy as np

class Grafica_balance(QMainWindow):
    def __init__(self,hist_bal,parent=None, *args):
        super(Grafica_balance, self).__init__(parent=parent)
        self.setWindowTitle('Casino')  # Título de página
        self.setWindowIcon(QIcon('Imagenes/icon.jpg'))  # Icono de ventana
        self.setFixedSize(900, 800)  # Tamaño
        self.hist_balance=hist_bal

        # Data for plotting


        fig, ax = plt.subplots()
        ax.plot(t, s)

        ax.set(xlabel='time (s)', ylabel='Dinero',
               title='About as simple as it gets, folks')
        ax.grid()


        plt.show()










if __name__ == '__main__':
    app = QApplication([])
    grafico = Grafica_balance()


    grafico.show()
    app.exec_()

