from django.shortcuts import render
from .models import Project

def home(request):
    temp = 'My_home_page'
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'temp': temp, 'projects': projects})
