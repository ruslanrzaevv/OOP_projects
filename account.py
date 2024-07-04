import pytz
from datetime import datetime


class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.history = []

    @staticmethod
    def current_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self.balance += amount
        self.history.append([amount, self.current_time()])
        self.show_balance()

    def withdraw(self, amount):
        self.balance -= amount
        self.history.append([-amount, self.current_time()])
        self.show_balance()

    def show_balance(self):
        print(f'Your balance: {self.balance}')

    def show_history(self):
        for amount, time in self.history:
            if amount > 0:
                print(f'Внесено {amount} в {time}')
            else:
                print(f'Потрачено {amount} в {time}')