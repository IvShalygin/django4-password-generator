from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html', )


def password(request):
    characters = list('abcdefgijklmnopqrstuvwxyz', )
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGIJKLMNOPQRSTUVWXYZ', ))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789', ))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+', ))
    length = int(request.GET.get('length', 12))

    the_password = ''
    for x in range(length):
        the_password += random.choice(characters)
    return render(request, 'generator/password.html', {'password': the_password})


def about(request):
    about_create = 'Created by Dark_unicorn'
    about_why = 'This created for two targets: 1. Main target it\'s train, 2. Generic password with given parameters'
    return render(request, 'generator/about.html', {'about_create': about_create, 'about_why': about_why})
