from django.db import models
from django.utils import timezone

CURRENCY = [("UAH", "UAH"), ("USD", "USD")]


class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY)
    type = models.CharField(max_length=50)
    date = models.DateField("Income date", default=timezone.now)

    def __str__(self):
        return f"{self.amount} {self.currency} on {self.date} from {self.type}"


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY)
    type = models.CharField(max_length=50)
    date = models.DateField("Expense date", default=timezone.now)

    def __str__(self):
        return f"{self.amount} {self.currency} on {self.date} for {self.type}"
