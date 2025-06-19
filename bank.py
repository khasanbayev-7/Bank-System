from typing import Any, List, Dict


class Bank:
    """
    Bank classi, bu klassda quyidagi amallar bajarilishi mumkin:
        
    """


    def __init__(
        self,
        name: str,
        address,
        head: str,
        balance: int = 0,
        currencies: List[str] = [],
    ):
        self.name = name
        self.address = address
        self.currencies = currencies
        self.balance = balance
        self.head = head


    def __str__(self):
        return f"""{self.address}da joylashgan {self.head} boshchiligidagi {self.name} banki"""


bank = Bank(
    name="Humo", address="Namangan shahar, Chorsu, 18 ko'cha", head="Ism familiya"
)
print(bank)