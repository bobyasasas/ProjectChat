import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

from test import Graph
from ui_analyse import Ui_Form


# 假设 Graph 类已经定义，并且可以实例化和显示
# from your_module import Graph

class Analyse(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.widget_1 = self.findChild(QWidget, "widget_1")  # 确保正确获取 widget_1
        if self.widget_1 is not None:
            self.widget_1.setLayout(QVBoxLayout())
            self.graph = Graph()
            self.widget_1.layout().addWidget(self.graph)
        else:
            print("Error: widget_1 not found in the UI.")

# 主程序
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Analyse()
    window.show()
    if not app.exec():
        print("Error: QApplication.exec() returned with an error.")
    sys.exit(app.exec())