class Triangle():
    def __init__ (self, b,h):
        self.base = b
        self.height = h

    def area (self):
        return self.base * self.height / 2

t1 = Triangle(10, 20)
print(t1.area())
