from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Budget
from.forms import BudgetForm
from django.contrib.auth import logout



# Create your views here.
def index(request):
    return HttpResponse("Hello, Index")


def budgeting(request):
    return HttpResponse("Hello, budgeting")


def investment(request):
    return HttpResponse("Hello, investment")


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # get the user info from the form data and log in the user
            user = form.get_user()
            login(request, user)
            return redirect('budget-dashboard')
        # else:
        #     render(request, 'budget/login.html', context={'form': form, 'isValid': False})
    else:
        form = AuthenticationForm()
        return render(request, 'budget/login.html', context={'form': form, 'isValid': True})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    # check whether it's valid: for example it verifies that password1 and password2 match
        if form.is_valid():
            form.save()
    # redirect the user to login page so that after registration the user can enter the credentials
        return redirect('budget-dashboard')
    else:
        # Create an empty instance of Django's UserCreationForm to generate the necessary html on the template.
        form = UserCreationForm()
        return render(request, 'budget/register.html', {'form': form})


@login_required(login_url='../login')
def budget_dashboard(request):
    current_user = request.user
    budgets = Budget.objects.filter(created_by=current_user.id)
    return render(request, 'budget/budget-dashboard.html', context={'budgets': budgets})


@login_required(login_url='../login')
def budget_dashboard_add(request):
    form = BudgetForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.created_by = request.user
            form.save()
            return redirect('budget-dashboard')
    return render(request, 'budget/add.html', context={'form': form})


@login_required(login_url='../login')
def budget_dashboard_delete(request, id_):
    budget = Budget.objects.get(id=id_)
    if request.method == 'POST':
        budget.delete()
        return redirect('budget-dashboard')
    return render(request, 'budget/delete-confirm.html', context={'budget': budget})


@login_required(login_url='../login')
def budget_dashboard_update(request, id_):
    budget = Budget.objects.get(id=id_)
    form = BudgetForm(request.POST or None, instance=budget)
    if form.is_valid():
        form.save()
        return redirect('budget-dashboard')
    return render(request, 'budget/update.html', {'form': form, 'budget': budget})


def logout_view(request):
    logout(request)
    return redirect('index')


def budget_dashboard_details(request, id_):
    budget = Budget.objects.get(id=id_)
    context = {'budget': budget, 'housing_expense': 'test', 'income': 'test income'+str(budget.earned_income)}
    if budget.housing_expense > 10:
        context.update({"income" : 'test 2 updated: '+str(budget.earned_income)})
    return render(request, 'budget/details.html', context)
