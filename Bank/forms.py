from django import forms
from .models import Account

class CreateAccount(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'