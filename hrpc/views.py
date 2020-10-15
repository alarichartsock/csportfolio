from django.shortcuts import render
import re

def mobile(request):
# Return True if the request comes from a mobile device.
    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return True
    else:
        return False

# Create your views here.

def index(request):
    if mobile(request):
        return render(request,'mobileindex.html') # Mobile users don't get the cool glitch text effect (breaks on mobile), same for all the other views
    else:
        return render(request,"index.html") # Desktop users

def resume(request):
    if mobile(request):
        return render(request,'mobileresume.html')
    else:
        return render(request,"resume.html") # Desktop users
     

def portfolio(request):
    if mobile(request):
        return render(request,'mobileportfolio.html')
    else:
        return render(request,"portfolio.html") # Desktop users

def contact(request):
    if mobile(request):
        return render(request,'mobilecontact.html')
    else:
        return render(request,"contact.html") # Desktop users