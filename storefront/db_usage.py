#
# Note: If you make changes in database models (app.models), prepare migrations and migrate changes to database:
# python manage.py makemigrations
# python manage.py migrate
#
# db_usage.py:
# Examples of how to use the database with a few useful methods.
# Note: The script at the end deletes all data from the database, make sure you have a backup of your data before running it.
#
from storefront.wsgi import * # To set env variables, not needed in project
from app.models import User, Animal, TransferType, Donation
from decimal import Decimal
import datetime

# Add one record to tables
user = User.objects.create(name='John', surname='Kowalsky', email='jk@pdf.com', password='kolysanka', birth_date='2000-01-01') # Default date format: YYYY-MM-DD)

animal1 = Animal.objects.create(name='Kit', type='Cat')
animal2 = Animal.objects.create(name='Leszek', type='Dog')

# datetime.date
d = datetime.date(2024, 6, 27)
animal2.due_date = d

transferTypes = ['barter','blik','przelew tradycyjny','paysafecard']
for type in transferTypes:
    transferT = TransferType.objects.create(type=type)

transfer_types = TransferType.objects.all()
for t in transfer_types:
    print(f"ID: {t.id}, {t}")
          
donation = Donation.objects.create(user_id=user, animal_id=animal1, type_id=TransferType.objects.get(type="przelew tradycyjny"), amount=50.50)
donation2 = Donation.objects.create(user_id=user, animal_id=animal2, type_id=TransferType.objects.get(type='barter'), amount=607.06)

# Modify records
donations_to_update_for_animal1 = Donation.objects.filter(animal_id=animal1.id)
donations_to_update_for_animal2 = Donation.objects.filter(animal_id=animal2.id)

for d in donations_to_update_for_animal1:
    animal1.donation_target = 100.00
    animal1.donations_amount = Decimal(animal1.donations_amount)+d.amount
    animal1.total_donations += 1

for d in donations_to_update_for_animal2:
    animal2.donation_target = 500.00
    animal2.donations_amount = Decimal(animal2.donations_amount) + d.amount
    animal2.total_donations += 1

animal1.save()
animal2.save()

# Print tables
users = User.objects.all()
animals = Animal.objects.all()
donations = Donation.objects.all()
transfer_types = TransferType.objects.all()

print("User:")
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Surname: {user.surname}, Email: {user.email}, Password: {user.password}, Birthdate: {user.birth_date}")

print("\nAnimal:")
for animal in animals:
    print(f"ID: {animal.id}: {animal}, Funds collected: {animal.donations_amount}/{animal.donation_target}, Total donations: {animal.total_donations}, Due date: {animal.due_date}")

print("\nDonation:")
for donation in donations:
    print(f"ID: {donation.id}, {donation}, TransferType: {donation.type_id}, Date: {donation.date}")


animals.delete()
transfer_types.delete()
users.delete()
donations.delete()

# Print tables
donations = Donation.objects.all() 
users = User.objects.all()
animals = Animal.objects.all()
transfer_types = TransferType.objects.all()

print("\nUser:")
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Surname: {user.surname}, Email: {user.email}, Password: {user.password}, Birthdate: {user.birth_date}")

print("\nAnimal:")
for animal in animals:
    print(f"ID: {animal.id}: {animal}, Funds collected: {animal.donations_amount}/{animal.donation_target}, Total donations: {animal.total_donations}")

print("\nDonation:")
for donation in donations:
    print(f"ID: {donation.id}, {donation}, TransferType: {donation.type_id}, Date: {donation.date}")


# The flush command clears the entire database and migrates the data back, essentially performing a clear and create.
# This is necessary to reset the incrementation of model IDs.
import subprocess
subprocess.run(['python', 'manage.py', 'flush'], input='yes'.encode())