import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from random import randint, choice


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("New Window")
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        # layout.addWidget(self.label)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.draw_rectangles()

    def draw_rectangles(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor("#376F9F"))
        painter.setPen(pen)
        painter.drawRoundedRect(40, 40, 100, 100, 10, 10)
        painter.drawRoundedRect(80, 80, 100, 100, 10, 50)
        painter.drawRoundedRect(120, 120, 100, 100, 50, 10)
        painter.drawRoundedRect(160, 160, 100, 100, 50, 50)
        painter.end()
        self.label.setPixmap(canvas)

        painter.end()
        self.label.setPixmap(canvas)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel("kopytko")
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.new_windows()
        self.draw_something()
        


    def draw_something(self):
        colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']

        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor('#376F9F'))
        painter.setPen(pen)
        
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor("#FFD141"))
        brush.setStyle(Qt.Dense1Pattern)
        painter.setBrush(brush)
        
        painter.drawRects([
            QtCore.QRect(50, 50, 100, 100),
            QtCore.QRect(60, 60, 150, 100),
            QtCore.QRect(70, 70, 100, 150),
            QtCore.QRect(80, 80, 150, 100),
            QtCore.QRect(90, 90, 100, 150),
            ])
        
        painter.end()
        self.label.setPixmap(canvas)

    def new_windows(self):
        self.w = AnotherWindow()
        self.w.show()

    


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()