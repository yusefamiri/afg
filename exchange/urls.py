from django.urls import path

from exchange import views

app_name = 'exchange'
urlpatterns = [
    path('', views.ExchangeRateOverview.as_view(), name='overview'),
    path('<slug:slug>/', views.CurrencyDetail.as_view(), name='currency_detail'),
]
