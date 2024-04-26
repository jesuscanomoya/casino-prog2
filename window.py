import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MainApp, self).__init__(parent=parent)
        self.setWindowTitle('Casino')
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setMinimumSize(800, 600)
        self.isFullScreen()



app = QApplication([])
window = MainApp()
window.show()
app.exec_()
