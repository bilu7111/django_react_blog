from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    if(request.user.is_authenticated):
        return render(request,"frontend/index.html")
    else:
        return HttpResponseRedirect("login")
