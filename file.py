import os
import sys

import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLineEdit, \
    QFileDialog
from qfluentwidgets import LineEdit, PushButton, TextEdit, MessageBox


class FileUploadWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("File Upload")
        self.setGeometry(600, 200, 300, 400)  # x, y, width, height

        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建一个文本编辑框用于显示选中的文件路径
        self.filePathDisplay = LineEdit(self)
        self.filePathDisplay.setReadOnly(True)
        layout.addWidget(self.filePathDisplay)

        # 创建一个按钮用于打开文件选择对话框
        self.uploadButton = PushButton("Choose File", self)
        self.uploadButton.clicked.connect(self.chooseFile)
        layout.addWidget(self.uploadButton)
        self.sendButton = PushButton("Send File", self)
        self.sendButton.clicked.connect(self.sendFile)
        layout.addWidget(self.sendButton)
        # 创建一个文本框作为额外的界面元素，可以用于显示状态消息
        self.statusTextEdit = TextEdit(self)
        self.statusTextEdit.setReadOnly(True)
        layout.addWidget(self.statusTextEdit)

        # 创建一个容器widget
        widget = QWidget()
        widget.setLayout(layout)

        # 设置中央小部件
        self.setCentralWidget(widget)

    def chooseFile(self):
        # 打开文件选择对话框并获取用户选择的文件路径
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Choose File", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            # 在文本编辑框中显示选中的文件路径
            self.filePathDisplay.setText(fileName)
            self.statusTextEdit.clear()
            # 这里可以添加代码来处理文件上传的逻辑
            # 例如: self.uploadFile(fileName)
            self.statusTextEdit.append("File selected: " + fileName)

    def sendFile(self,filename):
        BASE_URL = 'http://119.188.240.140:22255'  # 假设 Flask 服务器运行在本地的 5000 端口
        UPLOAD_ENDPOINT = '/chat/post/upload'

        # 设置文件路径
        file_path = self.filePathDisplay.text()  # 替换为要上传的文件的实际路径

        # 确保文件存在
        if not os.path.isfile(file_path):
            print("Error: File does not exist.")
            MessageBox("error", "file not exist", self).show()
            exit(1)

        # 打开文件并准备文件上传
        file = {'file': open(file_path, 'rb')}
        self.statusTextEdit.append("uploading..... please wait")

        # 发送 POST 请求上传文件
        response = requests.post(BASE_URL + UPLOAD_ENDPOINT, files=file)

        # 关闭文件，避免资源泄露
        file['file'].close()

        # 检查服务器响应
        if response.ok:
            response_json = response.json()
            if response_json.get('msg') == 'true':
                print("File uploaded successfully.")
                MessageBox("upload successfully", "upload successfully", self).show()
                self.statusTextEdit.clear()
                self.filePathDisplay.clear()
            else:
                print("Error:", response_json.get('msg'))
                MessageBox("error", "unknown error", self).show()
        else:
            MessageBox("error", "unknown error", self).show()

        # 打印服务器的响应文本
        print("Server response:", response.text)


