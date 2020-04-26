from django.shortcuts import render, redirect
from .forms import CreateAccount
from .models import Account
from django.http import HttpResponse


def index(request):
    account_info = Account.objects.all()
    return render(request, "build/index.html", {'account_info': account_info})


def addAccount(request):
    addAccount = CreateAccount()
    if request.method == 'POST':
        addAccount = CreateAccount(request.POST, request.FILES)
        if addAccount.is_valid():
            addAccount.save()
            return redirect('index')
    else:
        return render(request, 'account_form.html', {'account_form': addAccount})


def updateAccount(request, Bank_id):
    Bank_id = int(Bank_id)
    try:
        account_info = Account.objects.get(id=Bank_id)
    except Account.DoesNotExist:
        return redirect('index')
    account_form = CreateAccount(request.POST or None, instance=account_info)
    if account_form.is_valid():
        account_form.save()
        return redirect('index')
    return render(request, 'account_form.html', {'account_form': account_form})


def deleteAccount(request, Bank_id):
    Bank_id = int(Bank_id)
    try:
        account_info = Account.objects.get(id=Bank_id)
    except Account.DoesNotExist:
        return redirect('index')
    account_info.delete()
    return redirect('index')
