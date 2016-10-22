from django.db import models

# Create your models here.
class Building(models.Model):
    streetname = models.CharField(max_length=200, default=0)
    streetnum = models.CharField(max_length=5, default=0)
    zipcode = models.CharField(max_length=5, default=0)
    latitude = models.CharField(max_length=10, default=0)
    longitude = models.CharField(max_length=10, default=0)


def __str__(self):
    return self.streetname