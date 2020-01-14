from django.db import models
from django.apps import apps

# Create your models here.


class Variable(models.Model):
    name = models.CharField(max_length=50)


class Measurement(models.Model):
    value = models.FloatField(null=True, blank=True, default=None)
    unit = models.CharField(max_length=50)
    dateTime = models.DateTimeField(auto_now_add=True)
    variable = models.ForeignKey(
        Variable, on_delete=models.CASCADE, default=None)
    sensor = models.ForeignKey(
        'places.Sensor', on_delete=models.CASCADE, default=None)
