import os


from PySide6.QtWidgets import QWidget

from ui_plt import Ui_Plot


def open_user():
    os.system('start ./user.exe')


def open_messages():
    os.system('start ./message.exe')


class Plt(QWidget, Ui_Plot):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_user.clicked.connect(self, open_user)
        self.pushButton_message.clicked.connect(self, open_messages)
