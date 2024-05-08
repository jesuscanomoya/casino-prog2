import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# Cuando escribí esto, solo Dios y yo entendíamos lo que estaba haciendo
# Ahora ya solo lo sabe Dios.


class MainApp(QMainWindow):
    def __init__(self,titulo, parent=None, *args):
        super(MainApp, self).__init__(parent=parent)
        self.setWindowTitle('Casino')
        self.setWindowIcon(QIcon('Imagenes/icon.jpg'))
        self.setFixedSize(900, 800)
        self.titulo = titulo

        self.fondo = QLabel(self)
        self.fondo.setGeometry(-30, -70, 1024, 1024)
        self.fondo.setPixmap(QPixmap('Imagenes/fondo_inicio_sesion.jpeg'))

        self.label_menu = QLabel(self.titulo,parent= self)
        self.label_menu.setGeometry(230,140,371,481)
        self.label_menu.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.label_menu.setStyleSheet(
            "background-color: rgba(14, 146, 163, 0.5); border-width: 90px;  border-radius: 20px;"
        )
        self.label_menu.setFont(QFont('MS Sans Serif', 20))


        self.user_label = QLabel(text="Usuario", parent=self)
        self.user_label.setGeometry(280, 250, 231, 41)
        self.user_label.setFont(QFont('MS Shell Dlg 2', 10))

        self.password_label = QLabel("Contraseña", self)
        self.password_label.setGeometry(280, 350, 231, 41)
        self.password_label.setFont(QFont('MS Shell Dlg 2', 10))

        self.enter_button = QPushButton("Entrar", self)
        self.enter_button.setGeometry(360, 480, 93, 28)
        self.enter_button.clicked.connect(self.verificar_usuario)

        self.no_accounts_button = QPushButton("No tengo cuenta", self)
        self.no_accounts_button.setGeometry(350, 550, 110, 28)
        self.no_accounts_button.clicked.connect(self.pasar_a_registro)

        self.line_username = QLineEdit(self)
        self.line_username.setGeometry(280, 300, 231, 41)

        self.line_password = QLineEdit(self)
        self.line_password.setGeometry(280, 420, 231, 41)

        self.error_line = QLabel('Debes introducir bien los parámetros',self)
        self.error_line.setStyleSheet(
            "background-color: rgba(14, 146, 163, 0); color:red;font-weight: bold;"
        )
        self.error_line.setGeometry(250, 200, 400, 41)
        self.error_line.setFont(QFont('MS Shell Dlg 2', 10))


        self.error_line.hide()


    def pasar_a_registro(self):
        register.no_accounts_button.hide()
        register.show()
        self.hide()

    def verificar_usuario(self):
        if self.line_username.text() == '' and self.line_password.text() == '':
            self.error_line.show()
        else:
            nombre,contrasenya =self.line_username.text(), self.line_password.text()
            print(f'Nombre: {nombre}\nContraseña: {contrasenya}')


# class etiqueta(QLabel):
#     def __init__(self, parent=None,*args, **kwargs):
#         super(etiqueta, self).__init__(parent)
#         self.parent = parent


if __name__ == '__main__':
    app = QApplication([])
    log_in = MainApp("Iniciar sesion")
    register = MainApp("Registro de usuario")

    log_in.show()
    app.exec_()
