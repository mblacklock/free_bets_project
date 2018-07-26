from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from bets.models import Affiliate

def new_market(request):
    return redirect('market_manual')

def market_manual(request):
    affiliates = Affiliate.objects.all()
    return render(request, 'market/market.html', {'affiliates': affiliates})
