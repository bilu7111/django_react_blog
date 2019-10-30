from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, JsonResponse
from django.utils import timezone
from .models import Article


def addArticle(request):
    if(request.user.is_authenticated):
        print(request.GET)
        heading = request.GET.get("heading")
        content = request.GET.get("content")
        print(heading,content)
        article = Article(heading=heading,content=content,date_pub=timezone.now())
        article.author = request.user
        article.save() 
        return HttpResponseRedirect("/")
    else:
        return render(request,"backend/login.html",{"error":"Please Login First"})

def getArticle(request):
    if(request.user.is_authenticated):
        title = request.GET.get('heading')
        article = Article.objects.filter(heading=title).values_list('heading','content','date_pub')
        return JsonResponse({"article":article[0]})
    else:
        return HttpResponseRedirect("/login")

def getArticles(request):
    if(request.user.is_authenticated):
        articles = Article.objects.filter(author=request.user).values_list('heading','content','date_pub')
        result = []
        for article in articles:
            result.append(article)
        return JsonResponse({"articles":result})
    else:
        return render(request,"backend/login.html",{"error":"Please Login First"})

def loginPage(request):
    if(request.user.is_authenticated):
        return HttpResponseRedirect("/")
    else:
        return render(request,"backend/login.html")

def loginUser(request):
    print(request.POST)
    username = request.POST.get("username")
    password = request.POST.get("password")
    print(username, password)
    auth = authenticate(request,username=username,password=password)
    if(auth):
        login(request, auth)
        return HttpResponseRedirect("/")
    else:
        return render(request,"backend/login.html",{"error":"Wrong email or password"})