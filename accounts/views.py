from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib import auth, messages

from accounts.models import Token

# Create your views here.

def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(  
        reverse('login') + '?token=' + str(token.uid)
    )
    
    msg_plain = f'Use this link to log in:\n\n{url}'
    msg_html = render_to_string('accounts/login_email.html', {'url': url})
    
    send_mail(
        'Your login link for Free Bet Maximizer',
        msg_plain,
        'noreply@freebetmaximizer',
        [email],
        html_message=msg_html,
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')

def login(request):
    user = auth.authenticate(uid=request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')
