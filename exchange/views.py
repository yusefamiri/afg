from django.core.exceptions import ObjectDoesNotExist
from django.db.models.functions import Coalesce
from django.views.generic import ListView

from exchange.models import ExchangeRate, Currency


class CurrencyDetail(ListView):
    exchange_rates = ExchangeRate
    currencies = Currency
    template_name = 'exchange/currency_detail.html'

    def get_queryset(self):
        return self.exchange_rates.objects.all()\
            .filter(currency__iso=self.kwargs['slug'].upper())\
            .order_by('-change_date_time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['currency'] = self.currencies.objects.get(iso=self.kwargs['slug'].upper())
        except Currency.DoesNotExist:
            context['currency'] = None
        finally:
            context['slug'] = self.kwargs['slug'].upper()
            return context


class ExchangeRateOverview(ListView):
    # finds the latest exchange rate row for each currency
    # TODO: Disable caching
    # TODO: Find django method instead of SQL query
    queryset = ExchangeRate.objects.raw('''SELECT c.*, e1.*
    FROM home_currency c
    JOIN home_exchangerate e1 ON (c.id = e1.currency_id)
    LEFT OUTER JOIN home_exchangerate e2 ON (c.id = e2.currency_id AND 
        (e1.change_date_time < e2.change_date_time OR (e1.change_date_time = e2.change_date_time AND e1.id < e2.id)))
    WHERE e2.id IS NULL''')

    template_name = 'exchange/overview.html'
