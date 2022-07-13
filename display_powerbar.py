import sys
from PySide6 import QtCore, QtGui, QtWidgets
from barwidget import PowerBar


app = QtWidgets.QApplication(sys.argv)
volume = PowerBar()
volume.setGeometry(0, 0, 150, 400)
volume.show()
app.exec()