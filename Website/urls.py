from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('budgeting', views.budgeting, name="budgeting"),
    path('investment', views.investment, name="investment"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('budget-dashboard/', views.budget_dashboard,),
    path('budget-dashboard/add', views.budget_dashboard_add, name="budget-dashboard-add"),
    path('budget-dashboard/delete', views.budget_dashboard_delete, name="budget-dashboard-delete"),
    path('budget-dashboard/update', views.budget_dashboard_update, name="budget-dashboard-update"),
    #testing23#
    ## cristian barco
]