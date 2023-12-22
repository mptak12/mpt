from django.db import models
from django.utils import timezone

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
    due_date = models.DateField(blank=True, null=True)

    def set_default_due_date(self):
        if not self.due_date:
            self.due_date = timezone.now() + timezone.timedelta(days=60)

    def save(self, *args, **kwargs):
        self.set_default_due_date()
        super().save(*args, **kwargs)

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
    

class Item(models.Model):
    name = models.CharField(max_length=50)
    animal_id = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    picture = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    due_date = models.DateField(blank=True, null=True)

    def set_default_due_date(self):
        if not self.due_date:
            self.due_date = self.animal_id.due_date

    def save(self, *args, **kwargs):
        self.set_default_due_date()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.price}"
    
class Purchase(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f"User: {self.user_id}\n Items: {self.items}"