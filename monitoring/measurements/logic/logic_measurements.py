from ..models import Measurement, Variable
from places.models import Room, Sensor
from django.db import models


def add_measurement(diccionario):
    measurement = Measurement()
    measurement.value = diccionario['value']
    measurement.unit = diccionario['unit']
    variable_name = diccionario['variable']
    measurement.variable = Variable.objects.get(name=variable_name)
    sensor_code = diccionario['sensor']
    measurement.sensor = Sensor.objects.get(code=sensor_code)
    measurement.save()
    return True


def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements


def get_measurement_by_id(measurement_id):
    measurement = Measurement.objects.get(id=measurement_id)
    return measurement


def get_measurement_by_sensor(sensor_code):
    measurement = Measurement.objects.filter(sensor__code=sensor_code)
    return measurement


def find_sensor_mesurements(p_code):
    measurements = Measurement.objects.filter(sensor__code=p_code)
    return measurements
