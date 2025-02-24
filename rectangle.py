import math

class Rectangle:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b

    # Create method "is_valid" in the Rectangle class
    # This method checks if the rectangle is valid
    # True if the rectangle is valid, False otherwise

    # Create method "perimeter" in the Rectangle class
    # This method finds the perimeter of the rectangle
    # return perimeter of the rectangle if the rectangle is valid, 0 otherwise

    # Create method "area" in the Rectangle class
    # This method finds the area of the rectangle
    # return area of the rectangle if the rectangle is valid, 0 otherwise
    def is_valid(self):
        if self.a == self.b:
            return True
        else:
            False
    def perimeter(self):
        if self.is_valid():
            return (self.a + self.b)*2
        else:
            return 0
    def area(self):
        if self.is_valid():
            return self.a * self.b
        else:
            return 0

