from django.db import models

# Create your models here.


class Parking(models.Model):
    max_spaces = models.IntegerField(default=15)
    address = models.TextField(blank=True)


class Vehicle(models.Model):
    parking = models.ForeignKey(Parking, blank=True, null=True, on_delete=models.SET_NULL)
    car_registration = models.CharField(max_length=15)
    color = models.CharField(max_length=50, blank=True)
    size = models.FloatField(blank=True)
    KMs_for_liter = models.FloatField(blank=True)