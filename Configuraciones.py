from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
import sys

class MiVentana(QMainWindow):
    def __init__(self):
        super(MiVentana,self).__init__()
        self.setGeometry(0, 0, 1900, 970)
        self.setWindowTitle('Menu casino')
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('Casino')
        self.label.move(900, 300)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Ruleta')
        self.b1.move(500, 600)
        self.b1.clicked.connect(self.clicado)

    def clicado(self):
        self.label.setText('Clicado')
        self.update()


    def update(self):
        self.label.adjustSize()



def ventana():
    app = QApplication(sys.argv)
    win = MiVentana()

    win.show()
    sys.exit(app.exec_())


ventana()
