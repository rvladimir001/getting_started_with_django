from django.contrib import admin
from django.urls import path
from blog.views import home, test

urlpatterns = [
    path('', home),
    path('test', test)
]
