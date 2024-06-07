import os
import sys
from PySide6.QtGui import QIcon, QCloseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from qfluentwidgets import MessageBox
import myUtil.Post
from login import LoginWindow
from main_interface import MainInterface
from signin import SigninWindow


class Main(MainInterface):
    def __init__(self, main_father, username):
        super().__init__(username)
        self.main_father = main_father

    def closeEvent(self, event: QCloseEvent) -> None:
        self.main_father.close()
        sys.exit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stackedWidget = QStackedWidget()

        self.login_interface = LoginWindow()
        self.login_interface.pushButton_signin.clicked.connect(self.on_go_to_sign_interface)

        self.sign_interface = SigninWindow()
        self.sign_interface.pushButton_signin.clicked.connect(self.signin)
        self.sign_interface.pushButton_login.clicked.connect(self.on_go_to_login_interface)

        self.stackedWidget.addWidget(self.sign_interface)
        self.stackedWidget.addWidget(self.login_interface)

        self.setCentralWidget(self.stackedWidget)
        self.resize(396, 501)
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('Kchat')
        self.sign_interface.lineEdit_passwd.returnPressed.connect(self.signin)

    def on_go_to_login_interface(self):
        self.stackedWidget.setCurrentIndex(1)

    def on_go_to_sign_interface(self):
        self.stackedWidget.setCurrentIndex(0)

    def login_success(self, username):
        self.resize(0, 0)
        self.stackedWidget.close()
        main = Main(self, username)
        main.show()

    def signin(self):
        username = self.sign_interface.lineEdit_username.text()
        passwd = self.sign_interface.lineEdit_passwd.text()
        json = {
            'username': username,
            'passwd': passwd

        }
        if myUtil.Post.get_post("http://119.188.240.140:22255/chat/post/signin", json):
            MessageBox("登录成功", "欢迎登录，" + username, self).show()
            self.login_success(username)
        else:
            MessageBox("登录失败", "用户名或者密码错误。", self).show()


config_path = os.getenv("LOCALAPPDATA")
config_path = config_path + "\k-chat\\"
print(config_path)
if not os.path.exists(config_path):
    os.makedirs(config_path)
    print("config path created")
app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
