class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print("The name of the restuarant is " + self.name.title() +
              " and the cuisine type is " + self.cuisine.title())

    def open_restaurant(self):
        print("The restaurant is opened")


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ["Vainilla", "Chocolate", "Granizado"]

    def show_flavors(self):
        print("The flavours available are: ")
        for flavor in self.flavors:
            print(flavor)


r2 = IceCreamStand('Roberto', 'Puto')
r2.describe_restaurant()
r2.show_flavors()
