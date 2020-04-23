from django.db import models

# Create your models here.


class Account(models.Model):
    def __init__(self):
        self.balance = 0
        self.transactions = []
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(-amount)
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def display(self):
        print("\n Net Available Balance=", self.balance)

    def get_balance(self):
        return self.balance

    def recent_transactions(self):
        if len(self.transactions) < 1:
            return None
        else:
            return self.transactions.pop()
