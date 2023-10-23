from django.shortcuts import render
from django.http import HttpResponse


def say_sth(request):
    return render(request, "first.html") #HttpResponse("hi")
