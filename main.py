from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from login import LoginWindow
from main_interface import MainInterface
from signin import SigninWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stackedWidget = QStackedWidget()

        self.login_interface = LoginWindow()
        self.login_interface.pushButton_signin.clicked.connect(self.on_go_to_sign_interface)

        self.sign_interface = SigninWindow()
        self.sign_interface.pushButton_login.clicked.connect(self.on_go_to_login_interface)

        self.stackedWidget.addWidget(self.sign_interface)
        self.stackedWidget.addWidget(self.login_interface)

        self.setCentralWidget(self.stackedWidget)
        self.resize(396, 501)
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('Kchat')

    def on_go_to_login_interface(self):
        self.stackedWidget.setCurrentIndex(1)

    def on_go_to_sign_interface(self):
        self.stackedWidget.setCurrentIndex(0)

    def login_success(self):
        main = MainInterface()
        main.show()



app = QApplication([])
window = MainWindow()
window.show()
app.exec()
