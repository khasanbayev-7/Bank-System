from user import User

def find_user_by_passport(passport_id, users):
    for u in users:
        if u["passport_id"] == passport_id:
            return u
    return None
