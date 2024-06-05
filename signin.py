import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget
from qfluentwidgets import MessageBox

from ui_signin import Ui_signin_window


class SigninWindow(QWidget, Ui_signin_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_forget.clicked.connect(self.forget_passwd)

    def forget_passwd(self):
        MessageBox("重置密码", "请联系管理员重置密码", self).show()

