from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Expense(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.description


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plain_password = models.CharField(max_length=128)