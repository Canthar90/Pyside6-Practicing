import logging
from multiprocessing import Process
import time
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout
from checkbox import AnimatedToggle
from barwidget import PowerBar
from PySide6 import QtCore

@QtCore.Slot()
def checking_power():
    while True:
        time.sleep(2)
        print(speed_bar.value())
    
@QtCore.Slot()    
def checking():
    print(main_toggle.isChecked())
    print(secondary_toggle.isChecked())
    print(speed_bar.value())
    print(type(speed_bar.value()))

logging.basicConfig(level=logging.INFO)
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

check_button = QPushButton("check varibles")
check_button.setStyleSheet("""
    background-color: #D49B54;
    padding 20px;
    font-size: 18px;
    max-width: 120px;
    height: 50px;
    border-radius: 10px
    """)

check_button.clicked.connect(checking)

speed_bar = PowerBar(colors_3)


window.setLayout(QGridLayout())
window.layout().addWidget(speed_bar, 0, 0, 11, 3)

window.layout().addWidget(QLabel("Main Toggle"), 9, 4)
window.layout().addWidget(main_toggle, 10, 4)

window.layout().addWidget(QLabel("Secondary Toggle"), 11, 4)
window.layout().addWidget(secondary_toggle, 12, 4)

window.layout().addWidget(check_button, 12, 0)

window.setGeometry(0, 0, 250, 450)
main_toggle.stateChanged.connect(secondary_toggle.setChecked)



window.show()

if __name__ == '__main__':
    x = Process(target=checking_power())
    x.start()
    x.join()
app.exec()



