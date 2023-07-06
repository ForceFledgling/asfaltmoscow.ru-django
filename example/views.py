# example/views.py
from datetime import datetime

from django.http import HttpResponse

from django.core.mail import send_mail

from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm

from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        data = request.POST
        subject = 'Новая заявка с сайта asfaltmoscow.ru'
        message = f'''Новая заявка!
        
        Имя: {data["name"]}
        Номер телефона: {data["phone"]}'''
        email(subject, message)
    return render(request, 'index.html', {'form': ContactForm})


# Функция отправки сообщения
def email(subject, content):
   send_mail(subject,
      content,
      'asfaltmoscow.ru@mail.ru',
      ['nairigukasyan2015@mail.ru']
   )
