class Shape:
    """Shape class"""
    colors = ['BLUE', 'GREEN', 'ORANGE', 'PURPLE', 'RED', 'YELLOW', "LAVENDER"]

    def __init__(self, color='BLUE'):
        self._color = color

    def change_color(self, new_color):
        if new_color not in self.colors:
            raise InvalidColorError
        self._color = new_color

    def display_color(self):
        return str(self._color)

class Rectangle(Shape):   # Base class is Shape
    """Rectangle derived class of Shape base class"""
    def __init__(self, c='RED', l=0, w=0):  # default values
        super().__init__(c)  # calls the base constructor
        self._length = l
        self._width = w

    def area(self):
        return self._length * self._width

    def display_color(self):
        return str('Rectangle color ' + self._color)


class InvalidColorError(Exception):
    """InvalidColorError is derived class of Exception base class"""
    pass

# Driver
# my_shape = Shape()
# color = 'blue'
# try:
#     my_shape.change_color(color)
# except InvalidColorError:
#     print("Color is not valid:", color)
#     print("Color is", my_shape.display_color())

# Driver
my_shape = Shape()
my_rectangle = Rectangle()
# Tests if object my_shape is Shape
print('my_shape is a Shape:', isinstance(my_shape, Shape))
# Tests if object my_rectangle is Shape
print('my_rectangle is a Shape:', isinstance(my_rectangle, Shape))
# Tests if object my_shape is Rectangle
print('my_shape is a Rectangle:', isinstance(my_shape, Rectangle))
# Tests if object my_rectangle is Rectangle
print('my_rectangle is a Rectangle:', isinstance(my_rectangle, Rectangle))
