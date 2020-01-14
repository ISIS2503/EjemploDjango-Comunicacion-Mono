from ..models import Sensor, Room
from measurements.models import Measurement


def add_sensor(diccionario):
    sensor = Sensor()
    sensor.code = diccionario['code']
    room_code = diccionario['code'].split("-")
    sensor.room = Room.objects.get(code=room_code[0]+'-'+room_code[1])
    sensor.save()


def find_sensor_by_code(p_code):
    return Sensor.objects.get(code=p_code)
