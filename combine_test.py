from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QGraphicsGridLayout, QGraphicsScene, QGraphicsWidget, QGridLayout
from checkbox import AnimatedToggle
from barwidget import PowerBar

colors_3 = (["#5e4fa2", "#3288bd", "#66c2a5", "#abdda4", "#e6f598", "#ffffbf", "#fee08b", "#fdae61", "#f46d43", "#d53e4f", "#9e0142"])

app = QApplication([])

window = QWidget()

main_toggle = AnimatedToggle()
secondary_toggle = AnimatedToggle(
    checked_color="#FFB000",
    pulse_checked_color="#44FFB000"
)
main_toggle.setFixedSize(main_toggle.sizeHint())
secondary_toggle.setFixedSize(secondary_toggle.sizeHint())


speed_bar = PowerBar(colors_3)


window.setLayout(QGridLayout())
window.layout().addWidget(speed_bar, 0, 0, 5, 3)

window.layout().addWidget(QLabel("Main Toggle"), 2, 4)
window.layout().addWidget(main_toggle, 3, 4)

window.layout().addWidget(QLabel("Secondary Toggle"), 4, 4)
window.layout().addWidget(secondary_toggle, 5, 4)

main_toggle.stateChanged.connect(secondary_toggle.setChecked)

window.show()
app.exec()