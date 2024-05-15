import sys
from PySide6 import QtWidgets

from qt_material import apply_stylesheet


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()


apply_stylesheet(app, theme='dark_teal.xml')


window.show()
app.exec()
