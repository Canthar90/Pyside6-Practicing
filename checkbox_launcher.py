from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from checkbox import AnimatedToggle

app = QApplication([])

window = QWidget()

main_toggle = AnimatedToggle()
secondary_toggle = AnimatedToggle(
    checked_color="#FFB000",
    pulse_checked_color="#44FFB000"
)
main_toggle.setFixedSize(main_toggle.sizeHint())
secondary_toggle.setFixedSize(secondary_toggle.sizeHint())

window.setLayout(QVBoxLayout())
window.layout().addWidget(QLabel("Main Toggle"))
window.layout().addWidget(main_toggle)

window.layout().addWidget(QLabel("Secondary Toggle"))
window.layout().addWidget(secondary_toggle)

main_toggle.stateChanged.connect(secondary_toggle.setChecked)

window.show()
app.exec()