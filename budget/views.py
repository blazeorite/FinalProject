from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def budget(request):
    return HttpResponse("Hello, budget")


def budget_dashboard(request):
    return HttpResponse("Hello, budgetdashboard")


def budget_dashboard_add(request):
    return HttpResponse("Hello, budgetdashboard-add")


def budget_dashboard_delete(request):
    return HttpResponse("Hello, budgetdashboard-delete")


def budget_dashboard_update(request):
    return HttpResponse("Hello, budgetdashboard-update")


def login(request):
    return redirect('login')


def register(request):
    return None