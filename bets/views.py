from django.shortcuts import render, redirect
from django.http import HttpResponse

from bets.models import Affiliate, Item, Summary

# Create your views here.

def home_page(request):        
    return render(request, 'home.html')

def view_summary(request, summary_id):
    summary = Summary.objects.get(id=summary_id)
    items = [item for item in summary.item_set.all()]
    
    return render(request, 'bets/summary.html', {'summary': summary, 'items': items})

def new_summary(request):
    summary = Summary.create_new()
    return redirect(str(summary.get_absolute_url()))


def update_ajax(request, param):
    item = None
    if request.method == 'GET':
        summary_id = request.GET['summary_id']
        summary = Summary.objects.get(id=summary_id)
        if summary:
            name = request.GET['affiliate_name']
            
            if name != 'summary_name':
                affiliate = Affiliate.objects.get(name=name)
                item = Item.objects.get(summary=summary, affiliate=affiliate)

                if param == 'username':
                    item.username = request.GET['value']
                elif param == 'status':
                    item.status = request.GET['value']
                elif param == 'balance':
                    item.balance = request.GET['value']
                elif param == 'profit':
                    item.profit = request.GET['value']
                elif param == 'banked':
                    item.banked = request.GET['value']
                item.save()
                return HttpResponse(item)
    
            else:
                summary.name = request.GET['value']
                summary.save()
                return HttpResponse(summary)

        return HttpResponse(None)
                
            
