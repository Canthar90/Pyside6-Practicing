from PySide6.QtWidgets import QWidget
from PySide6 import QtWidgets
from PySide6.QtCore import QPropertyAnimation, QSequentialAnimationGroup, QPoint, QSize
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(100, 100)
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setEndValue(QPoint(200, 200))
        self.anim.setDuration(1500)
        self.anim_2 = QPropertyAnimation(self.child, b"size")
        self.anim_2.setEndValue(QSize(250, 150))
        self.anim_2.setDuration(2000)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()
        

app = QtWidgets.QApplication(sys.argv)
basic_animation = Window()
basic_animation.show()
app.exec()