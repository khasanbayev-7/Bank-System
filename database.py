import json

def load_users():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_users(data):
    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)
