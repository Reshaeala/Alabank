from django import forms
from .models import Account
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateAccount(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
