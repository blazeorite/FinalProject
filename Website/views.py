from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, Index")


def budgeting(request):
    return HttpResponse("Hello, budgeting")


def investment(request):
    return HttpResponse("Hello, investment")


def login(request):
    return HttpResponse("Hello, login")


def register(request):
    return HttpResponse("Hello, register")


def budget_dashboard(request):
    return HttpResponse("Hello, budgetdashboard")


def budget_dashboard_add(request):
    return HttpResponse("Hello, budgetdashboard-add")


def budget_dashboard_delete(request):
    return HttpResponse("Hello, budgetdashboard-delete")


def budget_dashboard_update(request):
    return HttpResponse("Hello, budgetdashboard-update")