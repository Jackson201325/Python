""" Make a Hexagon class with a method called calculate perimeter that calculates and returns its perimeter. Then create a Hexagon object
call calculate perieter on it and print the result"""

class Hexagon:
    def __init__ (self, s):
        self.side = s

    def area(self):
        return self.side * 6
h1 = Hexagon(3)
print(h1.area())
