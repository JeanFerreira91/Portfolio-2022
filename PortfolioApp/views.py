from django.shortcuts import render

# Create your views here.
def portfolioView(request):
    return render(request, 'PortfolioApp/portfolio_index.html')