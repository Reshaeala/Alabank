from django.db import models
from django import forms

# Create your models here.

#
# class SignUp(forms.Form):
#     first_name = forms.CharField(initial='First Name')
#     last_name = forms.CharField()
#     email = forms.EmailField(help_text='write your email')
#     password = forms.CharField(widget=forms.PasswordInput)
#     re_password = forms.CharField(help_text='renter your password', widget=forms.PasswordInput)
#

class Account(models.Model):
    item = models.CharField(max_length=200, default='')
    cost = models.DecimalField(decimal_places=2, max_digits=500)
    savings = models.DecimalField(decimal_places=2, max_digits=500)

    def __str__(self):
        return self.item


    def __init__(self):
        self.balance = 0
        self.transactions = []


    # def deposit(self):
    #     amount = float(input("Enter amount to be Deposited: "))
    #     self.balance += amount
    #     print("\n Amount Deposited:", amount)
    #
    # def withdraw(self):
    #     amount = float(input("Enter amount to be Withdrawn: "))
    #     if self.balance >= amount:
    #         self.balance -= amount
    #         self.transactions.append(-amount)
    #         print("\n You Withdrew:", amount)
    #     else:
    #         print("\n Insufficient balance  ")
    #
    # def display(self):
    #     print("\n Net Available Balance=", self.balance)
    #
    # def get_balance(self):
    #     return self.balance
    #
    # def recent_transactions(self):
    #     if len(self.transactions) < 1:
    #         return None
    #     else:
    #         return self.transactions.pop()
