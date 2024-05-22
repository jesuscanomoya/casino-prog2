import sys
from PyQt5 import QtCore, QtWidgets
from menu import Ui_MainWindow
from main2 import Tragaperras, Blackjack  # Asegúrate de que este import sea correcto
import pygame


class MiApp(QtWidgets.QMainWindow):
    def __init__(self,jugador):
        super().__init__()
        self.jugador = jugador
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Eliminar barra y de título - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Mover ventana
        self.ui.barra_superior.mouseMoveEvent = self.mover_ventana

        # Acceder a las páginas
        self.ui.bt_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.bt_uno.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_uno))
        self.ui.bt_dos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_dos))
        self.ui.bt_tres.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_tres))


        # Control barra de títulos
        self.ui.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.ui.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.ui.bt_maximizar.clicked.connect(self.control_bt_maximizar)
        self.ui.bt_cerrar.clicked.connect(self.close)


        # Menú lateral
        self.ui.bt_menu.clicked.connect(self.mover_menu)

        # Conectar botones de juego
        self.ui.pushButton_5.clicked.connect(self.accion_jugar_tragaperras)
        self.ui.pushButton_4.clicked.connect(self.accion_jugar_blackjack)
        self.ui.pushButton_3.clicked.connect(self.ingresar_dinero)

        self.tragaperras = None  # Inicializa la instancia de Tragaperras
        self.blackjack = None

    def control_bt_minimizar(self):
        self.showMinimized()

    def control_bt_normal(self):
        self.showNormal()
        self.ui.bt_restaurar.hide()
        self.ui.bt_maximizar.show()

    def control_bt_maximizar(self):
        self.showMaximized()
        self.ui.bt_maximizar.hide()
        self.ui.bt_restaurar.show()

    def mover_menu(self):
        width = self.ui.barra_lateral.width()
        normal = 0
        extender = 200 if width == 0 else normal

        self.animacion = QtCore.QPropertyAnimation(self.ui.barra_lateral, b'minimumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()

    def accion_jugar_tragaperras(self):
        if self.tragaperras is None:
            self.tragaperras = Tragaperras(self.jugador)
        try:
            self.tragaperras.inicio_tragaperras()
        except pygame.error:
            self.tragaperras = Tragaperras(self.jugador)
            self.tragaperras.inicio_tragaperras()

    def accion_jugar_blackjack(self):
        if self.blackjack is None:
            self.blackjack = Blackjack(self.jugador)
        try:
            self.blackjack.inicio_blackjack()
        except pygame.error:
            self.blackjack = Blackjack(self.jugador)
            self.blackjack.inicio_blackjack()

    def ingresar_dinero(self):
        self.jugador.balance += 10

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        if not self.isMaximized():
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <= 20:
            self.showMaximized()
        else:
            self.showNormal()

