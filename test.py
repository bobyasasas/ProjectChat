from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QDialog


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 省略了布局和控件的创建代码...
        # 假设我们有一个登录按钮
        self.login_btn = QPushButton('登录', self)
        self.login_btn.clicked.connect(self.on_login)

        # 设置布局等...

    def on_login(self):
        if self.validate_credentials():  # 验证凭据...
            self.accept()  # 或者使用 self.close()
            self.open_main_window()

    def validate_credentials(self):
        # 验证逻辑...
        return True

    def open_main_window(self):
        main_window = MainWindow()
        main_window.show()


class MainWindow(QMainWindow):
    # ...（省略了其他代码）
    pass


app = QApplication([])
login_window = LoginWindow()
login_window.show()
app.exec()
