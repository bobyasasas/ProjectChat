import sys

from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import QUrl

from ui_func import Ui_Form_func


def openWebPage():
    # 定义要打开的 URL
    url = QUrl("https://www.example.com")
    # 使用 QDesktopServices 打开网页
    QDesktopServices.openUrl(url)


class Func(QMainWindow, Ui_Form_func):
    def __init__(self):
        super().__init__()
        self.openWebPageButton = None
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_flume)
        self.pushButton_3.clicked.connect(self.open_sqoop)
        self.pushButton_2.clicked.connect(self.backup)

    def open_flume(self):
        url = QUrl("http://119.188.240.140:51170/explorer.html#/kchat/messages")
        QDesktopServices.openUrl(url)

    def open_sqoop(self):
        url = QUrl("https://www.example.com")
        QDesktopServices.openUrl(url)

    def backup(self):
        pass


if __name__ == "__main__":
    app = QApplication([])
    window = Func()
    window.show()
    sys.exit(app.exec())
