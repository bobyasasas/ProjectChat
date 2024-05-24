import sys

from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QApplication, QWidget, QListWidgetItem
from qfluentwidgets import NavigationItemPosition, FluentWindow, SubtitleLabel, setFont
from qfluentwidgets import FluentIcon as FIF

from dialog import CustomMessageBox
from ui_contacts import Ui_Contacts_Form


class Contacts(QWidget, Ui_Contacts_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setObjectName("contracts")
        stands = [
            'kai', 'wyx', 'zzw', 'czy', 'yjy', 'zlr'
        ]
        for stand in stands:
            item = QListWidgetItem(stand)
            item.setIcon(QIcon(':/qfluentwidgets/images/logo.png'))
            self.listWidget.addItem(item)
        self.pushButton_add_contact.clicked.connect(self.showDialog_add_contact)

    def showDialog_add_contact(self):
        dialog = CustomMessageBox(self)
        if dialog.exec():
            print(dialog.urlLineEdit.text())


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignmentFlag.AlignCenter)

        # 必须给子界面设置全局唯一的对象名
        self.setObjectName(text.replace(' ', '-'))


class MainInterface(FluentWindow):
    """ 主界面 """

    def __init__(self):
        super().__init__()

        # 创建子界面，实际使用时将 Widget 换成自己的子界面
        self.contactsInterface = Contacts()
        self.chatInterface = Widget('chat Interface', self)
        self.transmitInterface = Widget('transmit Interface', self)
        self.analyzeInterface = Widget('analyze Interface', self)
        self.profileInterface = Widget('profile Interface', self)

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.contactsInterface, FIF.PEOPLE, 'Contacts')
        self.addSubInterface(self.chatInterface, FIF.CHAT, 'Chat')
        self.addSubInterface(self.transmitInterface, FIF.SEND_FILL, 'Transmit file')
        self.addSubInterface(self.analyzeInterface, FIF.UPDATE, 'Analyze')
        self.addSubInterface(self.profileInterface, FIF.VIEW, 'Profile', NavigationItemPosition.BOTTOM)

    def initWindow(self):
        self.resize(900, 600)
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('Kchat')


if __name__ == ('__mai'
                'n__'):
    app = QApplication(sys.argv)
    w = MainInterface()
    w.show()
    app.exec()
