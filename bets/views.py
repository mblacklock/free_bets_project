from django.shortcuts import render, redirect

from bets.models import Summary

# Create your views here.

def home_page(request):
    if request.method == 'POST':
        return redirect('/summary/create_new')
        
    return render(request, 'home.html')

def view_summary(request, summary_id):
    return render(request, 'bets/summary.html')

def new_summary(request):
    summary = Summary.create_new()
    return redirect(str(summary.get_absolute_url()))
