class MyCustomClass:

    def __init__(self):
        self.value = None


    @property
    def value(self):
        print("getting the value", self._value)
        return self._value

    @value.setter
    def value(self, value):
        print("setting the value", value)
        self._value = value


obj = MyCustomClass()

a = obj.value       
# Acces the value
print(a)
obj.value = 'hello'  
# Set the value
b = obj.value        
# Acces the value
print(b)