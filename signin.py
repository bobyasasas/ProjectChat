import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget
from qfluentwidgets import MessageBox

import myUtil.Post
from ui_signin import Ui_signin_window


class MyWindow(QWidget, Ui_signin_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_signin.clicked.connect(self.signin)

    def signin(self):
        username = self.lineEdit_username.text()
        passwd = self.lineEdit_passwd.text()
        json = {
            'username': username,
            'passwd': passwd
        }
        if myUtil.Post.get_post("http://127.0.0.1:8080/chat/post/signin", json):
            MessageBox("登录成功", "欢迎登录，" + username, self).show()
        else:
            MessageBox("登录失败", "用户名或者密码错误。", self).show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()
