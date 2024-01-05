from django.contrib import admin
from .models import Animal, Donation, Item

admin.site.register(Animal)
admin.site.register(Item)
admin.site.register(Donation)
