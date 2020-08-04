from django.contrib import admin

# Register your models here.
from exchange.models import Currency, ExchangeRate

admin.site.register(Currency)
admin.site.register(ExchangeRate)
