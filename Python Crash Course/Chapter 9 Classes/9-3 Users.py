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


u1 = User('Jackson', 'Huang', 'jacksonh201325@gmail.com', 'Chilli Willy', '+1-905-515-2767')
u1.greet_user()
u1.describe_user()
