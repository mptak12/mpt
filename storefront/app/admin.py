from django.contrib import admin
from .models import Animal, Donation, Item

admin.site.register(Donation)

admin.site.register(Item)

admin.site.register(Animal)