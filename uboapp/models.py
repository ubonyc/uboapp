from django.db import models

# Create your models here.
class Building(models.Model):
    address = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=5)


def __str__(self):
    return self.address