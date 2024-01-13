import decimal
import os
from unidecode import unidecode
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import Animal, Item
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


def main_page(request):
    # animal1 = Animal.objects.create(name='Kit', type='Cat')
    # animal1.save()

    all_animals = Animal.objects.all
    return render(request, "index.html", {"all": all_animals})


def save_uploaded_image(uploaded_file, name):
    destination_path = os.path.join(settings.BASE_DIR, 'static', 'images', name)

    # Save the file to the specified destination
    with open(destination_path, 'wb') as destination_file:
        for chunk in uploaded_file.chunks():
            destination_file.write(chunk)

    return destination_path


@csrf_exempt
def dotation_page(request):
    all_animals = Animal.objects.all

    if request.method == "POST":
        if 'imageUpload' in request.FILES:
            # save img
            uploaded_image = request.FILES['imageUpload']
            type_and_name = request.POST.get('collectionName')
            if len(type_and_name.split()) != 2:
                return JsonResponse({'error': 'Niepoprawna nazwa zbiórki'}, status=500)

            saved_path = save_uploaded_image(uploaded_image, f'{unidecode(type_and_name).replace(" ", "_")}.png')

            saved_path = saved_path.split('static\\', 1)[1]
            # add animal
            t, n = type_and_name.split()
            newA = Animal.objects.create(name=n,
                                         type=t,
                                         description=request.POST.get('description'),
                                         picture=saved_path,
                                         total_donations=0,
                                         donations_amount=0,
                                         donation_target=request.POST.get('targetAmount'),
                                         due_date=request.POST.get('endDate')
                                         )

            newA.save()

        elif 'donation_value' in request.POST:
            print("Wplacono " + request.POST.get('donation_value') + " Oferta:" + request.POST.get('offer_pk'))
            animal_pk = request.POST.get('offer_pk')
            animal_val = request.POST.get('donation_value')

            a = Animal.objects.get(pk=animal_pk)
            a.donations_amount += decimal.Decimal(animal_val.replace(',', '.').strip('-'))
            a.total_donations += 1
            a.save()

        else:
            return JsonResponse({'error': "Dodaj obrazek"}, status=500)
    return render(request, "Wplac.html", {"all": all_animals})


@csrf_exempt
def auctions(request):
    all_items = Item.objects.all
    all_animals = Animal.objects.all

    if request.method == "POST":
        if 'imageUpload' in request.FILES:
            uploaded_image = request.FILES['imageUpload']
            item_name = request.POST.get('collectionName')
            saved_path = save_uploaded_image(uploaded_image, f'{unidecode(item_name).replace(" ", "_")}.png')
            saved_path = saved_path.split('static\\', 1)[1]

            connected_animal = get_object_or_404(Animal, pk=int(request.POST.get('dropdownList')))

            newItem = Item.objects.create(name=item_name,
                                          animal_id=connected_animal,
                                          description=request.POST.get('description'),
                                          picture=saved_path,
                                          price=request.POST.get('targetAmount'),
                                          )
            newItem.save()

        else:
            item_pk = request.POST.get('offer_pk')
            val = request.POST.get('value')
            print("Wpłacono" + val + "na item o kluczu" + item_pk)

            item = Item.objects.get(pk=item_pk)
            item.price = int(val)
            item.save()

    return render(request, "Licytacje.html", {"items": all_items, "animals": all_animals})


def about_us(request):
    return render(request, "O-nas.html")


def login(request):
    return render(request, "Login.html")
