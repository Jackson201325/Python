class User():
    def __init__(self, first, last, email, gender, number):
        self.first = first
        self.last = last
        self.email = email
        self.gender = gender
        self.number = number
        self.attempts = 5

    def greet_user(self):
        print("Hi, " + self.first.title() + " " + self.last.title() + " how are you ?")

    def describe_user(self):
        print("The user name is: " + self.first.title() + " " + self.last.title() + ".")
        print("His email is " + self.email + ", the phone number is " +
              self.number + " .You sexually identify yourself as " + self.gender + ".")

    def inrement_login_attempts(self, chances):
        self.attempts -= chances
        if self.attempts >= 1:
            print("You have " + str(self.attempts) + " attempts left.")
        else:
            User.reset_login_attempts(self)

    def reset_login_attempts(self):
        print("You ran out of chances plz KYS ")


u1 = User('Jackson', 'Huang', 'jacksonh201325@gmail.com', 'Chilli Willy', '+1-905-515-2767')
u1.greet_user()
u1.describe_user()
u1.inrement_login_attempts(5)
