import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainApp(QMainWindow):
    def __init__(self, titulo: str, parent=None, *args):
        super(MainApp, self).__init__(parent=parent)
        self.setWindowTitle('Casino')
        self.setWindowIcon(QIcon('Imagenes/icon.jpg'))
        self.setFixedSize(900, 800)
        self.titulo = titulo

        fondo = QLabel(self)
        fondo.setGeometry(-30, -70, 1024, 1024)
        fondo.setPixmap(QPixmap('Imagenes/fondo_inicio_sesion.jpeg'))


        label_menu = QLabel(self.titulo , self)
        label_menu.setGeometry(230,140,371,481)
        label_menu.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        label_menu.setStyleSheet("background-color: rgba(14, 146, 163, 0.5); border-width: 90px;  border-radius: 20px;")
        label_menu.setFont(QFont('MS Sans Serif', 20))

        user_label = QLabel("Usuario", self)
        user_label.setGeometry(280, 250, 231, 41)
        user_label.setFont(QFont('MS Shell Dlg 2', 10))

        password_label = QLabel("Contraseña", self)
        password_label.setGeometry(280, 350, 231, 41)
        password_label.setFont(QFont('MS Shell Dlg 2', 10))

        enter_button = QPushButton("Entrar", self)
        enter_button.setGeometry(360, 480, 93, 28)

        no_accounts_button = QPushButton("No tengo cuenta", self)
        no_accounts_button.setGeometry(350, 550, 110, 28)








class label():
    pass


if __name__ == '__main__':
    app = QApplication([])
    window = MainApp("Inicio de sesión")

    window.show()
    app.exec_()
