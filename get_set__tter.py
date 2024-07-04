class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height


    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value

    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value

    @property
    def area(self):
        return self._width * self._height
    
    @property
    def perimetr(self):
        return 2 * (self._height + self._width)

rect = Rectangle(5, 10)
print(rect.area)

rect.width = 500

print(rect.perimetr)


