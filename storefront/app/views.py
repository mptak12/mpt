from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal

def main_page(request):
    #animal1 = Animal.objects.create(name='Kit', type='Cat')
    #animal1.save()

    all_animals = Animal.objects.all
    return render(request, "index.html", {"all": all_animals})


def second_page(request):
    return HttpResponse("This is test page content")
