from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    capacity = models.IntegerField()
    year = models.IntegerField()
    price = models.IntegerField()