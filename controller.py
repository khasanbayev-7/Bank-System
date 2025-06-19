import json
from user import User

class CommandController:
    def __init__(self, command):
        self.command = command

class RegisterController(CommandController):
    def __init__(self, command):
        super().__init__(command)
        self.labels = {
            "first_name": "Ismingiz: ",
            "last_name": "Familiyangiz: ",
            "age": "Yoshingiz: ",
            "email": "Email: ",
            "passport_id": "Pasport ID: ",
            "password": "Parol: ",
        }

    def register(self):
        userDetails = {}
        for field, label in self.labels.items():
            value = input(label)
            if field == "age":
                value = int(value)
            userDetails[field] = value

        user = User(
            role="customer",
            first_name=userDetails["first_name"],
            last_name=userDetails["last_name"],
            age=userDetails["age"],
            passport_id=userDetails["passport_id"],
            password=userDetails["password"],
            email=userDetails["email"],
        )

        user_data = {
            "role": user.role,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
            "passport_id": user.passport_id,
            "email": user.email,
            "balance": user.balance,
            "cards": user.cards,
        }

        try:
            with open("users.json", "r") as file:
                data = json.load(file)
        except:
            data = []

        data.append(user_data)

        with open("users.json", "w") as file:
            json.dump(data, file, indent=4)

        print("✅ Foydalanuvchi muvaffaqiyatli qo‘shildi!")

class LoginController(CommandController):
    def login(self):
        passport_id = input("Pasport ID: ")
        password = input("Parol: ")

        try:
            with open("users.json", "r") as file:
                data = json.load(file)
        except:
            print("❌ Hech qanday foydalanuvchi mavjud emas.")
            return None

        for user in data:
            if user["passport_id"] == passport_id and user["email"] and user["balance"] >= 0:
                print("✅ Muvaffaqiyatli tizimga kirildi.")
                return user

        print("❌ Noto‘g‘ri ma’lumot.")
        return None

class BalanceController(CommandController):
    def show_balance(self, user):
        if user:
            print(f"💰 Balans: {user['balance']} UZS")
        else:
            print("❌ Avval login qiling.")
