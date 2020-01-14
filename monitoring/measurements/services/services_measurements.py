from django.http import HttpResponse
import json
from ..logic.logic_measurements import add_measurement, get_measurement_by_id, find_sensor_mesurements
from places.services.services_sensor import get_sensor_by_code
from django.core import serializers


def post_measurement(request):
    data = request.body.decode('utf-8')
    diccionario = json.loads(data)
    rpta = 'The measurement was added correctly'
    try:
        add_measurement(diccionario)
    except Exception as e:
        rpta = e
    return HttpResponse(rpta)


def get_sensor_measurements(request, sensor_code):
    response = 'No measurements found'
    try:
        sensor = get_sensor_by_code(sensor_code)
        if sensor is None:
            response = 'sensor not found'
        else:
            measurements = find_sensor_mesurements(sensor_code)
            response = serializers.serialize('json', measurements)
    except Exception as e:
        response = e
    return HttpResponse(response)
