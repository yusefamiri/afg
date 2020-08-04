from django.shortcuts import redirect
from django.views.generic import ListView

from blog.models import Post
from exchange.models import ExchangeRate


class Homepage(ListView):
    queryset = Post.objects.filter(status=1).order_by('creation_date')[:2]
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exchangerate_list'] = ExchangeRate.objects.raw('''SELECT c.*, e1.*
    FROM exchange_currency c
    JOIN exchange_exchangerate e1 ON (c.id = e1.currency_id)
    LEFT OUTER JOIN exchange_exchangerate e2 ON (c.id = e2.currency_id AND
        (e1.change_date_time < e2.change_date_time OR (e1.change_date_time = e2.change_date_time AND e1.id < e2.id)))
    WHERE e2.id IS NULL''')
        return context
