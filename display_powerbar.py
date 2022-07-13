import sys
from PySide6 import QtCore, QtGui, QtWidgets
from barwidget import PowerBar


app = QtWidgets.QApplication(sys.argv)
volume = PowerBar()
volume.show()
app.exec()