from django.shortcuts import render

# Create your views here.

def odds_converter(request):        
    return render(request, 'betting_tools/converter.html')
