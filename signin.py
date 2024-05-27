import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget
from qfluentwidgets import MessageBox

import myUtil.Post
from ui_signin import Ui_signin_window


class SigninWindow(QWidget, Ui_signin_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_forget.clicked.connect(self.forget_passwd)

    def forget_passwd(self):
        MessageBox("重置密码", "请联系管理员重置密码", self).show()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SigninWindow()
    window.show()
    app.exec()
