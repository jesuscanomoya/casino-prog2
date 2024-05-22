import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from usuario import *

# Cuando escribí esto, solo Dios y yo entendíamos lo que estaba haciendo
# Ahora ya solo lo sabe Dios.

# Creamos la clase para la ventana
class MainApp(QMainWindow):
    def __init__(self,titulo, parent=None, *args):  # Inicializamos los parámetros
        super(MainApp, self).__init__(parent=parent)  # Super_init para obtener la información de la clase QMainWindow
        self.setWindowTitle('Casino') # Título de página
        self.setWindowIcon(QIcon('Imagenes/icon.jpg'))  # Icono de ventana
        self.setFixedSize(900, 1000)  # Tamaño
        self.titulo = titulo  # Parámetro para ver el título de la página

        # ----------------Etiquetas------------------#
        # Fondo
        self.fondo = QLabel(self)  # Creamos una etiqueta que va a ser el fondo de la ventana
        self.fondo.setGeometry(-100, 0, 1024, 1024)  # Su posición
        self.fondo.setPixmap(QPixmap('Imagenes/fondo_inicio.jpeg'))  # Imagen de fondo

        # Donde se va a meter visualmente las demás etiquetas
        self.label_menu = QLabel(self.titulo,parent= self)  # Creamos una etiqueta
        self.label_menu.setGeometry(230, 140+175, 371, 460)  # Su posición
        self.label_menu.setAlignment(Qt.AlignHCenter | Qt.AlignTop)  # La alineación del texto respecto a la imagen de su label
        self.label_menu.setStyleSheet(
            "background-color: rgba(124, 90, 61, 0.25); border-width: 90px;  border-radius: 20px;"
        )  # Propiedades para que quede bonito
        self.label_menu.setFont(QFont('MS Sans Serif', 20))  # Fuente de la letra

        # Etiqueta de DNI
        self.dni_label = QLabel(text="DNI", parent=self)
        self.dni_label.setGeometry(280, 250+175, 231, 41)
        self.dni_label.setFont(QFont('MS Shell Dlg 2', 10))

        # Etiqueta de la contraseña
        self.password_label = QLabel("Contraseña", self)
        self.password_label.setGeometry(280, 350+175, 231, 41)
        self.password_label.setFont(QFont('MS Shell Dlg 2', 10))

        # Linea de error de parámetros que se mostrará cuando haya uno
        self.error_line = QLabel('Debes introducir bien los parámetros', self)
        self.error_line.setStyleSheet(
            "background-color: rgba(14, 146, 163, 0); color:red;font-weight: bold;"
        )
        self.error_line.setGeometry(250, 200+175, 400, 41)
        self.error_line.setFont(QFont('MS Shell Dlg 2', 10))
        self.error_line.hide()

        # ----------------Botones------------------#
        # Botón para la entrada al sistema
        self.enter_button = QPushButton("Entrar", self)
        self.enter_button.setGeometry(360, 480+175, 93, 28)
        self.enter_button.clicked.connect(self.verificar_usuario_log_in)  # Esto sirve para que hacer si se clica el botón

        # Botón si no tienes cuenta
        self.no_accounts_button = QPushButton("No tengo cuenta", self)
        self.no_accounts_button.setGeometry(350, 550+175, 110, 28)
        self.no_accounts_button.clicked.connect(self.pasar_a_registro)

        # ----------------Entradas de texto------------------#
        # Escribir tu DNI

        self.line_DNI = QLineEdit(self)
        self.line_DNI.setGeometry(280, 300+175, 231, 41)

        # Escribir contraseña
        self.line_password = QLineEdit(self)
        self.line_password.setGeometry(280, 420+175, 231, 41)

        # Si estamos en el registro
        if self.titulo == "Registro de usuario":
            # Cambiamos las posiciones para que quede bonito
            self.label_menu.setGeometry(230, 140+175, 371, 600)

            self.user_label = QLabel(text="Usuario", parent=self)
            self.user_label.setGeometry(280, 250+100, 231, 41)
            self.user_label.setFont(QFont('MS Shell Dlg 2', 10))

            self.line_username = QLineEdit(self)
            self.line_username.setGeometry(280, 300+100, 231, 30)

            self.error_line.setGeometry(250, 175, 400, 41)

            # Creamos nuevas etiquetas y entradas de texto
            self.apellido_label = QLabel("Apellidos", self)
            self.apellido_label.setGeometry(280, 350+100, 231, 41)
            self.apellido_label.setFont(QFont('MS Shell Dlg 2', 10))
            self.line_apellido = QLineEdit(self)
            self.line_apellido.setGeometry(280, 400+100, 231, 30)

            self.dni_label.setGeometry(280, 450+100, 231, 41)

            self.line_DNI.setGeometry(280, 500+100, 231, 30)

            self.password_label.setGeometry(280, 550+100, 231, 41)
            self.line_password.setGeometry(280, 600+100, 231, 30)

            self.enter_button.setGeometry(360, 650+100, 93, 28)
            self.no_accounts_button.setGeometry(350, 700+100, 110, 28)


            # Cambiamos a donde apunta el click del botón
            self.enter_button.clicked.connect(self.verificar_usuario_register)

    def pasar_a_registro(self):  # Para pasar la ventana de registrarse
        register.no_accounts_button.hide()
        register.show()
        self.hide()

    # Esto es para que no se metan nombres, apellidos, etc con valores como NULL o cosas así
    def verificar_usuario_log_in(self):
        if self.line_DNI.text() == '' or self.line_password.text() == '':
            self.error_line.show()
        else:
            # Si va bien manda los valores a la clase Usuario y ahí ya verá si ha iniciado correctamente
            DNI,contrasenya =self.line_DNI.text(), self.line_password.text()
            print(f'DNI: {DNI}\nContraseña: {contrasenya}')
            print(Usuario.login(DNI, contrasenya))
            if Usuario.login(DNI, contrasenya) is None or Usuario.login(DNI, contrasenya) is False:
                self.error_line.show()
            else:
                self.hide()
            # if not Usuario.login(DNI, contrasenya):
            #     self.error_line.show()
            # else:
            #     self.hide()

    def verificar_usuario_register(self): # Mira que los valores no sean NULL y si no manda los datos a Usuario
        if self.line_username.text() == '' or self.line_password.text() == '' or self.line_apellido.text() == '' or self.line_DNI == '':
            self.error_line.setText("Debes introducir bien los parámetros")
            self.error_line.show()
        else:
            nombre,contrasenya,apellidos,DNI =self.line_username.text(), self.line_password.text(),self.line_apellido.text(),self.line_DNI.text()
            print(f'Nombre: {nombre}\nApellidos: {apellidos}\nDNI: {DNI}\nContraseña: {contrasenya}')
            user = Usuario(DNI, nombre, apellidos, contrasenya)
            if user.guardar_en_bd():
                print("entro")

            else:
                print("no entro")
                self.error_line.setText("Usuario ya existente")
                self.error_line.show()
                self.show()



if __name__ == '__main__':
    app = QApplication([])
    log_in = MainApp("Iniciar sesion")
    register = MainApp("Registro de usuario")

    log_in.show()
    app.exec_()
