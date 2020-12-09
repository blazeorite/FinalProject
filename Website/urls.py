from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('budgeting', views.budgeting, name="budgeting"),
    path('investment', views.investment, name="investment"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('budget-dashboard/', include('budget.urls'))
    #testing23#
    ## cristian barco
]