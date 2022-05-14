from django.urls import path

from . import views

app_name = 'PortfolioApp'

urlpatterns = [
    path('', views.portfolioView, name='portfolio'),
]