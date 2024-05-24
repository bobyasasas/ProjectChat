from PySide6.QtWidgets import QWidget
from qfluentwidgets import MessageBox
import myUtil.Post
from ui_login import Ui_login_window


class LoginWindow(QWidget, Ui_login_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_login.clicked.connect(self.login)

    def login(self):
        username = self.lineEdit_username.text()
        passwd = self.lineEdit_passwd.text()
        passwd_confirm = self.lineEdit_passwd_confirm.text()
        if passwd_confirm != passwd:
            MessageBox("注册失败", "两次密码不一致！", self).show()
        else:
            json = {
                'username': username,
                'passwd': passwd
            }
            if myUtil.Post.get_post("http://127.0.0.1:8080/chat/post/login", json):
                MessageBox("注册成功", "欢迎注册，" + username, self).show()
                return True, username
            else:
                MessageBox("注册失败", "该用户已注册", self).show()
                return False,username
