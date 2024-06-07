import os
import sys

import websockets

from PySide6.QtCore import QThread, Signal, QTimer
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication

from chat import ChatWindow, ChatBubble, BubbleMessage
from myUtil import Post
from myUtil.DataBase import Database
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
        config_path = os.getenv("LOCALAPPDATA")
        config_path = config_path + "\k-chat\\"
        path = config_path + self.username + ".db"
        self.db = Database(path)
        table_name = self.contact
        columns = {
            "message": "TEXT",
            "is_sender": "INTEGER"  # 假设 is_sender 是一个整数，你可以用它来表示发送者（1）或接收者（0）
        }

        # 创建表
        self.db.create_table(table_name, columns)
        columns_to_select = "message, is_sender"
        messages = self.db.select(table_name, columns_to_select)
        for message in messages:
            self.addMessage(message[0], message[1])

    def closeEvent(self, event):
        print("close...")
        self.socket.terminate()  # 首先尝试终止线程
        self.socket.wait()  # 等待线程安全退出
        self.db.close()
        event.accept()

    def recv_message(self, message):
        # 确保将接收到的消息追加到文本编辑框中
        for i in message:
            self.addMessage(i[2], False)
            data_to_insert = {
                "message": i[2],
                "is_sender": 0  # 假设 1 表示消息是发送者发出的
            }
            self.db.insert(self.contact, data_to_insert)

    def send_message(self):
        input_json = {
            "username": self.username,
            "contact_name": self.contact,
            "message": self.textEdit.toPlainText()
        }
        # 假设 Post.get_post 是一个有效的网络请求
        if Post.get_post("http://119.188.240.140:22255/chat/post/send_message", input_json):
            data_to_insert = {
                "message": self.textEdit.toPlainText(),
                "is_sender": 1  # 假设 1 表示消息是发送者发出的
            }
            self.db.insert(self.contact, data_to_insert)
            self.addMessage(self.textEdit.toPlainText(), True)
            self.textEdit.clear()

    def addMessage(self, message, is_sender):
        chat_bubble = BubbleMessage(message, is_sender)
        self.chat_layout.addWidget(chat_bubble)

        # 使用 QTimer 延迟滚动到底部，确保布局更新完成
        QTimer.singleShot(100, self.scrollToBottom)

    def scrollToBottom(self):
        # 滚动条可能需要更新，因为它的最大值可能已经改变
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())


if __name__ == "__main__":
    app = QApplication([])
    window = UIMessageWindow("abby", "kai")
    window.show()
    sys.exit(app.exec())
