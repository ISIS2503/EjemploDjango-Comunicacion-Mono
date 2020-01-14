from django.db import models
from measurements.models import Variable

# Create your models here.


class Building(models.Model):
    name = models.TextField(null=False, default=None)


class Room(models.Model):
    code = models.TextField(null=False, default=None)
    floor = models.IntegerField(null=True, blank=True, default=None)
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, default=None)


class Sensor(models.Model):
    code = models.TextField(null=False, default=None)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, default=None)
