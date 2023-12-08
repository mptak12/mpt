from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Animal
from django.views.decorators.csrf import csrf_exempt


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


@csrf_exempt
def dotation_page(request):
    if request.method == "POST":
        print("Wplacono " + request.POST.get('donation_value') + " Oferta:" + request.POST.get('offer_pk'))
        animal_pk = request.POST.get('offer_pk')
        animal_val = request.POST.get('donation_value')

        a = Animal.objects.get(pk=animal_pk)
        a.donations_amount += int(animal_val)
        a.total_donations += 1
        a.save()
        return redirect('donations')
    return render(request, "Wplac.html")


def about_us(request):
    return render(request, "O-nas.html")


def auctions(request):
    return render(request, "Licytacje.html")


def login(request):
    return render(request, "Login.html")