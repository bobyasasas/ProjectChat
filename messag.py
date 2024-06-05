import json
import sys
from time import sleep

import websockets

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout

from chat import ChatWindow, ChatBubble
from myUtil import Post
from ui_messages import Ui_Form_message

IP_ADDR = "119.188.240.140"
IP_PORT = "8888"


async def clientHands(websocket):
    while True:
        await websocket.send("hello")
        response_str = await websocket.recv()
        if "123" in response_str:
            print("握手成功")
            return True


async def clientSend(websocket):
    while True:
        input_text = input("input text: ")
        if input_text == "exit":
            print(f'"exit", bye!')
            await websocket.close(reason="exit")
            return False
        await websocket.send(input_text)
        recv_text = await websocket.recv()
        print(f"{recv_text}")


async def clientRun():
    ipaddress = IP_ADDR + ":" + IP_PORT
    async with websockets.connect("ws://" + ipaddress) as websocket:
        await clientHands(websocket)
        await clientSend(websocket)


class SocketThread(QThread):
    message_received = Signal(list)

    def __init__(self, username, contact):
        super().__init__()
        self.username = username
        self.contact = contact

    def run(self):
        # 假设这个方法会周期性地检查新消息
        while True:
            # 这里使用 QThread.sleep 来暂停线程，避免无限循环过快执行
            QThread.sleep(4)
            input_json = {
                "username": self.contact,
                "contact_name": self.username
            }
            # 假设 Post.get_contracts 是一个有效的网络请求
            message = Post.get_contracts("http://119.188.240.140:22255/chat/post/get_message", input_json)
            if message:
                self.message_received.emit(message)  # 发出信号传递消息
                print("Message received:", message)  # 打印接收到的消息


class UIMessageWindow(QWidget, Ui_Form_message):
    def __init__(self, username, contact):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.contact = contact
        self.label.setText(contact)
        self.socket = SocketThread(self.username, self.contact)
        # 连接信号到槽函数，确保 recv_message 能够接收字符串参数
        self.socket.message_received.connect(self.recv_message)
        self.socket.start()
        # 假设 self.pushButton_send 和 self.plainTextEdit 是通过 setupUi 正确设置的
        self.pushButton_send.clicked.connect(self.send_message)
        self.chat_layout = QVBoxLayout()

        # 将滚动区域的布局设置为垂直
        self.chat_layout.setContentsMargins(0, 0, 0, 0)
        self.chat_layout.setSpacing(5)

        # 创建消息显示区域
        self.chat_widget = QWidget()
        self.chat_widget.setLayout(self.chat_layout)

        # 将消息显示区域添加到滚动区域中
        self.scrollArea.setWidget(self.chat_widget)
        self.scrollArea.setWidgetResizable(True)

    def closeEvent(self, event):
        print("close...")
        self.socket.terminate()  # 首先尝试终止线程
        self.socket.wait()  # 等待线程安全退出
        event.accept()

    def recv_message(self, message):
        # 确保将接收到的消息追加到文本编辑框中
        for i in message:
            self.addMessage(i[2], False)  # 假设 textEdit 是 setupUi 中设置的 QTextEdit 控件

    def send_message(self):
        input_json = {
            "username": self.username,
            "contact_name": self.contact,
            "message": self.plainTextEdit.toPlainText()
        }
        # 假设 Post.get_post 是一个有效的网络请求
        if Post.get_post("http://119.188.240.140:22255/chat/post/send_message", input_json):
            self.addMessage(self.plainTextEdit.toPlainText(), True)
            self.plainTextEdit.clear()

    def addMessage(self, message, is_sender):
        chat_bubble = ChatBubble(message, is_sender)
        self.chat_layout.addWidget(chat_bubble)
        self.scrollArea.ensureWidgetVisible(chat_bubble, 0)
