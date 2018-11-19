class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print("The name of the restuarant is " + self.name.title() +
              " and the cuisine type is " + self.cuisine.title())

    def open_restaurant(self):
        print("The restaurant is opened")

    def number_of_serves(self):
        return "The number of served dishes today is: {}.".format(self.number_served)

    def increment_number_served(self, increment):
        self.number_served += increment
        print("The cuisine have served " + str(self.number_served) + " dishes.")


r1 = Restaurant('Jackson', 'Italian')
r1.open_restaurant()
r1.describe_restaurant()
print(r1.number_of_serves())
r1.increment_number_served(5)
