
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(756, 461)
        MainWindow.setMinimumSize(QtCore.QSize(400, 0))
        MainWindow.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.barra_superior = QtWidgets.QFrame(self.centralwidget)
        self.barra_superior.setMinimumSize(QtCore.QSize(0, 35))
        self.barra_superior.setMaximumSize(QtCore.QSize(16777215, 50))
        self.barra_superior.setStyleSheet("\n"
                                          "QFrame{\n"
                                          "border-top-left-radius: 20px;\n"
                                          "border-bottom-left-radius: 20px;\n"
                                          "\n"
                                          "background-color: rgb(160, 0, 0);\n"
                                          "\n"
                                          "}\n"
                                          "")
        self.barra_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_superior.setObjectName("barra_superior")

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.barra_superior)
        self.horizontalLayout_8.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.bt_menu = QtWidgets.QPushButton(self.barra_superior)
        self.bt_menu.setMinimumSize(QtCore.QSize(200, 0))
        self.bt_menu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.bt_menu.setStyleSheet("QPushButton{\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "font: 87 12pt \"Arial Black\";\n"
                                   "border-radius:0px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover{\n"
                                   "background-color: White;\n"
                                   "font: 87 12pt \"Arial Black\";\n"
                                   "\n"
                                   "}\n"
                                   "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("barra-de-menus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QtCore.QSize(32, 32))
        self.bt_menu.setAutoDefault(False)
        self.bt_menu.setDefault(False)
        self.bt_menu.setFlat(False)
        self.bt_menu.setObjectName("bt_menu")

        self.horizontalLayout_8.addWidget(self.bt_menu, 0, QtCore.Qt.AlignLeft)
        spacerItem = QtWidgets.QSpacerItem(265, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)

        self.bt_minimizar = QtWidgets.QPushButton(self.barra_superior)
        self.bt_minimizar.setMinimumSize(QtCore.QSize(35, 35))
        self.bt_minimizar.setStyleSheet("QPushButton{\n"
                                        "border:0px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "border:5px solid #aa00ff;\n"
                                        "background-color:#ffff00;\n"
                                        "\n"
                                        "}\n"
                                        "")
        self.bt_minimizar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("minimizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_minimizar.setIcon(icon1)
        self.bt_minimizar.setIconSize(QtCore.QSize(32, 32))
        self.bt_minimizar.setFlat(False)
        self.bt_minimizar.setObjectName("bt_minimizar")
        self.horizontalLayout_8.addWidget(self.bt_minimizar, 0, QtCore.Qt.AlignRight)

        self.bt_restaurar = QtWidgets.QPushButton(self.barra_superior)
        self.bt_restaurar.setMaximumSize(QtCore.QSize(35, 35))
        self.bt_restaurar.setStyleSheet("QPushButton{\n"
                                        "border:0px;\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "border:5px solid #aa00ff;\n"
                                        "background-color:#55ff00;\n"
                                        "\n"
                                        "}\n"
                                        "")
        self.bt_restaurar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("restaurar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_restaurar.setIcon(icon2)
        self.bt_restaurar.setIconSize(QtCore.QSize(30, 30))
        self.bt_restaurar.setObjectName("bt_restaurar")
        self.horizontalLayout_8.addWidget(self.bt_restaurar, 0, QtCore.Qt.AlignRight)
        self.bt_maximizar = QtWidgets.QPushButton(self.barra_superior)
        self.bt_maximizar.setStyleSheet("QPushButton{\n"
                                        "border:0px;\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "border:5px solid #aa00ff;\n"
                                        "background-color:#55ff00;\n"
                                        "\n"
                                        "}\n"
                                        "")
        self.bt_maximizar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("maximizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_maximizar.setIcon(icon3)
        self.bt_maximizar.setIconSize(QtCore.QSize(32, 32))
        self.bt_maximizar.setObjectName("bt_maximizar")
        self.horizontalLayout_8.addWidget(self.bt_maximizar, 0, QtCore.Qt.AlignRight)
        self.bt_cerrar = QtWidgets.QPushButton(self.barra_superior)
        self.bt_cerrar.setMaximumSize(QtCore.QSize(35, 16777215))
        self.bt_cerrar.setStyleSheet("QPushButton{\n"
                                     "border:0px;\n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "border:5px solid #aa00ff;\n"
                                     "background-color:red;\n"
                                     "\n"
                                     "}\n"
                                     "")
        self.bt_cerrar.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("cerrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cerrar.setIcon(icon4)
        self.bt_cerrar.setIconSize(QtCore.QSize(32, 32))
        self.bt_cerrar.setObjectName("bt_cerrar")
        self.horizontalLayout_8.addWidget(self.bt_cerrar, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.barra_superior)
        self.frame_inferior = QtWidgets.QFrame(self.centralwidget)
        self.frame_inferior.setStyleSheet("")
        self.frame_inferior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inferior.setObjectName("frame_inferior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.barra_lateral = QtWidgets.QFrame(self.frame_inferior)
        self.barra_lateral.setMinimumSize(QtCore.QSize(200, 0))
        self.barra_lateral.setMaximumSize(QtCore.QSize(0, 16777215))
        self.barra_lateral.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.barra_lateral.setAutoFillBackground(False)
        self.barra_lateral.setStyleSheet("\n"
                                         "QFrame{\n"
                                         "background-color:rgb(160, 0, 0)\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "QPushButton{\n"
                                         "background-color: rgb(225, 0, 0);\n"
                                         "border-top-left-radius: 20px;\n"
                                         "border-bottom-left-radius: 20px;\n"
                                         "\n"
                                         "font: 75 12pt \"Arial Narrow\";\n"
                                         "    \n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "background-color: white;\n"
                                         "border-top-left-radius: 20px;\n"
                                         "border-bottom-left-radius: 20px;\n"
                                         "\n"
                                         "font: 75 12pt \"Arial Narrow\";\n"
                                         "}")
        self.barra_lateral.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_lateral.setFrameShadow(QtWidgets.QFrame.Plain)
        self.barra_lateral.setObjectName("barra_lateral")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.barra_lateral)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 9)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bt_inicio = QtWidgets.QPushButton(self.barra_lateral)
        self.bt_inicio.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_inicio.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.bt_inicio.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("inteligencia-artificial.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_inicio.setIcon(icon5)
        self.bt_inicio.setIconSize(QtCore.QSize(32, 32))
        self.bt_inicio.setObjectName("bt_inicio")
        self.verticalLayout_2.addWidget(self.bt_inicio)
        self.bt_uno = QtWidgets.QPushButton(self.barra_lateral)
        self.bt_uno.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_uno.setToolTipDuration(0)
        self.bt_uno.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("base-de-datos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_uno.setIcon(icon6)
        self.bt_uno.setIconSize(QtCore.QSize(32, 32))
        self.bt_uno.setObjectName("bt_uno")
        self.verticalLayout_2.addWidget(self.bt_uno)
        self.bt_dos = QtWidgets.QPushButton(self.barra_lateral)
        self.bt_dos.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_dos.setStyleSheet("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("chip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_dos.setIcon(icon7)
        self.bt_dos.setIconSize(QtCore.QSize(32, 32))
        self.bt_dos.setObjectName("bt_dos")
        self.verticalLayout_2.addWidget(self.bt_dos)
        self.bt_tres = QtWidgets.QPushButton(self.barra_lateral)
        self.bt_tres.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_tres.setStyleSheet("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("moto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_tres.setIcon(icon8)
        self.bt_tres.setIconSize(QtCore.QSize(32, 32))
        self.bt_tres.setObjectName("bt_tres")
        self.verticalLayout_2.addWidget(self.bt_tres)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.barra_lateral)
        self.label_2.setStyleSheet("font: italic 15pt \"Vivaldi\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.barra_lateral, 0, QtCore.Qt.AlignLeft)
        self.frame_contenedor = QtWidgets.QFrame(self.frame_inferior)
        self.frame_contenedor.setStyleSheet("")
        self.frame_contenedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contenedor.setLineWidth(1)
        self.frame_contenedor.setObjectName("frame_contenedor")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_contenedor)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_contenedor)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")

        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        self.label = QtWidgets.QLabel(self.page)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logocasino.jpg"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.stackedWidget.addWidget(self.page)

        self.page_uno = QtWidgets.QWidget()
        self.page_uno.setObjectName("page_uno")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_uno)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.label_2 = QtWidgets.QLabel(self.page_uno)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Tragaperras/descripcion_tragaperras.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.stackedWidget.addWidget(self.page_uno)

        self.pushButton_5 = QtWidgets.QPushButton(self.page_uno)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 600, 956, 400))
        self.pushButton_5.setStyleSheet("background-color: rgb(0, 220, 0);\n"
                                        "font: 87 36pt \"Arial Black\";")
        self.pushButton_5.setObjectName("pushButton_5")

        self.stackedWidget.addWidget(self.page_uno)
        self.verticalLayout_4.addWidget(self.pushButton_5)

        self.page_dos = QtWidgets.QWidget()
        self.page_dos.setObjectName("page_dos")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_dos)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.label_3 = QtWidgets.QLabel(self.page_dos)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Tragaperras/descripcion_blackjack.png"))
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.stackedWidget.addWidget(self.page_dos)

        self.pushButton_4 = QtWidgets.QPushButton(self.page_dos)
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 220, 0);\n"
                                        "font: 87 36pt \"Arial Black\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_5.addWidget(self.pushButton_4)
        self.stackedWidget.addWidget(self.page_dos)

        self.page_tres = QtWidgets.QWidget()
        self.page_tres.setObjectName("page_tres")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_tres)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.label_4 = QtWidgets.QLabel(self.page_dos)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Imagenes/hist_bal.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.stackedWidget.addWidget(self.page_tres)

        self.pushButton_3 = QtWidgets.QPushButton(self.page_tres)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 220, 0);\n"
                                        "font: 87 36pt \"Arial Black\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_6.addWidget(self.pushButton_3)
        self.stackedWidget.addWidget(self.page_tres)

        self.page_cuatro = QtWidgets.QWidget()
        self.page_cuatro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_cuatro.setObjectName("page_cuatro")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_cuatro)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_cuatro)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 255, 0);\n"
                                        "font: 87 36pt \"Arial Black\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_7.addWidget(self.pushButton_2)
        self.stackedWidget.addWidget(self.page_cuatro)
        self.page_cinco = QtWidgets.QWidget()
        self.page_cinco.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_cinco.setObjectName("page_cinco")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_cinco)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton = QtWidgets.QPushButton(self.page_cinco)
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                      "font: 87 36pt \"Arial Black\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_8.addWidget(self.pushButton)
        self.stackedWidget.addWidget(self.page_cinco)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.frame_contenedor)
        self.verticalLayout.addWidget(self.frame_inferior)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_menu.setText(_translate("MainWindow", "     MENU "))
        self.bt_inicio.setText(_translate("MainWindow", "       INICIO             "))
        self.bt_uno.setText(_translate("MainWindow", "   TRAGAPERRAS"))
        self.bt_dos.setText(_translate("MainWindow", "    BLACKJACK"))
        self.bt_tres.setText(_translate("MainWindow", "    PERFIL"))
        self.pushButton_5.setText(_translate("MainWindow", "JUGAR"))
        self.pushButton_4.setText(_translate("MainWindow", "JUGAR"))
        self.pushButton_3.setText(_translate("MainWindow", "INGRESAR +10"))

    if __name__ == "__main__":
        import sys

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
