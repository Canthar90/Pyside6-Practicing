from PySide6 import QtCore


class CheckStates():
    
    @QtCore.Slot()
    def simple_print(self, state1, state2):
        print(state1)
        print(state2)
