from django.shortcuts import render

# Create your views here.

from django.core.mail import BadHeaderError, EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm

def contact_form(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            content = form.cleaned_data['content']
            try:
                email = EmailMessage(contact_name,
                                    content,
                                    contact_email,
                                    ['matthewblacklock@gmail.com'], #change to your email
                                     reply_to=[contact_email],
                                   )
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact_thanks')
    return render(request, 'blog/contact.html', {'form': form})


def contact_thanks(request):
    return render(request, 'blog/contact_thanks.html', {})
