from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
User = get_user_model()

from bets.models import Affiliate, Click, Item, Summary

# Create your views here.

def home_page(request):        
    return render(request, 'home.html')

def blog_redirect(request): 
    return redirect('/blog/') # blog_only
    
def view_summary(request, summary_id):
    summary = Summary.objects.get(id=summary_id)
    items = [item for item in summary.item_set.all()]
    
    return render(request, 'bets/summary.html', {'summary': summary, 'items': items})

def new_summary(request):
    summary = Summary.create_new()
    
    if request.user.is_authenticated:
        summary.owner = request.user
        summary.save()
        
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

def action(request, item_id):
    if request.method == 'POST':
        status = request.POST['action']
        item = Item.objects.get(id=item_id)
        if status == 'signup' or status == 'deposit':
            return redirect('affiliate_click', slug= item.affiliate.slug)
        elif status == 'initial' or status == 'free':
            return redirect('market_manual', item_id= item.id, bet_type= status)
    return redirect('home')

def my_summaries(request, email):
    owner = User.objects.get(email=email)
    return render(request, 'bets/my_summaries.html', {'owner': owner})
            
def affiliate_click(request, slug):
    affiliate = get_object_or_404(Affiliate, slug=slug)
    click = Click.objects.create(affiliate=affiliate)
    if request.user.is_authenticated:
        click.user = request.user
        click.save()
    
    return redirect(affiliate.url)

def tracking(request):
    clicks = Click.objects.all()
    return render(request, 'bets/tracking.html', {'clicks': clicks})
            
