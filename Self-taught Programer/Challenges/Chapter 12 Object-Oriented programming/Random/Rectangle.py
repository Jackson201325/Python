class Rectangle():
    def __init__ (self, l ,w):
        self.length = l
        self.width = w

    def area (self):
        return self.length * self.width

    def changed_size(self, l, w):
        self.length = l
        self.width = w

r1 = Rectangle(10, 20)
print (r1.area())
r1.changed_size(20, 30)
print (r1.area())
