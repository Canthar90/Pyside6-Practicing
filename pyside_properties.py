from PySide6.QtCore import Property, QObject


class CustomObject(QObject):
    def __init__(self):
        super().__init__()
        self.value = 0

    @Property(int)
    def value(self):
        return self._value

    @value.setter
    def value(self,value):
        self._value = value


        # emits signal when value is changed
        if value != self._value:
            self._value = value
            self.valueChanged.emit(value)



obj = CustomObject()
obj.value = 7
print(obj.value)