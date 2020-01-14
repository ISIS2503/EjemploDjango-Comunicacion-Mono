from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
import json
from ..logic.logic_sensor import add_sensor, find_sensor_by_code


def post_sensor(request):
    data = request.body.decode('utf-8')
    diccionario = json.loads(data)
    rpta = 'The sensor was added correctly'
    try:
        add_sensor(diccionario)
    except Exception as e:
        rpta = e
    return HttpResponse(rpta)


def get_sensor_by_code(sensor_code):
    response = 'No measurements found'
    try:
        response = find_sensor_by_code(sensor_code)
    except Exception as e:
        response = e
    return response
