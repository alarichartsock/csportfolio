from django.shortcuts import render
import re
from django.http import JsonResponse
from django.http import FileResponse
import requests
import os

def mobile(request):
# Return True if the request comes from a mobile device.
    MOBILE_AGENT_RE = re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

    if MOBILE_AGENT_RE.match( request.META['HTTP_USER_AGENT'] ):
        return True
    else:
        return False

# Create your views here.

def index(request):
    return render(request,"index.html") # Desktop users

def resume(request):
    if mobile(request):
        filepath = os.path.join('/home/bitnami/csportfolio/static','assets/documents/Resume.pdf')
        print(filepath)
        return FileResponse(open(filepath,'rb'),content_type='application/pdf')
    else:
        return render(request,"resume.html") # Desktop users

def license(request):
    return render(request,'license.html')