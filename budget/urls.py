from django.urls import path
from . import views
#from Website import views

urlpatterns = [
    path('', views.budget_dashboard, name="budget-dashboard"),
    path('add', views.budget_dashboard_add, name="budget-dashboard-add"),
    path('delete', views.budget_dashboard_delete, name="budget-dashboard-delete"),
    path('update', views.budget_dashboard_update, name="budget-dashboard-update"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    #testing23#
    ## cristian barco
]