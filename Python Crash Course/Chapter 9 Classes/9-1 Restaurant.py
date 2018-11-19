class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print("The name of the restuarant is " + self.name.title() +
              " and the cuisine type is " + self.cuisine.title())

    def open_restaurant(self):
        print("The restaurant is opened")


r1 = Restaurant('Jackson', 'Italian')
r1.open_restaurant()
r1.describe_restaurant()
