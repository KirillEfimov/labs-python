from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class Traveler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)


class Plane(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    description = models.CharField(max_length=255,null=True)

    objects = models.Manager()

class Booking(models.Model):
    user = models.ForeignKey(Traveler, on_delete=models.CASCADE)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    price = models.IntegerField()
    departure_date = models.DateField()
    


