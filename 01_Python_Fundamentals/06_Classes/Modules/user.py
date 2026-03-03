class User:
    def __init__(self, first_name, last_name, age, mobile_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.mobile_number = mobile_number
        self.login_attempts = 0

    def describe_user(self):
        print("USER SUMMARY")
        print(f"First Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Mobile Number: {self.mobile_number}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}! "
              f"Hope you are doing well.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
