import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MainApp, self).__init__(parent=parent)
        self.setWindowTitle('Casino')
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setFixedSize(900, 800)

        fondo=QLabel(self)
        fondo.setGeometry(-30, -70, 1024, 1024)
        fondo.setPixmap(QPixmap('fondo_inicio_sesion.jpeg'))
        fondo.setStyleSheet("background-color: rgba(14, 146, 163, 0);")





        label_menu = QLabel("Inicio de sesión", self)
        label_menu.setGeometry(230,140,371,481)
        label_menu.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        label_menu.setStyleSheet("background-color: rgba(14, 146, 163, 0.5);")
        label_menu.setFont(QFont('MS Sans Serif', 20))






if __name__ == '__main__':
    app = QApplication([])
    window = MainApp()

    window.show()
    app.exec_()
