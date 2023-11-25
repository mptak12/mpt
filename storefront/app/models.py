from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.surname}"


class Animal(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    description = models.TextField()
    picture = models.TextField()
    total_donations = models.IntegerField(default=0)
    donations_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    donation_target = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.type} {self.name}"


class TransferType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Donation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    animal_id = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True)
    type_id = models.ForeignKey(TransferType, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    confirmation = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Donation from {self.user_id} to {self.animal_id}. Amount: {self.amount}"