# Clase 31 Agosto, 2022
from random import randint

class Budget:

    def __init__(self, category: str, innitial_balance: float) -> None:
        self.category = category
        self.innitial_balance  = innitial_balance
        self.running_balance = innitial_balance

    def get_running_balance(self) -> float:
        return self.running_balance

    def withdraw(self, amount: float) -> None:
        self.running_balance -= amount

    def deposite(self, amount: float) -> None:
        self.running_balance += amount


class User:
    
    def __init__(self, name: str, total_budget: float) -> None:
        self.name = name
        self.id = randint(1, 1000)
        self.total_budget = total_budget
        self.budgets = dict()
    
    def add_budget(self, category: str, innitial_balance: float) -> float:
        budget = Budget(category=category, 
                        innitial_balance=innitial_balance)
        self.budgets.update({category: budget})

    def transfer_balance(self, sender: str, receiver: str, amount: float) -> None:
        pass




