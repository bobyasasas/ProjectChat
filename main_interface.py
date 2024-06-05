import json

import requests
from PySide6.QtCore import Slot, QStandardPaths
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QWidget, QListWidgetItem, QFileDialog
from qfluentwidgets import NavigationItemPosition, FluentWindow, SubtitleLabel, setFont, MessageBox
from qfluentwidgets import FluentIcon as FIF

import myUtil.Post
from dialog import CustomMessageBox
from file import FileUploadWindow
from messag import UIMessageWindow
from myUtil import Post
from ui_contacts import Ui_Contacts_Form
from ui_file import Ui_FILE


def add_contacts(add_name,username):
    json = {
        "username": username,
        "add_name": add_name
    }
    if Post.get_post("http://119.188.240.140:22255/chat/post/add_contacts", json):
        return True
    else:
        return False


class Contacts(QWidget, Ui_Contacts_Form):
    def __init__(self,username):
        super().__init__()

        self.username = username
        self.setupUi(self)
        self.setObjectName("contracts")
        input_json = {
            "username": self.username
        }
        stands = json.loads(myUtil.Post.get_contracts("http://119.188.240.140:22255/chat/post/get_contacts", input_json))
        for stand in stands:
            item = QListWidgetItem(stand)
            item.setIcon(QIcon(':/qfluentwidgets/images/logo.png'))
            self.listWidget.addItem(item)
        self.listWidget.itemClicked.connect(self.onItemClicked)
        self.pushButton_add_contact.clicked.connect(self.showDialog_add_contact)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setAlternatingRowColors(True)
        self.setStyleSheet("Contacts{background: rgb(249, 249, 249)} ")

    @Slot(QListWidgetItem)
    def onItemClicked(self, item: QListWidgetItem):
        self.open_message_box(item.text())

    def showDialog_add_contact(self):
        dialog = CustomMessageBox(self)
        if dialog.exec():
            if add_contacts(dialog.urlLineEdit.text(),self.username):
                MessageBox("添加成功", "添加好友成功", self).show()
                item = QListWidgetItem(dialog.urlLineEdit.text())
                item.setIcon(QIcon(':/qfluentwidgets/images/logo.png'))
                self.listWidget.addItem(item)
            else:
                MessageBox("添加失败", "添加好友失败,已添加或用户不存在", self).show()

    def open_message_box(self, contact_name):
        self.message_box = UIMessageWindow(self.username, contact_name)
        self.message_box.show()


class FileListItem(QListWidgetItem):
    def __init__(self, filename, filesize):
        super().__init__()
        self.filename = filename
        self.filesize = filesize


class File(QWidget, Ui_FILE):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setObjectName("file")
        self.flush()
        self.listWidget.itemClicked.connect(self.onItemClicked)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setAlternatingRowColors(True)
        self.setStyleSheet("Contacts{background: rgb(249, 249, 249)} ")
        self.pushButton_flush.clicked.connect(self.flush)
        self.pushButton_upload.clicked.connect(self.open_upload)
        self.upload = FileUploadWindow()

    def open_upload(self):
        self.upload.show()

    def flush(self):
        self.listWidget.clear()
        stands = myUtil.Post.get_filenames("http://119.188.240.140:22255/chat/post/get_files")
        for stand in stands:
            item = FileListItem(stand[0], stand[1])
            text = item.filename + "      " + item.filesize
            item.setText(text)
            item.setIcon(QIcon(':/qfluentwidgets/images/logo.png'))
            self.listWidget.addItem(item)

    def chooseSaveLocation(self, filename):
        # 设置默认的下载路径（例如用户的下载目录）
        default_path = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)

        # 弹出对话框让用户选择保存文件的位置和文件名
        # 如果用户没有选择文件名，则默认文件名为 "default_filename.txt"
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File",
                                                  default_path + "/" + filename,
                                                  "All Files (*)",
                                                  options=options)
        if fileName:  # 如果用户指定了文件名
            self.saveFilePath = fileName  # 存储文件路径
            self.startDownload(self.saveFilePath,filename)  # 启动下载过程（示例中未实现）

    @Slot(FileListItem)
    def onItemClicked(self, item: FileListItem):
        self.chooseSaveLocation(item.filename)

    def startDownload(self, filePath,filename):
        # 这里可以添加实际的下载文件逻辑
        # 假设下载成功，可以给用户一个提示
        MessageBox("Download", f"File will be saved to: {filePath}", self).show()

        url = "http://119.188.240.140:22255/chat/download/"+filename
        response = requests.get(url, stream=True)

        # 检查请求是否成功
        if response.status_code == 200:
            # 获取文件名
            # 打开文件进行写入
            with open(filePath, 'wb') as file:
                # 写入文件
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"文件已下载为: {filePath}")
        else:
            print(f"下载失败，状态码：{response.status_code}")

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

    def __init__(self,username):
        super().__init__()
        self.username = username

        # 创建子界面，实际使用时将 Widget 换成自己的子界面
        self.contactsInterface = Contacts(self.username)
        self.transmitInterface = File()
        self.analyzeInterface = Widget('analyze Interface', self)
        self.profileInterface = Widget('profile Interface', self)
        self.initNavigation()
        self.initWindow()

        # self.contactsInterface.pushButton_add_contact.clicked.connect()
    def setUsername(self,username):
        self.username = username

    def initNavigation(self):
        self.addSubInterface(self.contactsInterface, FIF.PEOPLE, 'Contacts')
        self.addSubInterface(self.transmitInterface, FIF.SEND_FILL, 'Transmit file')
        self.addSubInterface(self.analyzeInterface, FIF.UPDATE, 'Analyze')
        self.addSubInterface(self.profileInterface, FIF.VIEW, 'Profile', NavigationItemPosition.BOTTOM)

    def initWindow(self):
        self.resize(900, 600)
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('Kchat')
