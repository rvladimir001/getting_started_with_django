from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def home(request):
    #posts = Article.objects.all()
    posts = Article.objects.order_by('created_at')
    return render(request, 'blog/index.html', {'posts': posts})


def test(request):
    return HttpResponse('<h1>какая-то тестовая страница</h1><br><br><a href="/">на главную</a>')
