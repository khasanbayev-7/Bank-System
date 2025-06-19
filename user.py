class User:
    def __init__(self, role, first_name, last_name, age, passport_id, password, email):
        self.role = role
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.passport_id = passport_id
        self.password = password
        self.email = email
        self.balance = 0
        self.cards = []

    def __str__(self):
        return (
            f"User({self.first_name} {self.last_name}, Role: {self.role}, Age: {self.age}, "
            f"Passport ID: {self.passport_id}, Email: {self.email}, "
            f"Balance: {self.balance}, Cards: {len(self.cards)})"
        )