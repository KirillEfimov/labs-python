from django.db import models


class UserModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)


class PlaneModel(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    description = models.CharField(max_length=255)


class BookingModel(models.Model):
    user_id = models.ForeignKey(UserModel)
    plane_id = models.ForeignKey(PlaneModel)
    price = models.IntegerField()
    departure_date = models.DateField()
