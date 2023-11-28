from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Animal


def main_page(request):
    #animal1 = Animal.objects.create(name='Kit', type='Cat')
    #animal1.save()

    all_animals = Animal.objects.all
    return render(request, "index.html", {"all": all_animals})


def bump(request, pk):

    a = Animal.objects.get(pk=pk)
    print(f"Updated {a.name}")
    a.donations_amount += 20
    a.total_donations += 1
    a.save()
    return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))


def second_page(request):
    return HttpResponse("This is test page content")


