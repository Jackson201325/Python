class Horse():
    def __init__ (self, name, size, color, weight, owner):
        self.name = name
        self.size = size
        self.color = color
        self.weight = weight
        self.owner = owner

class Rider():
    def __init__ (self, name, s):
        self.name = name
        self.sex = s

Jack = Rider("Jackson", "Male")
Holska = Horse("Holska","Big", "Brown", "Heavy", Jack)

print(Holska.owner.sex)
print(Holska.color)
print(Jack.sex)
