import sys
from PySide6 import QtCore, QtGui, QtWidgets
from barwidget import PowerBar


colors_1 = 10
colors_2 = 3
colors_3 = (["#5e4fa2", "#3288bd", "#66c2a5", "#abdda4", "#e6f598", "#ffffbf", "#fee08b", "#fdae61", "#f46d43", "#d53e4f", "#9e0142"])
colors_4 = (["#a63603", "#e6550d", "#fd8d3c", "#fdae6b", "#fdd0a2", "#feedde"])


app = QtWidgets.QApplication(sys.argv)
volume = PowerBar(colors_3)
volume.setGeometry(0, 0, 150, 400)
volume.show()
app.exec()