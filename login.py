import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget
from ui_login import Ui_login_window


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login_window()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()
