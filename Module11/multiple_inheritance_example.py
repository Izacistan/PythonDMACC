class Human:
    def __init__(self, age, name):
        self._age = age
        self._name = name


class Dancer:
    def __init__(self, style):
        self._style = style


class Student(Human, Dancer):
    def __init__(self, _age, _name, _style):
        Human.__init__(self, _age, _name)
        Dancer.__init__(self, _style)


John = Student(20, "John", "HipHop")
print(John._style)
print(John._age)
print(John._name)