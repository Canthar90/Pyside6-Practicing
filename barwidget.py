from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class _Bar(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding
        )

    def siezeHint(self):
        return QtCore.QSize(40,120)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)

        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor('black'))
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        dial = self.parent()._dial
        vmin, vmax = dial.minimum(), dial.maximum()
        value = dial.value()

        
        padding = 5 
        d_height = painter.device().height() - (padding * 2)
        d_width = painter.device().width() - (padding * 2)
        step_size = d_height / 8
        bar_height = step_size * 0.5
        bar_spacer = step_size * 0.2 /2

        pc = (value - vmin) / (vmax - vmin)
        n_step_to_draw = int(pc * 8)
        brush.setColor(QtGui.QColor('red'))

        for n in range(n_step_to_draw):
            rect = QtCore.QRect(
                padding,
                padding + d_height - ((1 + n) * step_size) + bar_spacer,
                d_width,
                bar_height
            )
            painter.fillRect(rect, brush)
        painter.end()

    def _trigger_refresh(self):
        self.update()




class PowerBar(QtWidgets.QWidget):
    """Custom Qt widget to show a power bar and dial 
    Demostarating compound and custom-drawn wiget"""

    def __init__(self, steps=5, *args, **kwargs):
        super(PowerBar, self).__init__(*args, **kwargs)

        layout = QtWidgets.QVBoxLayout()
        self._bar = _Bar()
        layout.addWidget(self._bar)

        self._dial = QtWidgets.QDial()
        layout.addWidget(self._dial)

        self.setLayout(layout)
        self._dial.valueChanged.connect(self._bar._trigger_refresh)