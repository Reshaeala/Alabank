from django.shortcuts import render, redirect
from .forms import CreateAccount, CreateUserForm
from .models import Account
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

    context = {'form': form}
    return render(request, 'account/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'account/login.html', context)

def logOutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def customer(request):
    return render(request, "customer.html")


@login_required(login_url='login')
def index(request):
    account_info = Account.objects.all()
    return render(request, "index.html", {'account_info': account_info})


@login_required(login_url='login')
def addAccount(request):
    addAccount = CreateAccount()
    if request.method == 'POST':
        addAccount = CreateAccount(request.POST, request.FILES)
        if addAccount.is_valid():
            addAccount.save()
            return redirect('index')
    else:
        return render(request, 'account_form.html', {'account_form': addAccount})

@login_required(login_url='login')
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


@login_required(login_url='login')
def deleteAccount(request, Bank_id):
    Bank_id = int(Bank_id)
    try:
        account_info = Account.objects.get(id=Bank_id)
    except Account.DoesNotExist:
        return redirect('index')
    account_info.delete()
    return redirect('index')
