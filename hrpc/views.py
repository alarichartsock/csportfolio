from django.shortcuts import render

# Create your views here.

def index(request):
     return render(request,"index.html")

def resume(request):
     return render(request,"resume.html")

def portfolio(request):
     return render(request,"portfolio.html")

def contact(request):
     return render(request,"contact.html")