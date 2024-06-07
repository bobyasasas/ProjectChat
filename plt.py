import sys

from PySide6.QtCore import QThread
from PySide6.QtWidgets import QWidget, QApplication

from test import Graph
from ui_plt import Ui_Plot


class Plt(QWidget, Ui_Plot):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_user.clicked.connect(self,self.open_user)

    def open_user(self):
        window = Graph()
        window.show()


class UserThread(QThread):

    def __init__(self):
        super().__init__()

    def run(self):
        window = Graph()
        window.show()


