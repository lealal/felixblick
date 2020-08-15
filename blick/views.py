from django.shortcuts import render
from django.core.mail import send_mail
from .models import *

def home(request):
    listings = Listing.objects.order_by('-created_at')
    news = News.objects.order_by('-created_at')
    context = {
        'listings': listings,
        'news': news
    }
    return render(request, 'blick/home.html', context)

def listings(request):
    listings = Listing.objects.order_by('-created_at')
    context = {'listings': listings}
    return render(request, 'blick/listings.html', context)

def news(request):
    news = News.objects.order_by('-created_at')
    context = {'news': news}
    return render(request, 'blick/news.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        client = request.POST['client']
        message = request.POST['message']

        context = {
            'name': name,
            'email': email,
            'phone': phone,
            'client': client,
            'message': message
        }

        Contact.objects.create(
            name = name,
            email = email,
            phone = phone,
            client = client,
            message = message
        )

        send_mail(
          'Contact Form - ' + name, #subject
          'Message: ' + message + '\n' + 
          'Email: ' + email + '\n' + 
          'Phone number: ' + phone + '\n' +
          'Client: ' + client + '\n', #message
          email, #from email
          ['blickfelix@gmail.com'], #to email  
        )

        return render(request, 'blick/contact.html', {'name': name})
    
    else:
        context = {}
        return render(request, 'blick/contact.html', context)
