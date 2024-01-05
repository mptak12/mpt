import decimal
import os
import uuid

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Animal
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

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


def save_uploaded_image(uploaded_file, name):
    # Generate a unique filename using uuid
    # unique_filename = str(uuid.uuid4()) + os.path.splitext(uploaded_file.name)[-1]

    # Specify the destination path (assuming 'media/images/' as an example)
    destination_path = os.path.join(settings.BASE_DIR, 'assets', 'images', name)

    # Save the file to the specified destination
    with open(destination_path, 'wb') as destination_file:
        for chunk in uploaded_file.chunks():
            destination_file.write(chunk)

    # Return the path where the file is saved
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
            saved_path = save_uploaded_image(uploaded_image, f'{type_and_name}.png')

            saved_path = saved_path.split('images\\', 1)[1]
            saved_path = saved_path.replace(" ", "_")
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


def about_us(request):
    return render(request, "O-nas.html")


def auctions(request):
    return render(request, "Licytacje.html")


def login(request):
    return render(request, "Login.html")