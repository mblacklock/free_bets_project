from django.shortcuts import render

# Create your views here.

def summary_page(request):
    return render(request, 'bets/summary.html')
