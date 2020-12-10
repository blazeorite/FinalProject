from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
import datetime


# Create your models here.


class Budget(models.Model):
    created_by = models.ForeignKey(User, default=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    budget_name = models.CharField(max_length=100)
    earned_income = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    housing_expense = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    food_expense = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    medical_expense = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    child_care_expense = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    taxes = models.DecimalField(max_digits=20, decimal_places=2, default=0)

class EmailSignup(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254)
