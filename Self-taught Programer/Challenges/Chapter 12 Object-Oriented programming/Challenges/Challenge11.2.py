import math

class Circle:
    def __init__ (self, r):
        self.radius = r
    def area (self):
        return self.radius ** 2 * math.pi
c1 = Circle(4)
print (c1.area())
