
import pyqtgraph as pg  # import PyQtGraph after Qt
from PySide6.QtWidgets import QApplication, QMainWindow

class Graph(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        # plot data: x, y values
        self.graphWidget.plot(hour, temperature)

