from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Budget, EmailSignup
from .forms import BudgetForm, EmailForm
from django.contrib.auth import logout


# Create your views here.
def index(request):
    form = EmailForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'budget/index.html', {'form': form})


def budgeting(request):
    return render(request, 'budgeting.html')


def investment(request):
    return render(request, 'investment.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # get the user info from the form data and log in the user
            user = form.get_user()
            login(request, user)
            return redirect('budget-dashboard')
        else:
            return redirect('login_view')
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
    budgets = Budget.objects.filter(created_by=current_user.id).order_by('-created_at')
    return render(request, 'budget/budget-dashboard.html', context={'budgets': budgets, 'current_user': current_user})


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


@login_required(login_url='../login')
def budget_dashboard_details(request, id_):
    budget = Budget.objects.get(id=id_)
    # store the benchmark numbers
    expenses_avg = {'housing': 1689, 'food': 657, 'childcare': 500, 'medical': 357, 'taxes': 1374, 'total': 4100}

    # calculate the total expenses of the budget.
    total_expenses = budget.housing_expense + budget.food_expense + budget.child_care_expense + budget.medical_expense + budget.taxes

    # calculator the difference between benchmark - budget expenses.
    difference = {'housing': 1689 - budget.housing_expense, 'food': 657 - budget.food_expense,
                  'childcare': 500 - budget.child_care_expense, 'medical': 357 - budget.medical_expense,
                  'taxes': 1374 - budget.taxes, 'total': 4100 - total_expenses}

    # calculate how much is left over. income-expenses.
    leftover = budget.earned_income - total_expenses

    # pass the budget, the benchmark numbers, the differnce, the total expeneses
    # and also the comments.

    context = {'budget': budget, 'expenses_avg': expenses_avg, 'difference': difference,
               'total': total_expenses,
               'housing_expense_comment': 'You are good',
               'income_comment': 'Good job, your income $' +
                                 str(budget.earned_income) +
                                 ' is able to cover your expenses for each month. And you will have ' +
                                 str(leftover) + ' left over'}

    if leftover < 0:
        context.update({'income_comment': 'Sorry, Look likes your income $' +
                                          str(budget.earned_income) +
                                          ' is not able to cover your expenses for each month. And you will be in $' +
                                          str(abs(leftover)) + ' of debt'})

    # if budget.housing_expense > 10:
    #     context.update({"income": 'test 2 updated: '+str(budget.earned_income)})
    return render(request, 'budget/details.html', context)
