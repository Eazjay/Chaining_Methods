

class User:
    def __init__(self, first_name, last_name, age, account_balance):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.balance = account_balance
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    def display_user_balance(self):
        print(f"\n{self.first_name}'s account balance is: {self.balance}")
        return self



Joel = User("Joel", "Okoh" ,35 ,500)
Joel.make_deposit(50).make_deposit(50).make_deposit(50).make_deposit(50).make_withdrawal(20).display_user_balance()

Babe = User("Katie", "Rose", 22, 50).make_deposit(50).make_deposit(100).make_withdrawal(10).make_withdrawal(20).display_user_balance()

Friend = User("Ossai", "J", 38, 450)
Friend.make_deposit(100).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()