import re
class Abc:
    def __init__(self, a, b):
        self._field1 = a
        self._field2 = b

    def __str__(self):
        return f'Field 1: {self._field1}, Field 2: {self._field2}'



obj = Abc("Hello", '$World')
print(obj)
abc = obj

new = re.sub(r'\$', '_', str(obj))

print(new)  # Выводит "Hello _world!"