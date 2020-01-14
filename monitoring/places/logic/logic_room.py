from ..models import Room, Building, Sensor
from django.db import models
from measurements.models import Measurement
from measurements.logic.logic_measurements import get_measurement_by_sensor


def add_room(diccionario):
    room = Room()
    room.floor = diccionario['floor']
    room.code = diccionario['code']
    building_name = diccionario['code'].split("-")[0]
    room.building = Building.objects.get(name=building_name)
    room.save()


def find_room_by_code(p_code):
    return Room.objects.get(code=p_code)


def find_frequent_sensors(room):
    response = []
    all_sensors = Sensor.objects.filter(room=room.id)
    for sensor in all_sensors:
        measurements = get_measurement_by_sensor(sensor.code)
        if len(measurements) > 10:
            response.append(sensor)
    return response
