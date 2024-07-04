# class Calc:
#     def pl(self, a, b):
#         return a + b
#     def mn(self, a, b):
#         return a - b
#     def de(self, a ,b):
#         return a / b
#     def um(self, a, b):
#         return a * b
    
# c = Calc
# c.pl()

# class Calc:
#     def sum(self, first_num, second_num):
#         return first_num + second_num

#     def minus(self, first_num, second_num):
#         return first_num - second_num

#     def multiplication(self, first_num, second_num):
#         return first_num * second_num

#     def division(self, first_num, second_num):
#         if second_num == 0:
#             return 'На ноль не делится'

#         return first_num / second_num


# c = Calc(1, 1)
# c.sum()


import pytz
from datetime import datetime

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.history = []


    def deposit(self, amount):
        self.__balance += amount
        self.history.append([amount, self.current_time()])
        self.show_balance()


    def pay(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'You spent {amount}')
            self.history.append([-amount, self.current_time()])

        else:
            print(f'Not enough money your balance {self.__balance}')
        self.show_balance()

    @staticmethod
    def current_time():
        return datetime.now(pytz.utc)
    
    def show_history(self):
        for self.amount, time in self.history:
            if self.amount > 0:
                print(f'Submitted {self.__balance} in {time}')
            else:
                print(f'Spent {self.__balance} in {time}')

    def show_balance(self):
        print(f'Your balance {self.__balance}')


a = Account('ruslan', 40000000)
a.deposit(100)
a.show_history()