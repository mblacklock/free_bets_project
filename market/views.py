from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from bets.models import Affiliate, Item

def new_market(request):
    return redirect('market_manual')

def market_manual(request, bet_type=None, item_id=None):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        item = None
    return render(request, 'market/market.html', {'bet_type': bet_type, 'item': item})
