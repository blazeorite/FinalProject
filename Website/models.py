from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Budget(models.Model):
    created_by = models.ForeignKey(User, default=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    budget_name = models.CharField(max_length=100)
    earned_income = models.DecimalField(max_digits=20, decimal_places=2)
    housing_expense = models.DecimalField(max_digits=20, decimal_places=2)
