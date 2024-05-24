import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget
from qfluentwidgets import MessageBox

import myUtil.Post
from login import LoginWindow
from ui_signin import Ui_signin_window


class SigninWindow(QWidget, Ui_signin_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_signin.clicked.connect(self.signin)
        self.pushButton_forget.clicked.connect(self.forget_passwd)

    def forget_passwd(self):
        MessageBox("重置密码", "请联系管理员重置密码", self).show()

    def signin(self):
        username = self.lineEdit_username.text()
        passwd = self.lineEdit_passwd.text()
        json = {
            'username': username,
            'passwd': passwd
        }
        if myUtil.Post.get_post("http://127.0.0.1:8080/chat/post/signin", json):
            MessageBox("登录成功", "欢迎登录，" + username, self).show()
            return True, username
        else:
            MessageBox("登录失败", "用户名或者密码错误。", self).show()
            return False, username


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SigninWindow()
    window.show()
    app.exec()
