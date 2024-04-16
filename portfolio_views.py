from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def work(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/work.html', {'projects': projects})

def contact(request):
    return render(request, 'portfolio/contact.html')