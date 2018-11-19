class User():
    def __init__(self, first, last, email, gender, number):
        self.first = first
        self.last = last
        self.email = email
        self.gender = gender
        self.number = number

    def greet_user(self):
        print("Hi, " + self.first.title() + " " + self.last.title() + " how are you ?")

    def describe_user(self):
        print("The user name is: " + self.first.title() + " " + self.last.title() + ".")
        print("His email is " + self.email + ", the phone number is " +
              self.number + " .You sexually identify yourself as " + self.gender + ".")


class Priviledges():
    def __init__(self, priviledge=['can add post', 'can delete post', 'can ban user']):
        self.priviledge = priviledge

    def show_priviledge(self):
        print("The set of a admin priviledges are: ")
        for priviledge in self.priviledge:
            print(priviledge)


class Admin(User):
    def __init__(self, first, last, email, gender, number):
        super().__init__(first, last, email, gender, number)
        self.priviledge = Priviledges()


yo = Admin('Jackson', 'Huang', 'jacksonh201325@gmail.com', 'Chilly willy', '+1 905-515-2767')
yo.describe_user()
yo.priviledge.show_priviledge()
