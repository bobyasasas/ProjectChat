import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Pie Chart Example")
        self.setGeometry(100, 100, 400, 300)

        # 创建一个 matplotlib 图表
        self.figure = Figure()
        self.pieChart = self.figure.add_subplot(111)

        # 准备饼图数据
        labels = ['abby', 'ceil', 'kai', 'jyj']
        sizes = [215, 130, 245, 210]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

        # 确保 explode 列表的长度与 sizes 列表相同
        explode = [0.1 if i == 0 else 0 for i in range(len(sizes))]

        # 绘制饼图
        self.pieChart.pie(sizes, explode=explode, labels=labels, colors=colors,
                          autopct='%1.1f%%', shadow=True, startangle=90)

        # 隐藏图表的坐标轴
        self.pieChart.axis('equal')

        # 创建一个 FigureCanvas 并将其添加到 PyQt6 布局中
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)



