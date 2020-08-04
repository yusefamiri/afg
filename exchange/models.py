from django.db import models
from datetime import date


class Currency(models.Model):
    country = models.CharField(max_length=50, unique=True)
    iso = models.CharField(max_length=5, unique=True)
    designation = models.CharField(max_length=5, null=True)
    symbol = models.CharField(max_length=5, null=True)
    flag = models.CharField(max_length=1, null=True)

    def __str__(self):
        return "Currency of -- {} -- {}".format(self.country,  self.iso)


class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency')
    buy = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sell = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    change_date_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "Exchange rate of -- {} -- on date: {}".format(self.currency.iso, str(self.change_date_time))

    @property
    def is_today(self):
        return date.today() == self.change_date_time.date()
