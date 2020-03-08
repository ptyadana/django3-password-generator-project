from django.shortcuts import render
from django.http import HttpResponse

import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def aboutus(request):
    return render(request, 'generator/about_us.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))

    generated_password = ''

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('specialchars'):
        characters.extend(list('!@#$%^&*()'))
    
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for num in range(length):
        generated_password += random.choice(characters)
   
    return render(request, 'generator/password.html',{'password':generated_password})
