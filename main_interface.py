import json

import requests
from PySide6.QtCore import Slot, QStandardPaths, QThread, Signal
from PySide6.QtGui import QIcon, Qt, QBrush, QColor
from PySide6.QtWidgets import QFrame, QHBoxLayout, QWidget, QListWidgetItem, QFileDialog, QVBoxLayout
from plyer import notification
from qfluentwidgets import NavigationItemPosition, FluentWindow, SubtitleLabel, setFont, MessageBox, TeachingTip, \
    InfoBarIcon, TeachingTipTailPosition, PopupTeachingTip, BodyLabel, PrimaryPushButton, FlyoutViewBase
from qfluentwidgets import FluentIcon as FIF

import myUtil.Post
from dialog import CustomMessageBox
from file import FileUploadWindow
from func import Func
from messag import UIMessageWindow
from myUtil import Post
from plt import Plt
from ui_contacts import Ui_Contacts_Form
from ui_file import Ui_FILE


def add_contacts(add_name, username):
    json = {
        "username": username,
        "add_name": add_name
    }
    if Post.get_post("http://119.188.240.140:22255/chat/post/add_contacts", json):
        return True
    else:
        return False



    def paintEvent(self, e):
        pass


class Contacts(QWidget, Ui_Contacts_Form):
    def __init__(self, username):
        super().__init__()

        self.username = username
        self.setupUi(self)
        self.setObjectName("contracts")
        input_json = {
            "username": self.username
        }
        stands = json.loads(
            myUtil.Post.get_contracts("http://119.188.240.140:22255/chat/post/get_contacts", input_json))
        color = QColor(204, 229, 255, 64)
        for stand in stands:
            item = QListWidgetItem(stand)
            item.setIcon(QIcon(FIF.FEEDBACK.icon()))
            self.listWidget.addItem(item)
            item.setBackground(QBrush(color))
        self.listWidget.itemClicked.connect(self.onItemClicked)
        self.pushButton_add_contact.clicked.connect(self.showDialog_add_contact)
        self.pushButton_del_contact.clicked.connect(self.del_contacts)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setAlternatingRowColors(True)
        self.setStyleSheet("Contacts{background: rgb(249, 249, 249)} ")
        self.check = CheckThread(self.username)
        self.check.check_received.connect(self.check_update)
        self.check.start()

    def showBottomTip(self,usr):
        TeachingTip.create(
            target=self.listWidget,
            icon=InfoBarIcon.SUCCESS,
            title='new messages',
            content="You have new messages from:"+usr,
            isClosable=True,
            tailPosition=TeachingTipTailPosition.TOP,
            duration=10000,
            parent=self
        )

    def closeEvent(self, event):
        print("close...")
        self.check.terminate()  # 首先尝试终止线程
        self.check.wait()  # 等待线程安全退出
        event.accept()

    @Slot(QListWidgetItem)
    def onItemClicked(self, item: QListWidgetItem):
        color = QColor(204, 229, 255, 64)
        item.setBackground(QBrush(color))
        self.open_message_box(item.text())

    def check_update(self, new_message_name):
        names = " "
        for name in new_message_name:
            print(name[0])
            self.change_font_color(name[0])
            names = names + name[0] + " "
        self.showBottomTip(names)

    def change_font_color(self, match_text):
        # 遍历所有项
        color = QColor(102, 255, 102, 80)
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            if item.text() == match_text:
                item.setBackground(QBrush(color))

    def del_contacts(self):
        self.change_font_color("abby")

    def showDialog_add_contact(self):
        dialog = CustomMessageBox(self)
        if dialog.exec():
            if add_contacts(dialog.urlLineEdit.text(), self.username):
                MessageBox("添加成功", "添加好友成功", self).show()
                color = QColor(204, 229, 255, 64)
                item = QListWidgetItem(dialog.urlLineEdit.text())
                item.setIcon(QIcon(FIF.FEEDBACK.icon()))
                self.listWidget.addItem(item)
                item.setBackground(QBrush(color))
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


class CheckThread(QThread):
    check_received = Signal(list)

    def __init__(self, username):
        super().__init__()
        self.username = username

    def run(self):
        # 假设这个方法会周期性地检查新消息
        while True:
            # 这里使用 QThread.sleep 来暂停线程，避免无限循环过快执行
            QThread.sleep(10)
            input_json = {
                "username": self.username
            }
            # 假设 Post.get_contracts 是一个有效的网络请求
            new_message_name = Post.get_contracts("http://119.188.240.140:22255/chat/post/check_message", input_json)
            if new_message_name:
                self.check_received.emit(new_message_name)  # 发出信号传递消息
                print("Message received from:", new_message_name)  # 打印接收到的消息


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
            item.setIcon(FIF.DOCUMENT.icon())
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
            self.startDownload(self.saveFilePath, filename)  # 启动下载过程（示例中未实现）

    @Slot(FileListItem)
    def onItemClicked(self, item: FileListItem):
        self.chooseSaveLocation(item.filename)

    def startDownload(self, filePath, filename):
        # 这里可以添加实际的下载文件逻辑
        # 假设下载成功，可以给用户一个提示
        MessageBox("Download", f"File will be saved to: {filePath}", self).show()

        url = "http://119.188.240.140:22255/chat/download/" + filename
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

    def __init__(self, username):
        super().__init__()
        self.username = username

        # 创建子界面，实际使用时将 Widget 换成自己的子界面
        self.contactsInterface = Contacts(self.username)
        self.transmitInterface = File()
        self.analyzeInterface = Func()
        self.profileInterface = Plt()
        self.initNavigation()
        self.initWindow()

        # self.contactsInterface.pushButton_add_contact.clicked.connect()

    def setUsername(self, username):
        self.username = username

    def initNavigation(self):
        self.addSubInterface(self.contactsInterface, FIF.PEOPLE, 'Contacts')
        self.addSubInterface(self.transmitInterface, FIF.SEND_FILL, 'Transmit file')
        self.addSubInterface(self.analyzeInterface, FIF.UPDATE, 'Analyze')
        self.addSubInterface(self.profileInterface, FIF.CLOUD, 'Manage', NavigationItemPosition.BOTTOM)

    def initWindow(self):
        self.resize(900, 600)
        self.setWindowIcon(QIcon(FIF.HOME_FILL.icon()))
        self.setWindowTitle('Kchat')
