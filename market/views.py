from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from bets.models import Affiliate, Item

def new_market(request):
    return redirect('market_manual')

def market_manual(request, bet_type, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'market/market.html', {'bet_type': bet_type, 'item': item})
