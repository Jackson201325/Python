class Person():
    def __init__ (self, name):
        self.name = 'Bob'

bob = Person()
bob1 = bob
print(bob is bob1)

bob2 = Person()
print (bob is bob2)
