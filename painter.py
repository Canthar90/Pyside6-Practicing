import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from random import randint, choice


class TekstWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Text Window")
        canvas = QtGui.QPixmap(500, 400)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.draw_tekst()


    def draw_tekst(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor('green'))
        painter.setPen(pen)

        font = QtGui.QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)

        painter.drawText(100, 100, "Hello There")
        painter.drawText(200, 200, 100, 100, Qt.AlignHCenter, "Hello world")
        painter.end()
        self.label.setPixmap(canvas)


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("New Window")
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
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

        # painter.end()
        # self.label.setPixmap(canvas)


class ThirdWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.draw_elipse()


    def draw_elipse(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor(204, 0, 0))
        painter.setPen(pen)

        painter.drawEllipse(10, 10, 100, 100)
        painter.drawEllipse(10, 10, 150, 200)
        painter.drawEllipse(10, 10, 200, 300)

        painter.drawEllipse(QtCore.QPoint(200, 200), 10, 10)
        painter.drawEllipse(QtCore.QPoint(200, 200), 15, 20)
        painter.drawEllipse(QtCore.QPoint(200, 200), 20, 30)
        painter.drawEllipse(QtCore.QPoint(200, 200), 25, 40)
        painter.drawEllipse(QtCore.QPoint(200, 200), 30, 50)
        painter.drawEllipse(QtCore.QPoint(200, 200), 35, 60)

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
        self.w1 = ThirdWindow()
        self.w1.show()
        self.t = TekstWindow()
        self.t.show()

    


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()