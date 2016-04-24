import math

class Square(object):
    def __init__(radius):
        self.radius = radius

    def calculate_area(self):
        return math.sqrt(self.radius) * math.pi 


def example():
    square_a = Square(5)
    return square_a.calculate_area()
