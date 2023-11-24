from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    return render(request, "index.html")


def second_page(request):
    return HttpResponse("This is test page content")
