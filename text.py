import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import QStandardPaths


class DownloadWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Download File Interface")
        self.setGeometry(100, 100, 280, 150)  # x, y, width, height

        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建一个按钮用于触发选择保存文件路径的操作
        self.downloadButton = QPushButton("Choose Save Location", self)
        self.downloadButton.clicked.connect(self.chooseSaveLocation)
        layout.addWidget(self.downloadButton)

        # 创建一个容器widget
        widget = QWidget()
        widget.setLayout(layout)

        # 设置中央小部件
        self.setCentralWidget(widget)

    def chooseSaveLocation(self):
        # 设置默认的下载路径（例如用户的下载目录）
        default_path = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)

        # 弹出对话框让用户选择保存文件的位置和文件名
        # 如果用户没有选择文件名，则默认文件名为 "default_filename.txt"
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File",
                                                  default_path + "/default_filename.txt",
                                                  "All Files (*)",
                                                  options=options)
        if fileName:  # 如果用户指定了文件名
            self.saveFilePath = fileName  # 存储文件路径
            self.startDownload(self.saveFilePath)  # 启动下载过程（示例中未实现）

    def startDownload(self, filePath):
        # 这里可以添加实际的下载文件逻辑
        # 假设下载成功，可以给用户一个提示
        QMessageBox.information(self, "Download", f"File will be saved to: {filePath}")


