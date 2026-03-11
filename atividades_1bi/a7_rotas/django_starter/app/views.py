from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def exemplo(request):
    return render(request, 'exemplo.html')