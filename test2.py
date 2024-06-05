import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor
from qfluentwidgets import ListWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 创建 QListWidget
        self.list_widget = ListWidget(self)
        self.setCentralWidget(self.list_widget)

        # 添加一些 QListWidgetItem
        for i in range(5):
            item = QListWidgetItem(self.list_widget)
            item.setText(f"Item {i + 1}")

        # 修改特定 QListWidgetItem 的颜色
        self.modify_item_color("Item 2", QColor(0, 128, 128, 64))

    def modify_item_color(self, text, color):
        # 遍历 QListWidget 中的所有项
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            if item.text() == text:
                # 设置前景颜色
                item.setForeground(QBrush(color))
                item.setBackground(QBrush(color))


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
