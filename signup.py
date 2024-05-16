import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget
from ui_signup import Ui_signUp_window


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_signUp_window()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()
